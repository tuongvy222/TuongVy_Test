Công ty BĐS Maico Group có nhu cầu muốn lưu trữ thông tin về nhân viên, văn phòng và doanh số theo từng văn phòng. Các nhu cầu lưu trữ cần có như sau.

# Nhân viên
Họ Tên
Văn phòng
Mã nhân viên

# Văn phòng
Mã văn phòng
Tên văn phòng

# Giao dịch
phần trăm đóng góp trong phí môi giới của nhân sự của giao dịch.
Ngày giao dịch
Phí môi giới
Mã Văn phòng
Mã nhân viên

Tạo 3 table trong PostgreSQL với tên lần lượt: EmployeeTable (bảng nhân sự), BranchTable (bảng văn phòng), OrderTable (bảng đơn hàng) và insert dữ liệu có sẵn trong 3 file csv: employee_data.csv, branch_data.csv, order_data.csv bằng psycopg2. 

Tạo bảng mới từ dữ liệu các bảng trên với các nhu cầu lưu trữ sau:
Tên nhân sự
Tổng doanh số (doanh số trong mỗi giao dịch = phần trăm đóng góp * phí môi giới)/100
Tên văn phòng

Lọc ra các nhân sự có doanh số cao hơn 200000000.
