# vi tips

vi関連のtipsをまとめてます。

## 参考

### viエディタ入門

[https://vim.jp.net/](https://vim.jp.net/)

### viコマンド（vimコマンド）リファレンス

[https://qiita.com/pe-ta/items/0510bee10bcfd88afeee](https://qiita.com/pe-ta/items/0510bee10bcfd88afeee)

## 使い方

### ウインドウ操作

#### 横に分割

```bash
:sp
```

#### ファイル編集

```bash
:E
```

#### ウインドウ切り替え

```bash
[Ctrl] + [w]
```

Windowsの場合は↑,↓で切り替え

### ファイル操作

#### カーソルの左から入力開始

```bash
i
```

#### 直前の操作をやめる(u: Undo の意味)

```bash
u
```

#### 書込みを行わず終了(quit の意味)

```bash
:q
```

#### 書込みを行わず強制終了する

```bash
q!
```

#### 書込み後終了

```bash
:wq
```

#### 書込み後強制終了

```bash
:wq!
```

### 文字カーソル移動

#### 先頭行へ移動

```bash
[g] + [g]
```

or

```bash
[1] + [G](shift + g)
```

#### 末尾に移動

```bash
[G](shift + g)
```

#### 1語次へ移動

```bash
w
```

#### 1語前へ移動

```bash
b
```

#### 単語末尾へ

```bash
e
```
