#!env python
#coding=utf-8
# Author:  joshua_zero@outlook.com

import redis as rds

class redis_op:
    
    def __init__(self):
        self._redis = rds.Redis(host="localhost", port=2020, db=0)
    
    def set_data(self, k, value):
        return self._redis.set(k, value)

    def get_data(self, k):
        return self._redis(k)


if __name__ == "__main__":
    rds_op = redis_op()
    f = rds_op.set_data('foo','bar')
    print(f)
    val = rds_op.get_data('foo')
    print(val)
