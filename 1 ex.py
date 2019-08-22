a = list(map(int,input('Enter numbers with a space ').split()))
a.sort(reverse=True)
print(a)
print("the largest numder is ", a[0], "; the smallest number is ", a[-1], "; length of the largest number is ", len(str(a[0])), "; length of the smallest number is ", len(str(a[-1])))
