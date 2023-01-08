# Goal

1. recommendation
2. 
3. pyspark cosine-random projection implementation
4. pyspark build-in lsh logic

# Numpy 

[Cosine - Random Projection Implementation](https://github.com/YLTsai0609/cs246_mining_massive_datasets/blob/main/implementation/lsh/jaccard_and_cosine.ipynb)

# pyspark cosine-random projection LSH


## [cosine-lsh-join-spark star 160+
](https://github.com/soundcloud/cosine-lsh-join-spark)

1. scala(we can check the source code when we need)

## [pyspark-lsh star 20+](https://github.com/magsol/pyspark-lsh)

1. python
2. RDD-based
3. Jaccard only

## Conclusion

Well, almost pyspark implementation using RDD approach

Which is painful to debug.

Use it very carful.

https://github.com/search?q=pyspark++lsh


# Near-realtime recommendation

## [datasketch: Big Data Looks Small star 1.5k+](https://github.com/ekzhu/datasketch)

1. pure python
2. support redis
3. Jaccard
4. MinHash-LSH and MinHash Forest(sub-linear) (we can learn to write better from this)

Use this if you wanna server millions items.

## [SparseLSH star 120+](https://github.com/brandonrobertz/SparseLSH)

1. pure python
2. sparse matrix only
3. redis
4. support multiple distance
   1. hamming
   2. L1
   3. L2
   4. cosine

## [locality-sensitive-hashing star 2+](https://github.com/akdel/locality-sensitive-hashing)

1. pure python
2. numba support(we can learn to write better from this)
3. dense only

# pyspark build-in lsh logic

[check here](https://github.com/YLTsai0609/pyspark_101/blob/main/notebook/algo/lsh_built_in.ipynb)



# Deduplicates without encoing to numpy array

## [simhash, 800+ star](https://github.com/1e0ng/simhash)