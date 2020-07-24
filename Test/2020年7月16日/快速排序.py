def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left<right and li[right] >= tmp:  # 从右面找比tmp小的数
            right -= 1 # 往左走一步
        li[left] = li[right]

        while left<right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp


li = [3, 4, 2, 1, 5, 6, 8, 7, 9]
print(li)
partition(li, 0, len(li)-1)
print(li)
