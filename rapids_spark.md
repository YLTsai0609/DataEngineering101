# RAPIDS

1. Gpu data science!
2. [home](https://rapids.ai/index.html) [github](https://github.com/rapidsai)
3. Intergretion the dataframe and gpu(cudf), mllib(cuml), graph analytics(cugraph) and so on 
4. Might be unstable,          `0.1.x`
5. provide python api

# RAPIDS + Spark

NVIDIA is bring RAPIDS to Apache Spark to accelerate ETL workflows with GPUs

1. Spark 3.0
2. According to nvidia, you might save your money(gpus more than cpus and VMs)
3. [home](https://www.nvidia.com/en-us/deep-learning-ai/solutions/data-science/apache-spark-3/) [github](https://github.com/NVIDIA/spark-rapids)
4. open source!
5. might be unstable `0.2.x`, (Apr 28, 2019 – Dec 10, 2020)
6. LACK OF DOCUMENTATION
7. Example just start, [Jun 2019 - Now, star 25+](https://github.com/NVIDIA/spark-xgboost-examples)

# RAPIDS + dask

1. friendly python api (shorter and easier compare between dask and spark)
2. training is extremely faster! (experiements case is random-forest)
3. [the case study spark cpu vs dask rapids 2020 Jul](https://towardsdatascience.com/random-forest-on-gpus-2000x-faster-than-apache-spark-9561f13b00ae)

4. we can use [cudf library](https://github.com/rapidsai/cudf) to combine dask rapids
