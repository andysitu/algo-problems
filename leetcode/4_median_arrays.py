def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l1 = len(nums1)
    l2 = len(nums2)
    c = l1 + l2
    if c % 2 == 0:
        even_status = True
    else:
        even_status = False
    end = int(c/2) + 1
    prev = 0
    value = 0
    a = 0
    b = 0
    for i in range(end):
        prev = value
        if (a >= l1):
            value = nums2[b]
            b += 1
        elif (b >= l2):
            value = nums1[a]
            a += 1
        elif (nums1[a] > nums2[b]):
            value = nums2[b]
            b += 1
        else:
            value = nums1[a]
            a += 1
    if even_status:
        return (value + prev) / 2
    else:
        return value
                
        