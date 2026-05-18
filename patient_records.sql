create database ehr;

use ehr;

create table patient_records (
    name varchar(100) primary key,
    age int,
    location varchar(100)
);

insert into patient_records (name, age, location) values
('arun', 25, 'kochi'),
('meera', 30, 'thrissur'),
('rahul', 28, 'malappuram'),
('sneha', 22, 'palakkad'),
('vijay', 35, 'ernakulam'),
('anju', 27, 'perinthalmanna'),
('manoj', 40, 'kottayam'),
('nisha', 33, 'calicut'),
('deepak', 29, 'trivandrum'),
('lakshmi', 24, 'alappuzha'),
('suresh', 31, 'wayanad'),
('geetha', 26, 'idukki'),
('arjun', 23, 'kasargod'),
('bindu', 34, 'kozhikode'),
('santosh', 38, 'thrissur'),
('reshma', 21, 'malappuram'),
('jithin', 32, 'ernakulam'),
('priya', 28, 'palakkad'),
('mohan', 36, 'trivandrum'),
('divya', 25, 'kochi');
