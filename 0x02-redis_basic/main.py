#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()




s1 = cache.store("foo")
print(s1)
s2 = cache.store("bar")
print(s2)
s3 = cache.store("42")
print(s3)

replay(cache.store)
print('Cache.store was called {} times'.format(call_count)

      
#inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
#outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

#print("inputs: {}".format(inputs))
#print("outputs: {}".format(outputs))
