'''
Viết hàm kiểm tra số nguyên tố
Nhập vào số nguyên bất kỳ
Trả về True nếu đó là số nguyên tố, ngược lại trả về False
'''
# Lấy dữ liệu
def nhap_so_n():
    n = int(input('Nhập vào số n bất kỳ: '))
    return n


# Kiểm tra số nguyên tố
def so_nguyen_to(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1  # count = count + 1
    if count == 2:
        return True
    return False


# In ra kết quả
if __name__ == "__main__":
    n = nhap_so_n()

    if so_nguyen_to(n)==True :
        print(f'{n} là số nguyên tố')
    else:
        print(f'{n} không là số nguyên tố')

