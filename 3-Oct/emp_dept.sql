CREATE TABLE departments ( dept_id INT PRIMARY KEY, dept_name VARCHAR(100) );
CREATE TABLE employees ( emp_id INT PRIMARY KEY, emp_name VARCHAR(100), salary DECIMAL(10, 2), dept_id INT, FOREIGN KEY (dept_id) REFERENCES departments(dept_id) );
INSERT INTO departments (dept_id, dept_name) VALUES (1, 'HR'), (2, 'Engineering'), (3, 'Marketing'), (4, 'Sales');
INSERT INTO employees (emp_id, emp_name, salary, dept_id) VALUES (101, 'Alice', 60000, 1), (102, 'Bob', 75000, 2), (103, 'Charlie', 50000, 3), (104, 'David', 80000, 2), (105, 'Eva', 55000, 1), (106, 'Frank', 40000, 4), (107, 'Grace', 90000, 2), (108, 'Helen', 45000, 3);
-- Questions.
-- Find the employees who earn more than the average salary of all employees.
SELECT * 
FROM employees
WHERE salary >(
SELECT AVG(salary)
FROM employees);
-- List the names of departments that have at least one employee earning more than 80,000.
SELECT dept_name
FROM departments
WHERE dept_id =(
SELECT dept_id 
FROM employees 
WHERE salary > 80000);
-- Find the employee(s) with the highest salary.
SELECT *
FROM employees
WHERE salary = (
SELECT MAX(salary)
FROM employees);
-- Display employees who work in the same department as 'Bob'.
SELECT * 
FROM employees
WHERE dept_id = (
SELECT dept_id 
FROM employees
WHERE emp_name = "Bob");
