#!/usr/bin/env python3
"""REdis Server"""
import uuid
import redis
from functools import wraps
from typing import Union, Callable, Any


def count_calls(method: Callable) -> Callable:
    """Function tracks the number of calls made to a method
    in the Cache class"""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """method to invoke the given method after incrementing"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker

def call_history(method: Callable) -> Callable:
    """Function tracks the call details of a method in a cache class"""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Function eturns methods's output after storing its inputs and
        outputs"""
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key ='{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


class Cache():
    """Class Cache represents an object for storing data in a redis storage"""
    def __init__(self) -> None:
        """Initializes a cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Function stores a value in a Redis data storag and returns a key"""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Function retrieves a value from a Redis data storage"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """Function retrieves a string value from a Redis data storage"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Functioon retrieves an integer value from a Redis data storage"""
        return self.get(key, lambda x: int(x))
