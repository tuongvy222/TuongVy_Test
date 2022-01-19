'''
Viết hàm tìm BCNN(a,b) (a,b nguyên dương)
Công thức: a * b = UCLN(a,b) * BCNN(a,b)
'''
a = int(input("Nhập số dương a: "))
while(a <= 0):
    a = int(input("Nhập lại số dương a: "))
b = int(input("Nhập số dương b: "))
while(b <= 0):
    b = int(input("Nhập lại số dương b: "))


ucln = 1
for i in range(min(a,b), 0, -1):
    if(a % i == 0 and b % i == 0):
        ucln = i
        break


print("BCNN của",a, "và",b, "là:", int(a*b/ucln))

