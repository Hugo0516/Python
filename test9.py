movieList = ["The Shape of Water", "Moonlight", "Superman", "Birdman", "Argo", "Spotlight"]

tag = ["39.jpg", "22.jpg", "192.jpg", "10.jpg", "4.jpg"]
movieList.sort(key=len)
print(movieList)

print(movieList[0][:-2])

print(tag[0][:-4])
tag.sort(key=lambda x: int(x[:-4]))
print(tag)
# print(sorted(tag, key=lambda x: int(x[:-4])))


a = [1, 2, 6, 3, 4, 5]
b = [2, 4, 3, 1, 0]


def findMissing(a, b):
    m = len(a)
    n = len(b)

    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                break

            if (j == n - 1):
                print(a[i], end=' ')


findMissing(a, b)
print("")

def findMissing2(a, b):
    for index in a:
        if index in b:
            pass
        else:
           print(index, end=' ')

findMissing2(a, b)