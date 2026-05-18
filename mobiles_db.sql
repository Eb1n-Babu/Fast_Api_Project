create database mobiles_db;

use mobiles_db;

create table products (
    product_id int auto_increment primary key,
    brand varchar(50) not null,
    model varchar(50) not null,
    description text,
    price decimal(10,2) not null
);

select * from products;

insert into products (brand, model, description, price)
values
('Samsung', 'Galaxy A1', 'Entry-level smartphone', 12000.00),
('Samsung', 'Galaxy A2', 'Budget smartphone', 15000.00),
('Samsung', 'Galaxy A3', 'Mid-range smartphone', 18000.00),
('Apple', 'iPhone SE', 'Compact iPhone model', 30000.00),
('Apple', 'iPhone 12', 'Flagship iPhone', 60000.00),
('Apple', 'iPhone 13', 'Latest iPhone model', 70000.00),
('Xiaomi', 'Redmi Note 10', 'Affordable smartphone', 14000.00),
('Xiaomi', 'Redmi Note 11', 'Updated budget smartphone', 16000.00),
('OnePlus', 'Nord CE', 'Mid-range OnePlus phone', 25000.00),
('OnePlus', 'OnePlus 9', 'Flagship OnePlus phone', 50000.00);

