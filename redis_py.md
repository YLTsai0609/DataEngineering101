# Redis

[Introduction to Redis](https://redis.io/docs/about/)

* in nemory data structure store 
  * strings/hashes/list/set/sorted sets
  * counting - bitmaps, hyperloglogs, geospatial indexes
* cache
  * LRU
  * on-disk persistence
* message broker
* streaming engine

* HA(high avaliability) with redis cluster


* `redis-cli`
* [`python client`](https://github.com/redis/redis-py)

## Getting Start

[Install Redis on macOS](https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/)

`brew install redis`

* maybe install at `/opt/homebrew/opt/redis/bin/redis-server /opt/homebrew/etc/redis.conf`

`which redis-server`

`which redis-cli`

`brew services start redis` - start service

`ps aux | ag 6379` - check service is running

`redis-cli` - check in to the database

or using python client : `python redis_py/redis_cache.py`

## Redis 16 db

[Redis 爲什麼要分 16 個庫](https://www.readfog.com/a/1636087731802181632)

* single machine : `db0` ~ `db15`
* cluster : only `db0`

* different - `db` (like different tables)
  * `redis/redis.conf` - databases 16 (可設定數量)
  * 不能設定不同 db 的密碼
  * flushall - 全數清空


# Redis-cli

command|means|note
-----|-----|-----
KEYS *|show all the keys||
KEYS N*|pattern match N*||
SELECT 15|select db no 15||
redis-cli FLUSHALL|flush all data cross redisdatabase||
redis-cli FLUSHDB|flush all data in specified redisdatabase||