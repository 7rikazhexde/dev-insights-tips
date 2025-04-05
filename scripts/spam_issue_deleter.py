#!/usr/bin/env python3
"""
GitHub スパムIssue削除スクリプト (spam_issue_deleter.py)
特定のキーワードを含むタイトルや本文のIssueを自動的に検出して削除（クローズまたは完全削除）します

[概要]
このスクリプトは、GitHubリポジトリのオープンIssueをスキャンし、事前定義されたキーワードパターンに
一致するタイトルや本文を持つスパムIssueを自動的に検出して削除します。これにより、
リポジトリ管理者はスパムIssueに対応する時間を節約し、リスク（特に悪意のあるリンクのクリック）を
軽減できます。

[主な機能]
- GitHub APIを使用してオープンIssueを取得
- 事前定義されたキーワードパターンでタイトルと本文をスキャン
- スパムと判断されたIssueに対して以下のアクションを実行:
  - 完全削除（デフォルト）またはクローズ
  - クローズ理由のコメント追加（デフォルト有効）
  - スパムラベルの追加（デフォルト無効）
- ログファイルに詳細な実行記録を保存

[設定方法]
1. 環境変数の設定:
   - SPAM_ISSUE_DELETER: GitHub Fine-Grained Personal Access Token
   - REPO_OWNER, REPO_NAME: リポジトリの所有者と名前（オプション、自動検出も可能）

2. 必要な権限（Fine-Grained PAT）:
   - Repository permissions > Issues: Read and write
   - Repository permissions > Metadata: Read-only
   - Repository permissions > Administration: Read and write (削除機能を使用する場合)

3. カスタマイズ:
   - SPAM_KEYWORDS リストでスパムパターンを追加/変更可能
   - process_issues() 呼び出し時のパラメータでラベル追加やコメント追加を制御可能

[使用方法]
- 手動実行: `python scripts/spam_issue_deleter.py`
- GitHub Actionsでの自動実行: .github/workflows/delete-spam-issues.yml を参照

[依存ライブラリ]
- requests: HTTP通信用
- GitHub CLI (gh): リポジトリ情報取得用（オプション）

作成: 2025-03-16
Python: 3.12.3
ライセンス: MIT
"""

import json
import logging
import os
import re
import subprocess
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Pattern, Tuple, TypedDict, cast

import requests

# ロギング設定
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("spam_issue_deleter.log")],
)
logger = logging.getLogger(__name__)

# 環境変数から設定を読み込む
_token: Optional[str] = os.getenv("SPAM_ISSUE_DELETER")
if not _token:
    logger.error("SPAM_ISSUE_DELETER 環境変数が設定されていません。")
    sys.exit(1)

# この時点でトークンはNoneではないことが確定
GITHUB_TOKEN: str = _token

# GitHub API エンドポイント
GITHUB_API = "https://api.github.com"

# スパムとみなすタイトルのキーワードパターン
SPAM_KEYWORDS = [
    r"viagra|cialis",
    r"earn money|make money|fast cash",
    r"casino|gambling|betting",
    r"crypto offer|bitcoin investment",
    r"dating site|hot singles",
    r"cheap (ray[\s-]?ban|nike|adidas)",
    r"(free|cracked) (software|games|movies)",
    r"weight loss pill",
    r"enlarge your",
    r"работа",
    r"成人|情色|色情",
    r"贷款|借钱",
    r"バイアグラ|カマグラ|媚薬",
    r"副業|投資|お金|儲か",
    # GitHub特有のセキュリティスパム
    r"unusual.*sign.?in|suspicious.*activity|security.*alert",
    r"account.*compromised|account.*security|unauthorized.*access",
    r"detected.*new.*device|login.*from.*new.*location",
    r"password.*reset.*required|security.*breach",
    # 必要に応じてキーワードを追加
]


def get_repo_info() -> Tuple[str, str]:
    """
    GitHub CLI (gh) を使用して現在のリポジトリ情報を取得

    Returns:
        tuple: (owner, repo) のタプル
    """
    try:
        # 現在のリポジトリURLを取得
        result = subprocess.run(
            [
                "gh",
                "repo",
                "view",
                "--json",
                "owner,name",
                "-q",
                "[.owner.login, .name]",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        output = result.stdout.strip()

        # JSON形式の結果をパース
        owner, repo = json.loads(output)

        logger.info(f"リポジトリ情報を取得しました: {owner}/{repo}")
        return owner, repo
    except (subprocess.SubprocessError, json.JSONDecodeError, ValueError) as e:
        logger.error(f"gh コマンドでのリポジトリ情報の取得に失敗しました: {e}")

        # 環境変数を確認
        owner = os.getenv("REPO_OWNER")
        repo = os.getenv("REPO_NAME")

        if owner and repo:
            logger.info(f"環境変数からリポジトリ情報を使用します: {owner}/{repo}")
            return owner, repo

        # 最後の手段: git remoteからURLを解析
        try:
            result = subprocess.run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True,
                text=True,
                check=True,
            )
            git_url = result.stdout.strip()

            # GitHub URLの形式: https://github.com/owner/repo.git または git@github.com:owner/repo.git
            if "github.com" in git_url:
                if git_url.startswith("http"):
                    # HTTPS URL
                    parts = git_url.split("/")
                    if len(parts) >= 2:
                        owner = parts[-2]
                        repo = parts[-1].removesuffix(".git")
                else:
                    # SSH URL
                    parts = git_url.split(":")[-1].split("/")
                    if len(parts) >= 2:
                        owner = parts[-2]
                        repo = parts[-1].removesuffix(".git")

                if owner and repo:
                    logger.info(f"Gitリモート情報から取得: {owner}/{repo}")
                    return owner, repo
        except subprocess.SubprocessError as e:
            logger.error(f"Git remoteからの情報取得に失敗しました: {e}")

        logger.error(
            "リポジトリ情報が取得できません。REPO_OWNER と REPO_NAME を環境変数で指定してください。"
        )
        sys.exit(1)


class IssueType(TypedDict):
    """Issueオブジェクトの型定義"""

    number: int
    title: str
    url: str
    html_url: str
    state: str
    body: Optional[str]
    user: Dict[str, Any]
    pull_request: Optional[Dict[str, Any]]


class GitHubSpamIssueDeleter:
    """GitHub スパムIssue検出・削除クラス"""

    def __init__(self, token: str, owner: str, repo: str, spam_patterns: List[str]):
        """
        初期化

        Args:
            token: GitHub API トークン
            owner: リポジトリのオーナー (ユーザー名または組織名)
            repo: リポジトリ名
            spam_patterns: スパムと判断するキーワードパターンのリスト
        """
        self.token: str = token
        self.owner: str = owner
        self.repo: str = repo
        self.headers: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github.v3+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

        # 正規表現パターンをコンパイル
        self.spam_patterns: List[Pattern[str]] = [
            re.compile(pattern, re.IGNORECASE) for pattern in spam_patterns
        ]

        # 設定の検証
        if not all([token, owner, repo]):
            logger.error("設定が不完全です。トークンとリポジトリ情報が必要です。")
            sys.exit(1)

        logger.info(f"対象リポジトリ: {owner}/{repo}")

    def fetch_open_issues(self, per_page: int = 100) -> List[IssueType]:
        """
        オープン状態のIssueを取得

        Args:
            per_page: 1ページあたりの取得数 (最大100)

        Returns:
            Issue のリスト
        """
        url = f"{GITHUB_API}/repos/{self.owner}/{self.repo}/issues"
        params: Dict[str, Any] = {
            "state": "open",
            "per_page": per_page,
            "sort": "created",
            "direction": "desc",
        }

        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()

            issues: List[Any] = response.json()
            logger.info(f"{len(issues)}件のオープンIssueを検出しました")

            # Pull Requestsは除外（GitHubのAPIではIssueに含まれる）
            issues = [issue for issue in issues if "pull_request" not in issue]
            logger.info(f"Pull Requestsを除外した結果: {len(issues)}件のIssue")

            return cast(List[IssueType], issues)

        except requests.exceptions.RequestException as e:
            logger.error(f"Issueの取得中にエラーが発生しました: {e}")
            if hasattr(e, "response") and e.response is not None:
                logger.error(f"レスポンス: {e.response.text}")
            return []

    def is_spam_title(self, title: str) -> bool:
        """
        タイトルがスパムパターンに一致するか確認

        Args:
            title: Issueのタイトル

        Returns:
            スパムと判断された場合はTrue
        """
        for pattern in self.spam_patterns:
            if pattern.search(title):
                return True
        return False

    def is_spam_body(self, body: Optional[str]) -> bool:
        """
        本文がスパムパターンに一致するか確認

        Args:
            body: Issueの本文（None の場合もある）

        Returns:
            スパムと判断された場合はTrue
        """
        if not body:
            return False

        for pattern in self.spam_patterns:
            if pattern.search(body):
                return True
        return False

    def is_spam(self, issue: IssueType) -> bool:
        """
        IssueがスパムかどうかをタイトルまたはBODYから判断

        Args:
            issue: 検査対象のIssue

        Returns:
            スパムと判断された場合はTrue
        """
        title = issue["title"]
        body = issue.get("body")

        # タイトルまたは本文がスパムパターンと一致
        return self.is_spam_title(title) or self.is_spam_body(body)

    def close_issue(self, issue_number: int) -> bool:
        """
        Issue をクローズ

        Args:
            issue_number: クローズするIssueの番号

        Returns:
            成功した場合はTrue
        """
        url = f"{GITHUB_API}/repos/{self.owner}/{self.repo}/issues/{issue_number}"
        data = {"state": "closed"}

        try:
            response = requests.patch(url, headers=self.headers, json=data)
            response.raise_for_status()

            logger.info(f"Issue #{issue_number} をクローズしました")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(
                f"Issue #{issue_number} のクローズ中にエラーが発生しました: {e}"
            )
            if hasattr(e, "response") and e.response is not None:
                logger.error(f"レスポンス: {e.response.text}")
            return False

    def delete_issue(self, issue_number: int) -> bool:
        """
        Issueを完全に削除（GitHub GraphQL APIを使用）

        Args:
            issue_number: 削除するIssueの番号

        Returns:
            成功した場合はTrue
        """
        # GraphQL APIのエンドポイント
        url = "https://api.github.com/graphql"

        # まずIssueのIDを取得する必要があります（GraphQLはnode IDが必要）
        query_id = """
        query GetIssueID($owner: String!, $repo: String!, $number: Int!) {
          repository(owner: $owner, name: $repo) {
            issue(number: $number) {
              id
            }
          }
        }
        """

        variables_id = {"owner": self.owner, "repo": self.repo, "number": issue_number}

        try:
            # IssueのIDを取得
            response = requests.post(
                url,
                headers=self.headers,
                json={"query": query_id, "variables": variables_id},
            )
            response.raise_for_status()

            data = response.json()
            if "errors" in data:
                logger.error(f"GraphQL エラー: {data['errors']}")
                return False

            issue_id = data["data"]["repository"]["issue"]["id"]

            # DeleteIssueミューテーションを実行
            mutation = """
            mutation DeleteIssue($id: ID!) {
              deleteIssue(input: {issueId: $id}) {
                repository {
                  id
                }
              }
            }
            """

            variables = {"id": issue_id}

            delete_response = requests.post(
                url,
                headers=self.headers,
                json={"query": mutation, "variables": variables},
            )
            delete_response.raise_for_status()

            delete_data = delete_response.json()
            if "errors" in delete_data:
                logger.error(f"GraphQL 削除エラー: {delete_data['errors']}")
                return False

            logger.info(f"Issue #{issue_number} を完全に削除しました")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"Issue #{issue_number} の削除中にエラーが発生しました: {e}")
            if hasattr(e, "response") and e.response is not None:
                logger.error(f"レスポンス: {e.response.text}")
            return False

    def add_spam_label(self, issue_number: int) -> bool:
        """
        Issueにスパムラベルを追加

        Args:
            issue_number: ラベルを追加するIssueの番号

        Returns:
            成功した場合はTrue
        """
        url = (
            f"{GITHUB_API}/repos/{self.owner}/{self.repo}/issues/{issue_number}/labels"
        )
        data = {"labels": ["spam"]}

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()

            logger.info(f"Issue #{issue_number} にスパムラベルを追加しました")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"ラベル追加中にエラーが発生しました: {e}")
            if hasattr(e, "response") and e.response is not None:
                logger.error(f"レスポンス: {e.response.text}")
            return False

    def add_spam_comment(self, issue_number: int) -> bool:
        """
        スパムIssueにコメントを追加

        Args:
            issue_number: コメントを追加するIssueの番号

        Returns:
            成功した場合はTrue
        """
        url = f"{GITHUB_API}/repos/{self.owner}/{self.repo}/issues/{issue_number}/comments"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "body": f"このIssueはスパムとして検出され、自動的にクローズされました。\nDetected as spam and automatically closed at {now}."
        }

        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()

            logger.info(f"Issue #{issue_number} にスパムコメントを追加しました")
            return True

        except requests.exceptions.RequestException as e:
            logger.error(f"コメント追加中にエラーが発生しました: {e}")
            if hasattr(e, "response") and e.response is not None:
                logger.error(f"レスポンス: {e.response.text}")
            return False

    def process_issues(
        self,
        add_label: bool = False,
        add_comment: bool = True,
        delete_issue: bool = True,
    ) -> int:
        """
        スパムIssueを検出して処理

        Args:
            add_label: スパムラベルを追加するかどうか
            add_comment: スパムコメントを追加するかどうか
            delete_issue: Issueを完全に削除するかどうか (Trueの場合はクローズの代わりに削除)

        Returns:
            処理したスパムIssueの数
        """
        issues = self.fetch_open_issues()
        processed_count = 0
        spam_detected = False

        for issue in issues:
            issue_number = issue["number"]
            title = issue["title"]

            if self.is_spam(issue):
                spam_detected = True
                # スパム元情報をログに記録
                if "body" in issue and issue["body"]:
                    body_preview = issue["body"][:100] + (
                        "..." if len(issue["body"]) > 100 else ""
                    )
                    logger.info(f'スパムを検出: Issue #{issue_number} - "{title}"')
                    logger.info(f"本文抜粋: {body_preview}")
                else:
                    logger.info(f'スパムを検出: Issue #{issue_number} - "{title}"')

                # スパムラベルを追加（オプション）
                if add_label:
                    self.add_spam_label(issue_number)

                # スパムコメントを追加（オプション）
                if add_comment:
                    self.add_spam_comment(issue_number)

                # Issueを処理（削除またはクローズ）
                if delete_issue:
                    # Issueを削除
                    if self.delete_issue(issue_number):
                        processed_count += 1
                else:
                    # Issueをクローズ
                    if self.close_issue(issue_number):
                        processed_count += 1

        if not spam_detected:
            logger.info("スパムIssueは検出されませんでした。")

        return processed_count


def main() -> None:
    """メイン処理"""
    logger.info("スパムIssue削除プロセスを開始します...")

    # リポジトリ情報を取得
    owner, repo = get_repo_info()

    # スパム削除ツールの初期化
    deleter = GitHubSpamIssueDeleter(
        token=GITHUB_TOKEN,  # ここでGITHUB_TOKENはnot Noneとチェック済み
        owner=owner,
        repo=repo,
        spam_patterns=SPAM_KEYWORDS,
    )

    # 処理実行
    processed_count = deleter.process_issues(
        add_label=False,  # スパムラベルを追加するかどうか
        add_comment=True,  # スパムコメントを追加するかどうか
        delete_issue=True,  # Issueを完全に削除するかどうか
    )

    if processed_count > 0:
        logger.info(f"処理完了: {processed_count}件のスパムIssueを削除しました")
    else:
        logger.info("処理完了: スパムIssueは見つかりませんでした")


if __name__ == "__main__":
    main()
