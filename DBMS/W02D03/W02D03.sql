USE MOHIT;

INSERT INTO employee VALUES(
100,'David','Wallace','1967-11-17','M',250000,NULL,NULL);

INSERT INTO branch VALUES(
1,'Corporate',100,'2006-02-09');

UPDATE employee
SET branch_id = 1
WHERE emp_id=100;

INSERT INTO employee VALUES(
101,'Jan','Levinson','1961-05-11','F',110000,100,1);

INSERT INTO employee VALUES(
102,'Michael','Scott','1964-03-15','M',75000,100,NULL);

INSERT INTO branch VALUES(
2,'Scranton',102,'1992-04-06');

UPDATE employee
SET branch_id = 2
WHERE emp_id=102;

INSERT INTO employee VALUES
(103,'Angela','Martin','1971-06-25','F',63000,102,2),
(104,'Kelly','Kapoor','1980-02-05','F',55000,102,2),
(105,'Stanley','Hudson','1958-02-19','M',69000,102,2),
(106,'Josh','Porter','1969-09-05','M',78000,100,NULL);

INSERT INTO branch VALUES(
3,'Stamford',106,'1998-02-13');

UPDATE employee
SET branch_id = 3
WHERE emp_id=106;

INSERT INTO employee VALUES
(107,'Andy','Bernard','1973-07-22','M',65000,106,3),
(108,'Jim','Halpert','1978-10-01','M',71000,106,3);