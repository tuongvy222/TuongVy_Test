'''
Viết hàm xuất ra màn hình một kim tự tháp 
Nhập vào số tầng, tầng dưới sẽ ít hơn tầng trên.
'''
# Nhập số tầng của kim tự tháp
def nhap_n():
    n = int(input("Nhập số tầng n: "))
    while(n <= 0):
        n = int(input("Nhập lại n: "))
    return n


# Dựng kim tự tháp
def kim_tu_thap(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(2*i - 1):
            print("*", end="")
        print()


# In kim tự tháp
if __name__ == "__main__":
    n = nhap_n()
    kim_tu_thap(n)

