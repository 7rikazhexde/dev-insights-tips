# DynamoDB

Quote from ChatGPT (as of 10/14/2023).

> Amazon DynamoDB is a key-value NoSQL database provided by AWS [^3][^4][^5].  
>
> Key Features and Usage.
>
> - **AP-type database**: DynamoDB is a typical example of an AP-type database that emphasizes availability (Availability) and network fragmentation tolerance (Partition Tolerance), and has excellent horizontal scalability features unique to cloud environments[^ 1].
> - **Key-value type storage**: DynamoDB stores data in a "key-value type" format with the simple feature of storing only "values" and "keys" for retrieving them².
> - **Schemaless**: DynamoDB has a schema-less table structure that does not require any particular item or attribute definition. Attributes can be different for each item [^1].
> - **Result consistency regarding read/write processing**: DynamoDB allows optional result consistency regarding read/write processing. Use it according to the importance of the process[^1].
> - **Unique Features**: DynamoDB has unique features such as conditional writes, DAX, and DynamoDB Streams. Since they can be utilized in a variety of processes, keep the contents in mind[^1].
>
> However, complex searches and table joins that were possible with RDB cannot be performed, so you must instead make full use of indexes or implement alternative processing in your application to replace the missing functions [^1].

[^1]: Summary of DynamoDB basics [for beginners] | Cal .... <https://karukichi-blog.netlify.app/blogs/dynamodb-about>.
[^3]: What is AWS Dynamodb, 3 benefits and pricing system explained! <https://tenshoku-careerchange.jp/column/1061/>.
[^4]: What is Amazon DynamoDB, illustrated in an easy-to-understand way, and how to use it .... <https://www.sbbit.jp/article/cont1/95515>.
[^5]: [For beginners] Let's reorganize about Amazon DynamoDB .... <https://zenn.dev/issy/articles/zenn-dynamodb-overview>.

## Usage

### [DynamoDB-local](dynamodb-local.md)
