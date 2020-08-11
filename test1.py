class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None


li = SLinkedList()
li.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# 连接第一第二个节点
li.headval.nextval = e2

# 连接第二第三个节点
e2.nextval = e3

print(e2.nextval)
# 结果为e3内存地址<__main__.Node object at 0x0000001A0F9644BE0>
print(e2.nextval.dataval)
# 结果为e3所代表的值Wed

print(li.headval.dataval, li.headval.nextval.dataval, (li.headval.nextval.nextval).dataval)

a_list = ['a', 'b', 'x', 'a', 'a', 'b', 'z']
counter_dict = {}
for element in a_list:
    if element not in counter_dict:
        counter_dict[element] = 1
    else:
        counter_dict[element] += 1

key_values = [('even',2),('odd',1),('even',8),('odd',3),('float',2.4),('odd',7)]

multi_dict = {}
for key,value in key_values:
    if key not in multi_dict:
        multi_dict[key] = [value]
    else:
        multi_dict[key].append(value)