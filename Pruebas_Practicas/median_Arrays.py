nums1 = [1,2]
nums2 = [3,4]
equal = (nums1 + nums2)
equal.sort()
if len(equal) % 2 == 0:
    x1 = len(equal) / 2
    x2 = (len(equal) / 2) + 1
    op = float(x1 + x2 / 2)
    median = float((equal[x1] + equal[x2]) / 2)
    print(op)
else:
    median = len(equal) / 2
    print(equal[median])