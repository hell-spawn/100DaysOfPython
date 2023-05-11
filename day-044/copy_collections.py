# Deep Copy
import copy

mutable = [1, 1, 2, 3, 5, 8]
immutable = (5, 8, 13, 21)

mutable_b = mutable
immutable_b = immutable

print(mutable is mutable_b)
print(immutable is immutable_b)


mutable += [mutable[-2] + mutable[-1]]
immutable += (immutable[-2] + immutable[-1],)

print(mutable)
print(mutable_b)
print(immutable)
print(immutable_b)

some_dict = {'a': [1, 1, 2, 3]}
another_dict = some_dict.copy()

print(some_dict)
print(another_dict)

some_dict['a'].append(5)

print(another_dict)

print(id(some_dict['a']))
print( id(some_dict['a']) == id(another_dict['a']) )

some_list = [[2, 3, 5], [7, 11, 13]]
another_list = some_list.copy()
print(some_list is another_list) #False
print(some_list[0] is another_list[0]) #True


some_dict = {'a': [1, 1, 2, 3]}
another_dict = copy.deepcopy(some_dict)

some_dict['a'].append(5)

print(some_dict) #{'a': [1, 1, 2, 3, 5]}
print(another_dict) #{'a': [1, 1, 2, 3]}
