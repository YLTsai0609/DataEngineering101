# Practical

[AmazingTalker 微服務化-快取服務](https://medium.com/amazingtalker-tech/amazingtalker-%E5%BE%AE%E6%9C%8D%E5%8B%99%E5%8C%96-%E5%BF%AB%E5%8F%96%E6%9C%8D%E5%8B%99-1f22f94b93ea)

[如何使用 Python 實現 LRU Cache 快取置換機制](https://blog.techbridge.cc/2019/04/06/how-to-use-python-implement-least-recently-used/)

[lru_cache is supported in python function tools](https://docs.python.org/3/library/functools.html)
# 衡量快取機制

1. latency - 快取就是要快，不然就沒意義，但可以比較的對象是從 database 拿，速度是幾倍 OR 和標準時間 (200ms) 比
2. hit rate - 一般來說快取做在熱門，因為命中率大


# 常見機制

1. FIFO(first in, first out)
2. LFU(Least Frequently Used) - 最常使用
3. LRU(Least Recently used) - 最近使用
4. NMRU(Not Most Recently Used) 