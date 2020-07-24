def insert_sort(li):
    for i in range(1, len(li)):  # i 表示摸到的牌的下标
        tmp = li[i]
        j = i - 1  # j指的是手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
        print(li)


li = [3, 4, 2, 1, 5, 6, 8, 7, 9]

insert_sort(li)
print(li)

print('-----------------')

def insert_sort(li):
    for i in range(1, len(li)):  # i 表示摸到的牌的下标
        while i > 0 and li[i-1] > li[i]:
            li[i-1],li[i] = li[i],li[i-1]
            i -= 1
        print(li)

li = [3, 4, 2, 1, 5, 6, 8, 7, 9]

insert_sort(li)
print(li)



