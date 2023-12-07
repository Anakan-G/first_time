def mergeSort(lst):
    if len(lst) > 1:
        center = len(lst)//2
        listOne = lst[:center]
        listTwo = lst[center:]
        mergeSort(listOne)
        mergeSort(listTwo)



list = [1,2,3,4]
mergeSort(list)