# DynamoDB

ChatGPTによる引用(2023/10/14時点)

> Amazon DynamoDBは、AWSが提供するキーバリュー型のNoSQLデータベースです[^3][^4][^5]。  
>
> 主な特徴と利用方法
>
> - **AP型データベース**：DynamoDBは、可用性（Availability）とネットワーク分断耐性（Partition Tolerance）を重視したAP型データベースの代表例で、クラウド環境ならではの水平スケーラビリティに優れた特徴を持っています[^1]。
> - **キーバリュー型ストレージ**：DynamoDBは、「値」とそれを取得するための「キー」だけを格納するというシンプルな機能を持った「キーバリュー型」の形式でデータを格納します²。
> - **スキーマレス**：DynamoDBは、特に項目・属性の定義が必要ないスキーマレスのテーブル構造を持つ。 属性は項目ごとに異なっても問題ない[^1]。
> - **読み書き処理に関する結果整合性**：DynamoDBは、読み書き処理に関する結果整合性をオプションで選択できる。 処理の重要性に応じて使い分ける[^1]。
> - **固有の機能**：DynamoDBには、条件付き書き込み、DAX、DynamoDB Streamsといった固有の機能がある。 さまざまな処理で活用できるので、一通り内容を押さえておく[^1]。
>
> ただし、RDBで可能だった複雑な検索やテーブル結合などは実行できないため、代わりにインデックスを駆使したり、不足する機能に代替する処理をアプリケーションで実装したりする必要があります[^1]。

[^1]: DynamoDBの基本についてまとめてみた【初心者向け】｜カル .... <https://karukichi-blog.netlify.app/blogs/dynamodb-about>.
[^3]: AWS Dynamodbとは？3つのメリットと料金システムについて解説！. <https://tenshoku-careerchange.jp/column/1061/>.
[^4]: Amazon DynamoDBとは何かをわかりやすく図解、どう使う .... <https://www.sbbit.jp/article/cont1/95515>.
[^5]: 【初心者向け】Amazon DynamoDB について改めて整理してみ .... <https://zenn.dev/issy/articles/zenn-dynamodb-overview>.

## 使い方

### [DynamoDB-local](dynamodb-local.md)
