#!/usr/bin/python
# -*- coding: UTF-8 -*-
import functools

from functools import reduce

def f(x):
	return x*x;

r=map(f,[1,2,3,4,5,6,7,8,9]);

print(list(r));

# map高阶函数的作用，map对于一个列表起作用
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])));

def add(x, y):
	 return x + y;

print(reduce(add,[1, 3, 5, 7, 9]));

# filter函数，根据函数返回的true或false进行筛选
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# sort也是一个高阶函数，比如下面按绝对值排序
sorted([36, 5, -12, 9, -21], key=abs)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

# 求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(lazy_sum(1,2,3));

# 匿名函数
f = lambda x: x * x;
print(f(5));

# 装饰器
def now():
	print('2018-03-10')
f = now;

print(f);

now.__name__='now';
f._name_

import functools

#
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')


# 偏函数
def int2(x, base=2):
    return int(x, base);
int2 = functools.partial(int, base=2)