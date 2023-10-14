# AWS CLI

公式サイト([https://aws.amazon.com/jp/cli/](https://aws.amazon.com/jp/cli/))引用:

> AWS コマンドラインインターフェイス (AWS CLI) は、AWS のサービスを管理するための統合ツールです。ダウンロードおよび設定用の単一のツールのみを使用して、コマンドラインから AWS の複数のサービスを制御し、スクリプトを使用してこれらを自動化することができます。
>
> AWS CLI v2 は、いくつもの新しい機能を提供します。インストーラの向上、および AWS IAM アイデンティティセンター (AWS SSO の後継) やインタラクティブな機能といった新しい設定オプションが含まれます。

!!! warning

    以下は備忘録を含みます。使い方の詳細は公式サイトを確認してください。

## For Mac

### Homebrewによるインストール

#### brew serch

??? info "brew info awscli"

    ```bash
    ==> awscli: stable 2.13.22 (bottled), HEAD
    Official Amazon AWS command-line interface
    https://aws.amazon.com/cli/
    Not installed
    From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/a/awscli.rb
    License: Apache-2.0
    ==> Dependencies
    Build: cmake ✘, pkg-config ✔, rust ✘
    Required: cffi ✘, docutils ✘, openssl@3 ✔, pycparser ✘, python@3.11 ✔, six ✘
    ==> Options
    --HEAD
     Install HEAD version
    ==> Caveats
    The "examples" directory has been installed to:
      /usr/local/share/awscli/examples
    ==> Analytics
    install: 129,295 (30 days), 341,177 (90 days), 722,229 (365 days)
    install-on-request: 128,405 (30 days), 338,558 (90 days), 716,665 (365 days)
    build-error: 1 (30 days)
    ```

#### brew install

??? info "brew install awscli"

    ※一部環境変数に置き換えています。

    ```bash
    brew install awscli
    ==> Downloading https://ghcr.io/v2/homebrew/core/awscli/manifests/2.13.22
    ######################################################################### 100.0%
    ==> Fetching dependencies for awscli: pycparser, cffi, docutils and six
    ==> Downloading https://ghcr.io/v2/homebrew/core/pycparser/manifests/2.21-1
    ######################################################################### 100.0%
    ==> Fetching pycparser
    ==> Downloading https://ghcr.io/v2/homebrew/core/pycparser/blobs/sha256:3171ff81
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/cffi/manifests/1.15.1
    ######################################################################### 100.0%
    ==> Fetching cffi
    ==> Downloading https://ghcr.io/v2/homebrew/core/cffi/blobs/sha256:3865305b34685
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/docutils/manifests/0.20.1-1
    ######################################################################### 100.0%
    ==> Fetching docutils
    ==> Downloading https://ghcr.io/v2/homebrew/core/docutils/blobs/sha256:510eb4b5a
    ######################################################################### 100.0%
    ==> Downloading https://ghcr.io/v2/homebrew/core/six/manifests/1.16.0_3
    ######################################################################### 100.0%
    ==> Fetching six
    ==> Downloading https://ghcr.io/v2/homebrew/core/six/blobs/sha256:0dee50367c6fac
    ######################################################################### 100.0%
    ==> Fetching awscli
    ==> Downloading https://ghcr.io/v2/homebrew/core/awscli/blobs/sha256:cd6ddb59898
    ######################################################################### 100.0%
    ==> Installing dependencies for awscli: pycparser, cffi, docutils and six
    ==> Installing awscli dependency: pycparser
    ==> Downloading https://ghcr.io/v2/homebrew/core/pycparser/manifests/2.21-1
    Already downloaded: $HOME/Library/Caches/Homebrew/downloads/ee6009519d741f590522d1ded090cfc31840cdb25ce7065cb5dbe485cc976aeb--pycparser-2.21-1.bottle_manifest.json
    ==> Pouring pycparser--2.21.ventura.bottle.1.tar.gz
    🍺  /usr/local/Cellar/pycparser/2.21: 50 files, 659.9KB
    ==> Installing awscli dependency: cffi
    ==> Downloading https://ghcr.io/v2/homebrew/core/cffi/manifests/1.15.1
    Already downloaded: $HOME/Library/Caches/Homebrew/downloads/7905e805664882089e0559ec93f8ba42193a86ceca50c509f59c93f3ed3bff7e--cffi-1.15.1.bottle_manifest.json
    ==> Pouring cffi--1.15.1.ventura.bottle.tar.gz
    🍺  /usr/local/Cellar/cffi/1.15.1: 33 files, 581.6KB
    ==> Installing awscli dependency: docutils
    ==> Downloading https://ghcr.io/v2/homebrew/core/docutils/manifests/0.20.1-1
    Already downloaded: $HOME/Library/Caches/Homebrew/downloads/4e1808204826d49b64005e73f77101af52c0113bfc10f001c2f7a9bbe52b93d9--docutils-0.20.1-1.bottle_manifest.json
    ==> Pouring docutils--0.20.1.ventura.bottle.1.tar.gz
    🍺  /usr/local/Cellar/docutils/0.20.1: 235 files, 2MB
    ==> Installing awscli dependency: six
    ==> Downloading https://ghcr.io/v2/homebrew/core/six/manifests/1.16.0_3
    Already downloaded: $HOME/Library/Caches/Homebrew/downloads/fa1a51f086a0aebe6dca89de7ed2eed5256badfcd82cfcea3e58164c812817e3--six-1.16.0_3.bottle_manifest.json
    ==> Pouring six--1.16.0_3.all.bottle.tar.gz
    🍺  /usr/local/Cellar/six/1.16.0_3: 20 files, 122.3KB
    ==> Installing awscli
    ==> Pouring awscli--2.13.22.ventura.bottle.tar.gz
    ==> Caveats
    The "examples" directory has been installed to:
      /usr/local/share/awscli/examples

    zsh completions and functions have been installed to:
      /usr/local/share/zsh/site-functions
    ==> Summary
    🍺  /usr/local/Cellar/awscli/2.13.22: 13,079 files, 111.2MB
    ==> Running `brew cleanup awscli`...
    Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
    Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
    ==> Caveats
    ==> awscli
    The "examples" directory has been installed to:
      /usr/local/share/awscli/examples

    zsh completions and functions have been installed to:
      /usr/local/share/zsh/site-functions
    ```

### 設定ファイルと認証情報ファイルの設定

??? info "aws configure"

    ```bash
    AWS Access Key ID [None]: localhogehogeid
    AWS Secret Access Key [None]: localhogehogepw
    Default region name [None]: us-west-2
    Default output format [None]: json
    ```

??? info "cat ~/.aws/config"

    ```bash
    [default]
    region = us-west-2
    output = json
    ```

??? info "cat ~/.aws/credentials "

    ```bash
    [default]
    aws_access_key_id = localhogehogeid
    aws_secret_access_key = localhogehogepw
    ```
