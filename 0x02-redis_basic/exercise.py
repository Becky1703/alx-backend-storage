#!/usr/bin/env python3
"""REdis Server"""
import uuid
import redis
from typing import Union


class Cache():
    """Class Cache represents an object for storing data in a redis storage"""
    def __init__(self) -> None:
        """Initializes a cache instance"""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Function stores a value in a Redis data storag and returns a key"""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
