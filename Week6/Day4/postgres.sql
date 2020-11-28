-- Day 3 
-- Write a query to display the names (first_name, last_name) using an alias name “First Name”, “Last Name” from employee table.
SELECT 
first_name AS "Full Name",
last_name AS "Last Name"
FROM employees;
-- Write a query to get a unique department ID from employee table.
SELECT department_id 
FROM employees
--how ever you interpet the question 
SELECT department_id
FROM employees
GROUP BY department_id;
-- Write a query to get the details of all employees from the employee table in descending order by their first name.
SELECT * FROM employees ORDER BY first_name ASC; 
-- Write a query to get the names (first_name, last_name), salary and 15% of salary as PF (what do you expect me to do here) (ie. alias) for all the employees.
SELECT first_name, last_name, salary, salary*.15 AS PF
	FROM employees;
-- Write a query to get the employee ID, names (first_name, last_name) and salary in ascending order according to their salary.
SELECT employees_id, first_name, last_name, salary FROM employees ORDER BY salary ASC;
-- Write a query to get the total salaries paid to the employees.
SELECT SUM(salary) FROM employees;
-- Write a query to get the maximum and minimum salary paid to the employees.
SELECT MAX(salary) FROM employees;
SELECT MIN(salary) FROM employees;
-- Write a query to get the average salary paid to the employees.
SELECT ROUND(AVG(salary))  AS "Round upto 2 decimal"; FROM employees;
-- Write a query to get the number of employees working in the company.
SELECT COUNT(employee_id) FROM employees
-- Write a query to get all the first name from the employees table in upper case.
SELECT UPPER(first_name) FROM employees

-- Write a query to get the first three characters of the first name for all the employees in the employees table.
SELECT SUBSTRING(first_name,1,3) 
     FROM employees;
-- Write a query to get the full name of all the employees from employees table. You have to include the first name and last name

not working 
SELECT
CONCAT  (first_name, ' ', last_name) AS "Full name"
FROM
employees;

-- Write a query to get the first name, last name and the length of the full name of all the employees from employees table.
SELECT first_name,last_name, LENGTH(first_name)+LENGTH(last_name)  'Length of Names' 
FROM employees; -- this one isnt working somehow 
SELECT first_name,last_name, LENGTH(first_name)+LENGTH(last_name)  
FROM employees;
-- Write a query to check whether the first_name column of the employees table containing any number.
SELECT first_name
FROM employees 
WHERE first_name 
SIMILAR TO '%0|1|2|3|4|5|6|7|8|9%';

SELECT * 
FROM employees 
WHERE first_name 
SIMILAR TO '%0|1|2|3|4|5|6|7|8|9%';

-- Write a query to select first ten records from a table.
SELECT *FROM employees WHERE employee_id <111

-- Restricting And Sorting
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000 
AND department_id IN (30, 100);


-- Write a query to display the name, including first_name and last_name and salary for all employees whose salary is between $10,000 and $15,000.
SELECT first_name, last_name, salary
FROM employees
WHERE salary >10000 AND <15000

SELECT first_name, last_name, salary
FROM employees
WHERE salary BETWEEN 10000 AND 15000
WHERE column_name BETWEEN value1 AND value2;
-- Write a query to display the name, including first_name and last_name and hire date for all employees who were hired in 1987.
why is this not working 
tryied the year function but nothing 
SELECT first_name, last_name
FROM employees 
WHERE hire_date LIKE '%1987';

-- Write a query to get the first name of the employees who holds the letter ‘c’ and ‘e’ in the first name.
 SELECT * FROM employees WHERE first_name LIKE 'C%'
 SELECT * FROM employees WHERE first_name LIKE 'E%'  
-- Write a query to display the last name, job, and salary for all the employees who don’t work as a Programmer or a Shipping Clerk, and not drawing the salary $4,500, $10,000, or $15,000.
SELECT first_name, last_name, salary, department_id
FROM employees
WHERE salary NOT BETWEEN 10000 AND 15000 

-- Write a query to display the last names of employees whose last name contain exactly six characters.

-- Write a query to display the last name of employees having ‘e’ as the third character.
SELECT first_name
FROM employees
where UPPER(first_name) like '%E%'
-- Write a query to display the jobs/designations available in the employees table.
--dont understand the question 
--but i guess it is this 
SELECT DISTINCT job_id  FROM employees;
-- WSELECT * 
FROM employees 
WHERE UPPER(last_name) IN('JONES', 'BLAKE', 'SCOTT', 'KING', 'FORD');

-- Update Statement
-- Write a SQL statement to change the email and commission_pct column of the employees table with ‘not available’ and 0.10 for all employees for those employees whose department_id is 110.
i dont understand  cant find commission_pct column doesnt seem to be there but coode should be like this: 
UPDATE employees 
SET email='Not available'
WHERE department_id=110 AND commission_pct=.10
-- Write a SQL statement to change the email column of the employees table with ‘available’ for those employees who belongs to the ‘Accounting’ department.
UPDATE employees
SET email= 'available'
WHERE department_id=11
-- Write a SQL statement to change the salary of an employee to 8000 whose ID is 105, if the existing salary is less than 5000.
UPDATE employees
SET salary =8000
WHERE employee_id=105  
AND salary < 5000;
-- Write a SQL statement to increase the salary of employees under the department 40, 90 and 110 according to the company rules that, the salary will be increased by 25% of the department 40, 15% for department 90 and 10% of the department 110 and the rest of the department will remain same.


