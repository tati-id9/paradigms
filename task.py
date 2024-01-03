def search_recursive(req, lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == req:
            return middle
        elif lst[middle] > req:
            right = middle - 1
        else:
            left = middle + 1
    else:
        return '-1'
    

init_lst = list(i for i in range(1,16))
n = int(input("введите значение для поиска "))
print(init_lst)
print(search_recursive(n, init_lst))