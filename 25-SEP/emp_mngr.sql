CREATE TABLE employee ( 
emp_id INT PRIMARY KEY,
name VARCHAR(100),
manager_id INT );

INSERT INTO employee (emp_id, name, manager_id) VALUES
(1, 'Alice Johnson', NULL),      
(2, 'Bob Smith', 1),
(3, 'Charlie Lee', 1), 
(4, 'David Kim', 2),
(5, 'Eva Green', 2),
(6, 'Frank Moore', 3),
(7, 'Grace Wong', 3),
(8, 'Henry Brown', 2);           

-- Find all employees along with the names of their managers.
SELECT e.emp_id, e.name, m.name as manager_name
FROM employee e
LEFT JOIN
employee m
ON e.manager_id = m.emp_id;

-- 2. Find all managers and how many employees report to them.
SELECT m.emp_id as manager_id,
m.name as manager_name,
COUNT(e.emp_id) as reportees
FROM employee m
INNER JOIN 
employee e
ON e.manager_id = m.emp_id
group by m.emp_id, m.name;

-- 3. Find all employees who do not have a manager.
SELECT * 
FROM employee
WHERE manager_id is null;