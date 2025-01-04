---
title: MongoDB
tags:
  - MongoDB
  - NoSQL
description:
---

MongoDB関連のtipsをまとめてます。

## MongoDB

ChatGPTによる引用(2023/10/14時点)

> MongoDBは、代表的なNoSQLデータベースで、ドキュメント指向型データベースの一つです。MongoDBはMongoDB社が開発し、オープンソースとして提供されています[^1][^2]。
>
> MongoDBの主な特徴は以下の通りです[^1]：
>
> - **インメモリで動作するため処理速度が速い**：データをメインメモリ（RAM）で読み込んでから処理するため、処理すべきデータ量が増えても、よりスピーディーにI/O処理を行える。
> - **負荷分散や冗長化を実現する仕組みがある**：データを複数のサーバーに分割して保存・処理できる「シャーディング」という機能を備えている。また、「レプリカセット」といって、3台以上のサーバーで常に同じデータを保存・管理する機能もある。
> - **外部システムとの連携が容易**：様々なシステムが採用する「JSON」に似た形式でデータを保存する。
> - **複雑な形式のデータを扱いやすい**：ドキュメント形式なので、動的かつ柔軟に扱うデータの形式を変えることもできる。
>
> ただし、MongoDBはデータの一貫性が重要なシステムでは、MongoDBは不向きです[^1]。

[^1]:【初心者向け】MongoDBとは？メリット・基本をわかりやすく解説 <https://www.kagoya.jp/howto/it-glossary/develop/mongodb/>
[^2]: MongoDBとは | MongoDB. <https://www.mongodb.com/ja-jp/what-is-mongodb>

## 使い方

### 基本操作

#### [MongoDBのinstall](./install-mongodb.md)

#### [mongoshの使い方](./mongosh.md)

#### [Python(pymongo)による操作例](./pymongo.md)

### GUIツール

[mongodb-compassの使い方](./mongodb-compass.md)
