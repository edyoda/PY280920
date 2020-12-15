-- BRANCH SUPPLIER
-- INSERT INTO branch_supplier VALUES(2, 'Hammer Mill', 'Paper');
-- INSERT INTO branch_supplier VALUES(2, 'Uni-ball', 'Writing Utensils');
-- INSERT INTO branch_supplier VALUES(3, 'Patriot Paper', 'Paper');
-- INSERT INTO branch_supplier VALUES(2, 'J.T. Forms & Labels', 'Custom Forms');
-- INSERT INTO branch_supplier VALUES(3, 'Uni-ball', 'Writing Utensils');
-- INSERT INTO branch_supplier VALUES(3, 'Hammer Mill', 'Paper');
-- INSERT INTO branch_supplier VALUES(3, 'Stamford Lables', 'Custom Forms');

-- CLIENT
INSERT INTO client VALUES(400, 2, 'Dunmore Highschool');
INSERT INTO client VALUES(401, 2, 'Lackawana Country');
INSERT INTO client VALUES(402, 3, 'FedEx');
INSERT INTO client VALUES(403, 3, 'John Daly Law, LLC');
INSERT INTO client VALUES(404, 2, 'Scranton Whitepages');
INSERT INTO client VALUES(405, 3, 'Times Newspaper');
INSERT INTO client VALUES(406, 2, 'FedEx');

-- WORKS_WITH
INSERT INTO works_with VALUES(105, 400, 55000);
INSERT INTO works_with VALUES(102, 401, 267000);
INSERT INTO works_with VALUES(108, 402, 22500);
INSERT INTO works_with VALUES(107, 403, 5000);
INSERT INTO works_with VALUES(108, 403, 12000);
INSERT INTO works_with VALUES(105, 404, 33000);
INSERT INTO works_with VALUES(107, 405, 26000);
INSERT INTO works_with VALUES(102, 406, 15000);
INSERT INTO works_with VALUES(105, 406, 130000);