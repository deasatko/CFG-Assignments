-- TASK 1 - CREATE DATABASE (commenting to not run it auto if not needed)
CREATE DATABASE bookstore;

USE bookstore;

-- TASK 5 - DIFFERENT  DATA TYPES
-- TASK 15 - DUPLICATE CHECK (each table holds unique data for each entry, no duplicates can happen)
-- TASK 2 - PRIMARY and FOREIGN KEYS 1/2
-- TASK 6 2/2

-- Creating the book table
-- PRIMARY KEY is a constraint hat makes sure that each value in the column is unique and not NULL.
-- AUTO_INCREMENT: for each new record added  to the table, it will generate an integer (x + 1). No duplicates.
-- price set to be up to 10 digits in total of which 2 digits are decimals.
-- Addded a CHECK for StockQuantity and Price (to avoid negative stock quantity and price 0 or less .
CREATE TABLE book (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL,
    CHECK (price > 0),
    CHECK (stock_quantity >= 0)
);

-- Creating the Customers table
-- UNIQUE added for the email addresses.
CREATE TABLE customer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    address TEXT
);

-- TASK 2 - PRIMARY and FOREIGN KEYS 2/2
-- Creating the Orders table
-- FOREIGN KEY usage: links two tables together. In this case links the CustomerID field in the Customers table. 
-- A customer can have multiple orders but each order is linked to different customers.
CREATE TABLE order_transaction (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

-- Creating the order_details table
CREATE TABLE order_detail (
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (order_id) REFERENCES order_transaction(id),
    FOREIGN KEY (book_id ) REFERENCES book(id),
    CHECK (quantity > 0)
);

-- TASK 3 - POPULATE DB 
-- TASK 7 - INSERT DATA
-- Inserting data into book table 
-- source for books and prices: https://www.lovereading.co.uk/genres/lrt10/uk-top-10-books
INSERT INTO book (title, author, price, stock_quantity) VALUES 
('The Last Devil To Die', 'Richard Osman', 8.99, 50),
('Yellowface', 'Rebecca F Kuang', 8.99, 20),
('Someone Else’s Shoes', 'Jojo Moyes', 10.99, 70),
('Traitors Gate', 'Jeffrey Archer', 8.99, 30),
('Resurrection Walk', 'Michael Connelly', 8.99, 80),
('Evocation', 'S.T. Gibson', 17.99, 60),
('Ruthless Vows', 'Rebecca Ross', 13.49, 300),
('Ultra-Processed People', 'Chris van Tulleken', 9.89, 40);

-- Inserting data into customer table
INSERT INTO customer (name, email, address) VALUES 
('Martina Zerbi', 'mzerb@outlookk.com', '12 Daisy Rd'),
('Andrea Silinga', 'asiling@outlookk.com', '45 Rose Rd'),
('Giacomo Zucca', 'gzucca@outlookk.com', '87 Geranium Rd'),
('Francesca Bella', 'fbella@outlookk.com', '93 Peppermint Rd'),
('Michele Bassi', 'mbassi@outlookk.com', '28 Chedarwood Rd'),
('Sara Taglia', 'staglia@outlookk.com', '86 Orange Rd'),
('Davide Solito', 'dsolito@outlookk.com', '76 Cherry Rd'),
('Marco Ballari', 'mballari@outlookk.com', '34 Love Rd');

-- Inserting data into order_transaction table
INSERT INTO order_transaction (customer_id, order_date) VALUES 
(1, '2024-06-03'),
(2, '2024-06-04'),
(3, '2024-06-05'),
(4, '2024-06-6'),
(5, '2024-06-07'),
(6, '2024-06-08'),
(7, '2024-06-10'),
(8, '2024-06-11');

-- Inserting data into order_details table (Mock Data); it will help us when we query which books were included in which orders, how many books were ordered etc..
-- Each tuple in the values represents what needs to be inserted into order_detail table.
INSERT INTO order_detail (order_id, book_id, quantity) VALUES 
(1, 1, 2),
(1, 2, 1),
(2, 3, 1),
(2, 4, 3),
(3, 5, 1),
(3, 6, 2),
(4, 7, 1),
(5, 8, 2),
(6, 1, 1),
(7, 3, 1),
(8, 5, 1);

-- TASK 8 - RETRIEVE
-- Retrieving all book
SELECT * FROM book ORDER BY title;

-- Retrieving all customer
SELECT * FROM customer ORDER BY name;

-- Retrieving all order_transaction
SELECT * FROM order_transaction ORDER BY order_date;

-- Retrieving order_details for a specific order
SELECT * FROM order_detail WHERE order_id = 1;

-- TASK 11 - JOINS
-- Retrieving all orders along with customer information and order by date
SELECT order_transaction.id, customer.name, order_transaction.order_date 
FROM order_transaction
JOIN customer ON order_transaction.customer_id = customer.id
ORDER BY order_transaction.order_date;

-- TASK 10 - AGGREGATE FUNCTIONS
-- Calculating the total number of order_transaction
SELECT COUNT(*) AS total_orders FROM order_transaction;

-- Calculating the total revenue
SELECT SUM(book.price * order_detail.quantity) AS total_revenue
FROM order_detail
JOIN book ON order_detail.book_id = book.id;

-- Finding the most popular book
SELECT book.title, SUM(order_detail.quantity) AS total_sold
FROM order_detail
JOIN book ON order_detail.book_id = book.id
GROUP BY book.title
ORDER BY total_sold DESC
LIMIT 1;

-- TASK 12 - IN-BUILT FUNCTIONS
-- Using UPPER as an additional in-built function
SELECT id, UPPER(title) AS Uppercasetitle, author, price, stock_quantity
FROM book;

-- Using CONCAT() as an additional in-built function
SELECT id, CONCAT(name, ' (', email, ')') AS customer_contact
FROM customer;

-- TASK 9 - DELETE FUNCTION
-- Deleting an order (commenting this section to not run it automatically)

-- DELETE FROM order_transaction WHERE id = 8;

-- There is a Foreign Key Constraint applied on the order_details table, resolving it this way:

-- Deleting the dependent records from order_details
-- DELETE FROM order_detail WHERE order_id = 8;

-- Deleting the record from order_transaction
-- DELETE FROM order_transaction WHERE oderd_id = 8;

-- Checking if the deletion was successful
-- SELECT * FROM order_transaction;
-- SELECT * FROM order_detail; 

-- TASK 13 - ORDER BY (most of the tables above have this function)
-- TASK 14 - STORED PROCEDURE
-- Creating a stored procedure to find all orders for a specific customer as per assignment requisite.
-- Added the DROP PROCEDURE to troubleshoot as I had typos in my code and I did not want to manually delete the procedure everytime.

DROP PROCEDURE IF EXISTS getcustomerorder ;
DELIMITER //
CREATE PROCEDURE getcustomerorder(IN cust_id INT)
BEGIN
    SELECT order_transaction.id, order_transaction.order_date, book.title, order_detail.quantity
    FROM order_transaction
    JOIN order_detail ON order_transaction.id = order_detail.id
    JOIN book ON order_detail.book_id = book.id
    WHERE order_transaction.customer_id = cust_id
    ORDER BY order_transaction.order_date;
END //
DELIMITER ;

-- Using the stored procedure
CALL getcustomerorder(1);
