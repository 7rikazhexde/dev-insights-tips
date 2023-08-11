# post-commit tips

post-commit hook is a git hooks function that runs when "**all commits complete**".

git hooks is a hook function that launches custom scripts. (See [the official documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) for details.)

### Example(Japanese)

The following article presents python code to create a post-commit shell script.

[【Pythonバージョン管理】git hookを使用してコミットをトリガーにpyproject.tomlとgit tagを更新するスクリプトについて](https://7rikazhexde-techlog.hatenablog.com/entry/2023/06/10/005231)

#### Code

##### create_post-commit.sh

```bash
git clone https://gist.github.com/7rikazhexde/89036d5fc849411b925e6da7d4986b52
```

<script src="https://gist.github.com/7rikazhexde/89036d5fc849411b925e6da7d4986b52.js"></script>

##### post-commit

It can be created by running `create_post-commit.sh`.

```bash
git clone https://gist.github.com/7rikazhexde/6ada2a6ef3ca23938bfa62f32e3fbed8
```

<script src="https://gist.github.com/7rikazhexde/3d786d926fcb19edd807ebb6e9c96df1.js"></script>
