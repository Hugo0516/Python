import collections

list = ['a', 'b', 'c', 'd']

dd = ''.join(list)
print(type(dd))
print(dd)

dict_1 = {'A': 'apple', 'B': 'banana', 'C': 'celcius'}

print(dict_1.values())

S = "ADOBECODEBANC"
a = collections.Counter(S)
print(collections.Counter(S), type(a))

s2 = "ADOBECODEBANC"
for i in s2:
    print(type(i), i)