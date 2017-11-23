#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Created on    : 17/11/22 上午9:35
# @Author  : zpy
# @Software: PyCharm
import sys
sys.path.append("..")

from data_structre.stream import Stream

def integer_stream(first):
    return Stream(first, lambda : integer_stream(first+1))

def stream_to_list(stream):
    _list = []
    while stream is not None:
        _list.append(stream.first)
        stream = stream.rest
    return _list

def fib_stream(a, b):
    return Stream(a, lambda :fib_stream(b, a+b))

def filter_stream(fn, s):
    if s is None:
        return s
    compute_rest = lambda : filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    return compute_rest()

def map_stream(fn, s):
    if s is None:
        return s
    compute_rest = lambda : map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)

def list_to_stream(lst):
    s = Stream(lst[0])
    c = s
    for i in lst[1:]:
        c.second = lambda : Stream(i)
        c = c.rest
    # return stream_to_list(s)  for test
    return s


def primes(s):
    def not_div(x):
        return x % s.first != 0
    def compute_rest():
        return primes(filter_stream(not_div, s.rest))
    return Stream(s.first, compute_rest)

def first_k(k, s):
    res = []
    for i in range(k):
        if s is None:
            break
        res.append(s.first)
        s = s.rest
    return res


if __name__ == '__main__':
    s = list_to_stream(list(range(100)))
    f = filter_stream(lambda x: x%2, s)
    #print(stream_to_list(f))
    m = map_stream(lambda x:x*x, s)
    #print(stream_to_list(m))
    print(first_k(5, m))
    print(first_k(6, integer_stream(1)))
    print(first_k(5, primes(integer_stream(2))))
    # print(stream_to_list(f))
    #
    # f = fib_stream(0, 1)
    #
    # for i in range(10):
    #     print(f.first)
    #     f = f.rest
    #
    # print(stream_to_list(s))
    # print(list_to_stream(list(range(10))))