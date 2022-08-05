# Why?

Join is the most important and foundemental operation in data processing.

Knowing how to perform join properly will make your query `possible` (the most important, especially in distributed environment) or `faster`

# Spark for example

https://github.com/YLTsai0609/paper101/blob/main/engineering/spark_join.md

1. shffule hash join.
2. broadcast hash join.
3. sort merge join.
4. broadcast nested loop join.

`shuffle`, `broadcast` are related to network transmission.


# Nested Loop Join

* just compare 2 tables.


$T_L : \{a, b, c\}$ l rows.

$T_R : \{a, c, d\}$ r rows.


```python
for l in tl:
    # a, b, c
    for r in tr:
        # a, c, d
        if l == r:
            # combine the data
```

tc : $O(lr)$

sc : $O(1)$

* no sorted need
* most naive way to perform join.

# Hash Join

* hash 1 tables (usually the small one to avoid OOM)
* compare 2 tables, since we already hash 1 table. it will be fast

```python

hashed = hash(tr)

for l in tl:
    if l in hashed:
        # perform combination
```

tc : O(R) (building hash table) + O(L) (comparing)
sc : O(R) (building hash table)

* no sorted needed.
* fast if we use it properly.

[ref](https://yuji.page/time-complexities-of-table-joins/)

# Sort Merge Join

sorted $T_L : \{a, b, c\}$ l rows.

sorted $T_R : \{a, c, d\}$ r rows.


[viz](https://bertwagner.com/posts/visualizing-merge-join-internals-and-understanding-their-implications/)

```python
if you wnat to write it down
https://hackernoon.com/python-and-data-engineering-under-the-hood-of-join-operators
```

tc : O(L) + O(R) (but sorted both) - genral strategy for spark and database(if two of them are indexed)

sc : O(1)

[overall tc](https://cs.stackexchange.com/questions/68113/time-complexity-of-sort-merge-join)