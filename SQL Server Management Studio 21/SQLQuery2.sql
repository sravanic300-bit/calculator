create database employees;
use employees;
create table employees(
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(10),
    age INT,
    department VARCHAR(50),
    designation VARCHAR(50),
    salary DECIMAL(10,2),
    email VARCHAR(100),
    phone VARCHAR(15),
    city VARCHAR(50),
    state VARCHAR(50),
    joining_date DATE,
    experience_years INT,
    status VARCHAR(20)
);
INSERT INTO employees VALUES
(101, 'Ravi', 'Kumar', 'Male', 28, 'IT', 'Software Engineer', 55000, 'ravi@gmail.com', '9876543210', 'Hyderabad', 'Telangana', '2022-06-15', 3, 'Active'),

(102, 'Anita', 'Sharma', 'Female', 32, 'HR', 'HR Manager', 65000, 'anita@gmail.com', '9876501234', 'Bangalore', 'Karnataka', '2020-04-10', 7, 'Active'),

(103, 'Suresh', 'Reddy', 'Male', 26, 'Finance', 'Accountant', 42000, 'suresh@gmail.com', '9123456780', 'Chennai', 'Tamil Nadu', '2023-01-05', 2, 'Active'),

(104, 'Priya', 'Singh', 'Female', 29, 'Marketing', 'Digital Marketer', 48000, 'priya@gmail.com', '9988776655', 'Delhi', 'Delhi', '2021-09-20', 4, 'Active'),

(105, 'Arjun', 'Mehta', 'Male', 35, 'Sales', 72000, 'arjun@gmail.com', '9001122334', 'Mumbai', 'Maharashtra', '2018-03-12', 10, 'Inactive'),

(106, 'Kavya', 'Nair', 'Female', 27, 'IT',  60000, 'kavya@gmail.com', '9012345678', 'Kochi', 'Kerala', '2022-11-01', 3, 'Active');

select emp_id,gender,age from students where emp_id 
IN(101,102,103)
AND gender IN('male','female','male')
AND age IN(28,32,26);

update employees set first_name='sravani',last_name='chowdam'where emp_id=101;
select*from employees;
drop table employees;
select count(*) as distinctcount from(select distinct status from employees) as tempp;
select *from employees order by age;
select*from employees  where not city='hyderabad';
select*from employees where age not between 27 and 29;
