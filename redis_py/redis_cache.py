"""
1. onstall on your os (or use GCP/AWS solution) - https://redis.io/docs/getting-started/installation/install-redis-on-mac-os/
2. install redis-cli or python client
brew install redis
"""
import redis

r = redis.Redis(host="localhost", port=6379, db=0)
r.set("foo", "bar")  # return True
print(redis.__version__)
print(r.get("foo"))  # get b'bar'
print(dir(r))
