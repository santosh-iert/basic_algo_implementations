
/* Query to use the database */
use camsec_database;

/* Query to retrive data from the table */
select * from adduser;

/* Query to create the table */
CREATE TABLE Images (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name varchar(250),
  data BLOB
);


/*  Conditianal queries in SQL
Example
*/

SELECT CASE
    WHEN 2 * GREATEST(A, B, C) >= (A + B + C) THEN "Not A Triangle"
    WHEN A = B AND A = C                      THEN "Equilateral"
    WHEN A = B OR A = C OR B = C              THEN "Isosceles"
                                              ELSE "Scalene"
    END
FROM TRIANGLES