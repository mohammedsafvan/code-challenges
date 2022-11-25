num = 1234567890
arr = [x for x in str(num)]
ouput = ""
arr = sorted(arr, reverse=True)
for i in arr:
    ouput +=i
a = int(ouput)  