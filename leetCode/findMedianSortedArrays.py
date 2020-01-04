def findMedianSortedArrays(nums1, nums2) -> float:  #暴力法，归并排序的一部分
    len1 = len(nums1)
    len2 = len(nums2)

    len_total = len1 + len2

    mid_postion = len_total // 2
    k = 0
    i = 0
    j = 0
    temp = [0 for t in range(len_total)]
    while i < len1 and j < len2:
        if nums1[i] > nums2[j]:
            temp[k] = nums2[j]
            print(temp[k])
            j = j + 1
        else:
            temp[k] = nums1[i]
            print(temp[k])
            i = i + 1
        k = k + 1
    while i < len1:
        temp[k] = nums1[i]
        print(temp[k])
        i = i + 1
        k = k +1
    while j < len2:
        temp[k] = nums2[j]
        print(temp[k])
        j = j + 1
        k = k + 1
    if len_total % 2 == 0:
        mid_value = (temp[mid_postion] + temp[mid_postion - 1]) / 2
    else:
        mid_value = temp[mid_postion]
    return mid_value


a = [1, 2]
b = [3, 4]
print(findMedianSortedArrays(a, b))
