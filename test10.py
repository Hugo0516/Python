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

# 注意 用法
print(dict_1['A'])
print(dict_1.get('A'))

graph_1 = [[]] * 5
print(graph_1)

graph_2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
print(graph_2)
print(graph_2[2])

graph_2[2].append(99)
print(graph_2[2][2])

graph_3 = [[], []]
graph_3[0].append(1)
print(graph_3)
graph_3[1].append(0)
print(graph_3)