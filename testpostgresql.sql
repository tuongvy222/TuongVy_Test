--Tạo bảng branch_table và insert branch_data.csv
CREATE TABLE branch_table(
	branch_id INT PRIMARY KEY,
	name VARCHAR(10)
);
COPY public.branch_table
FROM 'branch_data.csv'
DELIMITER ','
CSV HEADER;

--Tạo bảng employee_table và insert employee_data.csv
CREATE TABLE employee_table(
	id INT PRIMARY KEY,
	employee_name VARCHAR(30),
	branch VARCHAR(10)
);
COPY public.employee_table
FROM 'employee_data.csv'
DELIMITER ','
CSV HEADER;

--Tạo bảng order_table và insert order_data.csv
CREATE TABLE order_table(
	percent_contribute DECIMAL(5,2),
	brokerage_fee INT,
	created_at TIMESTAMP,
	branch_id INT REFERENCES branch_table,
	employee_id INT REFERENCES employee_table(id)
);
COPY public.order_table
FROM 'order_data.csv'
DELIMITER ','
CSV HEADER;

--Truy vấn dữ liệu
--Tạo bảng gồm: tên nhân viên, tổng doanh số, tên văn phòng
SELECT E.employee_name, ROUND(SUM(O.percent_contribute*O.brokerage_fee/100)) total_sales, E.branch
FROM employee_table E INNER JOIN order_table O
	ON E.id = O.employee_id
GROUP BY E.employee_name, E.branch

--Tạo bảng lọc ra nhân viên có doanh số >200000000
SELECT E.employee_name, ROUND(SUM(O.percent_contribute*O.brokerage_fee/100)) total_sales
FROM employee_table E INNER JOIN order_table O
	ON E.id = O.employee_id
GROUP BY E.employee_name
HAVING ROUND(SUM(O.percent_contribute*O.brokerage_fee/100)) > 200000000
