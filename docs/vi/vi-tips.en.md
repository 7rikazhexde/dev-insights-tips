# vi tips

This section summarizes information related to vi.

## Reference(Japanese)

### viエディタ入門

[https://vim.jp.net/](https://vim.jp.net/)

### viコマンド（vimコマンド）リファレンス

[https://qiita.com/pe-ta/items/0510bee10bcfd88afeee](https://qiita.com/pe-ta/items/0510bee10bcfd88afeee)

## Usage

### Manipulate windows

#### Split horizontally

```bash
:sp
```

#### file editing

```bash
:E
```

#### window switching

```bash
[Ctrl] + [w]
```

In Windows, use ↑, ↓ to switch

### file handling

#### Start typing from the left of the cursor

```bash
i
```

#### Stop the previous operation (u: meaning Undo)

```bash
u
```

#### Exit without writing (meaning quit)

```bash
:q
```

#### Forced termination without writing

```bash
q!
```

#### End after writing

```bash
:wq
```

#### Forced termination after writing

```bash
:wq!
```

### character cursor movement

#### Move to first line

```bash
[g] + [g]
```

or

```bash
[1] + [G](shift + g)
```

#### Moved to the end

```bash
[G](shift + g)
```

#### Go to next word

```bash
w
```

#### Move forward one word

```bash
b
```

#### To end of word

```bash
e
```
