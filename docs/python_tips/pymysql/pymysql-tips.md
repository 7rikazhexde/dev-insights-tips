# pymysql-tips

pymysqlに関するTipsです。
主に、使い方をまとめてます。

[Topに戻る](../../index.md)

## Table of Contents

- [pymysql-tips](#pymysql-tips)
  - [Table of Contents](#table-of-contents)
  - [詳細とインストール](#%E8%A9%B3%E7%B4%B0%E3%81%A8%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  - [使い方](#%E4%BD%BF%E3%81%84%E6%96%B9)
    - [基本編](#%E5%9F%BA%E6%9C%AC%E7%B7%A8)
    - [事例](#%E4%BA%8B%E4%BE%8B)
      - [【MESH + Flask + MariaDB】温度・湿度タグから取得した温度情報をローカルWebサーバ経由でデータベースに追加する方法](#mesh--flask--mariadb%E6%B8%A9%E5%BA%A6%E6%B9%BF%E5%BA%A6%E3%82%BF%E3%82%B0%E3%81%8B%E3%82%89%E5%8F%96%E5%BE%97%E3%81%97%E3%81%9F%E6%B8%A9%E5%BA%A6%E6%83%85%E5%A0%B1%E3%82%92%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%ABweb%E3%82%B5%E3%83%BC%E3%83%90%E7%B5%8C%E7%94%B1%E3%81%A7%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%81%AB%E8%BF%BD%E5%8A%A0%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)
      - [GoogleSpreadSheetからDLしたCSVファイルをMariaDBにレコード一括追加(BULK INSERT)する](#googlespreadsheet%E3%81%8B%E3%82%89dl%E3%81%97%E3%81%9Fcsv%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92mariadb%E3%81%AB%E3%83%AC%E3%82%B3%E3%83%BC%E3%83%89%E4%B8%80%E6%8B%AC%E8%BF%BD%E5%8A%A0bulk-insert%E3%81%99%E3%82%8B)

## 詳細とインストール

下記参照

[https://pypi.org/project/pymysql/](https://pypi.org/project/pymysql/)

## 使い方

### 基本編

公式ドキュメント

[https://pymysql.readthedocs.io/en/latest/](https://pymysql.readthedocs.io/en/latest/)

参考記事: PythonでMySQLを操作する（PyMySQL）

[https://python-work.com/pymysql/](https://python-work.com/pymysql/)

### 事例

#### 【MESH + Flask + MariaDB】温度・湿度タグから取得した温度情報をローカルWebサーバ経由でデータベースに追加する方法

[https://qiita.com/7rikazhexde/items/ec8fc8f90acf45703d53](https://qiita.com/7rikazhexde/items/ec8fc8f90acf45703d53)

#### GoogleSpreadSheetからDLしたCSVファイルをMariaDBにレコード一括追加(BULK INSERT)する

コード取得したい場合は下記を実行してください。

```bash
git clone https://gist.github.com/ed55e9b55ac69742b8ed61d5ae06502c.git
```

<script src="https://gist.github.com/7rikazhexde/ed55e9b55ac69742b8ed61d5ae06502c.js"></script>
