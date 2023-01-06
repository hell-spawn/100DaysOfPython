"""
Useful libs functools
"""

import time
import functools
import sys
"""
Exercise 98: Creating a print Function That Writes to stderr
"""

print("Hello stderr", file=sys.stderr)

print_stderr = functools.partial(print, file=sys.stderr)
print_stderr("Hello stderr")

"""
Exercise 97: Using lru_cache to Speed Up Our Code
"""

# Original version
#def func(x):
#    time.sleep(3)
#    print(f"Heavy aperation for {x}")
#    return x *10
#
#print("Func returned", func(1))
#print("Func returned", func(1))


# @functools.lru_cache() # Change the cache size with a default size is 128 Change with maxsize parameter 
@functools.lru_cache(maxsize=2)
def func1(x):
    time.sleep(3)
    print(f"Heavy aperation for {x}")
    return x *10

#print("Func returned:", func(1))
#print("Func returned:", func(2))
#print("Func returned:", func(3))
#print("Func returned:", func(3))
#print("Func returned:", func(2))
#print("Func returned:", func(1))


def func2(x):
    time.sleep(3)
    print(f"Heavy aperation for {x}")
    return x *10
    
cached_func = functools.lru_cache()(func2)

#print("Cached func returned:", cached_func(1))
#print("Cached func returned:", cached_func(1))
#print("Func returned:", func(1))
#print("Func returned:", func(1))


