'''
Cho các dự báo thời tiết cho 30 ngày
Nhập thông tin thứ - ngày/tháng/năm của hôm nay
Yêu cầu chương trình đưa ra dự báo của n ngày tiếp theo 
'''
import os

thu_trong_tuan = ['Monday', 'Tuesday', 'Wednesday',
                  'Thursday', 'Friday', 'Saturday', 'Sunday']
so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Lấy toàn bộ dữ liệu từ file
def file_read(path):
    # Kiểm tra có tồn tại file
    if os.path.exists(path) == False:
        raise Exception('File {} khong ton tai'.format(path))

    file = open(path, 'r')
    data = file.read()
    file.close()

    return data


# Chuyển dubaothoitiet sang dạng dict
def du_bao_thoi_tiet_parse(data):
    # Chia dữ liệu theo dòng
    lines = data.split('\n')

    # Nếu có dòng trong ô cuối thì xoá
    if lines[-1] == '':
        lines.pop(-1)

    # Với mỗi dòng chia thành 2 phần 'ngay/thang/nam' và 'kyhieu'
    for i in range(len(lines)):
        lines[i] = lines[i].split(':')

    # Tạo và trả về một dict có dạng 'ngay/thang/nam' = 'kyhieu'
    result = dict()
    for ntn, kh in lines:
        result[ntn] = kh

    return result


def ky_hieu_parse(data):
    lines = data.split('\n')
    if lines[-1] == '':
        lines.pop(-1)

    # Với mỗi dòng chia thành 2 phần 'kyhieu' và 'thoitiet'
    for i in range(len(lines)):
        lines[i] = lines[i].split(': ')
    result = dict()
    for kh, tt in lines:
        result[kh] = tt

    return result


# Hàm kiểm tra năm nhuận
def check_leap_year(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))


# Lấy ngày tiếp theo, dạng 'thu' - 'ngay/thang/nam'
def next_day(thu, ntn):
    ngay, thang, nam = map(int, ntn.split('/'))

    ngay += 1

    if ngay >= so_ngay_trong_thang[thang - 1] + (1 if thang == 2 and check_leap_year == True else 0):
        ngay = 1
        thang += 1

    if thang >= 12:
        thang = 1
        nam += 1

    ntn = '{}/{}/{}'.format(ngay, thang, nam)

    thu_idx = thu_trong_tuan.index(thu)
    thu_idx = (thu_idx + 1) % 7

    thu = thu_trong_tuan[thu_idx]

    return thu, ntn


# Lấy input
def get_input():
    print('Today: ', end= '')
    inp = input()
    thu, ntn = [i.strip() for i in inp.split('-')]

    print('n = ', end= '')
    n = int(input())
    return thu, ntn, n


# In ra output
def print_output(thu, ntn, n, dbtt_dict, kh_dict):
    print('weather forecast for {} day:'.format(n))

    for i in range(n):
        thu, ntn = next_day(thu, ntn)

        # Kiểm tra có tồn tại ngay/thang/nam trong file dubaothoitiet, nếu có trả về kyhieu
        kh = dbtt_dict[ntn] if ntn in dbtt_dict else False

        # Kiểm tra ký hiệu khác False và ký hiệu có năm trong file ký hiệu, nếu có trả về thời tiết, ngược lại 'Chưa có thông tin' 
        tt = False if kh == False else kh
        tt = kh_dict[kh] if kh in kh_dict else 'Chưa có thông tin'

        print('{} - {}: {}'.format(thu, ntn, tt))


print("Vi du:\n Today: Wednesday - 11/9/2022")
print(" n = 2 ")
print("weather forecast for 2 day: ")
print("thursday - 12/9/2022: fog")
print("friday - 13/9/2022: sunny")

dbtt_data = file_read('dubaothoitiet.txt')
dbtt_dict = du_bao_thoi_tiet_parse(dbtt_data)

kh_data = file_read('kyhieu.txt')
kh_dict = ky_hieu_parse(kh_data)

thu, ntn, n = get_input()
print_output(thu, ntn, n, dbtt_dict, kh_dict)

