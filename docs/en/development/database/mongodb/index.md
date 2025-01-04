---
title: MongoDB
tags:
  - MongoDB
  - NoSQL
description:
---

## MongoDB

Quote by ChatGPT (as of 10/14/2023).

> MongoDB is a typical NoSQL database and one of the document-oriented databases.MongoDB is developed by MongoDB Inc. and is available as open source[^1][^2].
>
> The main features of MongoDB are as follows[^1]:
>
> - **Faster processing speed because it operates in-memory**: Data is read in main memory (RAM) before processing, so I/O processing can be performed more quickly even if the amount of data to be processed increases.
> - **A system for load balancing and redundancy**: It has a function called "sharding" that allows data to be divided into multiple servers for storage and processing. There is also a "replica set" function that allows three or more servers to always store and manage the same data.
> - **Easy integration with external systems**: Data is stored in a format similar to "JSON," which is adopted by various systems.
> - **Easy to handle data in complex formats**: Because it is a document format, it is also possible to dynamically and flexibly change the format of the data to be handled.
>
> However, MongoDB is not suitable for systems where data consistency is important[^1].

[^1]: What is [for beginners] MongoDB? Benefits and basics explained in an easy-to-understand manner <https://www.kagoya.jp/howto/it-glossary/develop/mongodb/>
[^2]: What is MongoDB | MongoDB. <https://www.mongodb.com/ja-jp/what-is-mongodb>

## Usage

### Basic Operation

#### [MongoDB install](./install-mongodb.md)

#### [How to use mongosh](./mongosh.md)

#### [Example of operation by Python(pymongo)](./pymongo.md)

### GUI Tools

[How to use mongodb-compass](./mongodb-compass.md)
