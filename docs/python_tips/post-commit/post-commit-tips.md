# post-commit

[git hooks](https://git-scm.com/book/ja/v2/Git-%E3%81%AE%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%82%A4%E3%82%BA-Git-%E3%83%95%E3%83%83%E3%82%AF)の一機能ですが、スクリプトととしてPythonコードも実行できます。

[Topに戻る](../../index.md)

### 実例

[【Pythonバージョン管理】git hookを使用してコミットをトリガーにpyproject.tomlとgit tagを更新するスクリプトについて](https://7rikazhexde-techlog.hatenablog.com/entry/2023/06/10/005231)

#### コード

##### create_post-commit.sh

```bash
git clone https://gist.github.com/7rikazhexde/89036d5fc849411b925e6da7d4986b52
```

<script src="https://gist.github.com/7rikazhexde/89036d5fc849411b925e6da7d4986b52.js"></script>

##### post-commit

create_post-commit.shを実行することで作成できます。

```bash
git clone https://gist.github.com/7rikazhexde/6ada2a6ef3ca23938bfa62f32e3fbed8
```

<script src="https://gist.github.com/7rikazhexde/3d786d926fcb19edd807ebb6e9c96df1.js"></script>
