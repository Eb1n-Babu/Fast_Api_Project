create database company_db;
use company_db;

create table employee(employee_id int auto_increment primary key,
first_name varchar(50) not null,last_name varchar(50) not null,
email varchar(50) unique, department varchar(50) not null,
salary decimal(10,2),hire_date date,country varchar(50),phone varchar(20),
status enum("Active","Inactive") default "Active");

select * from employee;

insert into employee(first_name,last_name,email,department,salary,hire_date,country,phone,status) values
("jhone","emanuval","jhone.m@gmail.com","IT",55000,"2025-08-9","India","+91-6245678967","Active");

insert into employee(first_name, last_name, email, department, salary, hire_date, country, phone, status) values
('anita','sharma','anita.sharma@example.com','hr',48000.00,'2022-03-10','india','+91-9876543210','active'),
('rahul','menon','rahul.menon@example.com','it',60000.00,'2021-11-20','india','+91-9123456780','inactive'),
('meera','nair','meera.nair@example.com','finance',52000.00,'2020-06-15','india','+91-9988776655','active'),
('arjun','patel','arjun.patel@example.com','marketing',45000.00,'2023-01-05','india','+91-8899776655','active'),
('sneha','rao','sneha.rao@example.com','sales',47000.00,'2022-07-22','india','+91-7766554433','inactive'),
('vijay','kumar','vijay.kumar@example.com','it',62000.00,'2021-09-18','india','+91-6655443322','active'),
('priya','joshi','priya.joshi@example.com','hr',49000.00,'2020-12-01','india','+91-9988123456','active'),
('manoj','reddy','manoj.reddy@example.com','finance',53000.00,'2023-02-14','india','+91-8877665544','inactive'),
('deepa','pillai','deepa.pillai@example.com','marketing',46000.00,'2021-05-30','india','+91-7766443322','active'),
('suresh','gupta','suresh.gupta@example.com','sales',50000.00,'2022-08-25','india','+91-6655332211','active'),
('nisha','verma','nisha.verma@example.com','it',61000.00,'2020-04-12','india','+91-9988771122','inactive'),
('rohit','singh','rohit.singh@example.com','hr',48000.00,'2023-03-19','india','+91-8877552211','active'),
('kavya','iyer','kavya.iyer@example.com','finance',54000.00,'2021-07-07','india','+91-7766552211','active'),
('amit','das','amit.das@example.com','marketing',47000.00,'2022-09-09','india','+91-6655441122','inactive'),
('pooja','mishra','pooja.mishra@example.com','sales',49000.00,'2020-10-10','india','+91-9988665544','active'),
('sanjay','roy','sanjay.roy@example.com','it',63000.00,'2021-01-15','india','+91-8877661122','active'),
('rekha','gopal','rekha.gopal@example.com','hr',50000.00,'2022-05-05','india','+91-7766442211','inactive'),
('ajay','thomas','ajay.thomas@example.com','finance',55000.00,'2020-02-20','india','+91-6655331122','active'),
('divya','george','divya.george@example.com','marketing',46000.00,'2023-04-04','india','+91-9988776654','active'),
('mohan','chowdhury','mohan.chowdhury@example.com','sales',48000.00,'2021-06-06','india','+91-8877554433','inactive'),
('sita','banerjee','sita.banerjee@example.com','it',64000.00,'2022-07-07','india','+91-7766554433','active'),
('alok','sen','alok.sen@example.com','hr',51000.00,'2020-08-08','india','+91-6655443321','active'),
('geeta','paul','geeta.paul@example.com','finance',56000.00,'2021-09-09','india','+91-9988772211','inactive'),
('naveen','fernandes','naveen.fernandes@example.com','marketing',47000.00,'2022-10-10','india','+91-8877665544','active'),
('radha','desai','radha.desai@example.com','sales',50000.00,'2020-11-11','india','+91-7766443321','active'),
('arvind','joshi','arvind.joshi@example.com','it',65000.00,'2021-12-12','india','+91-6655332210','inactive'),
('latha','krishnan','latha.krishnan@example.com','hr',52000.00,'2022-01-01','india','+91-9988771100','active'),
('sunil','mehta','sunil.mehta@example.com','finance',57000.00,'2020-02-02','india','+91-8877551100','active'),
('rekha','rao','rekha.rao@example.com','marketing',48000.00,'2021-03-03','india','+91-7766551100','inactive'),
('gopal','iyer','gopal.iyer@example.com','sales',51000.00,'2022-04-04','india','+91-6655441100','active'),
('usha','patel','usha.patel@example.com','it',66000.00,'2020-05-05','india','+91-9988661100','active'),
('rajesh','singh','rajesh.singh@example.com','hr',53000.00,'2021-06-06','india','+91-8877661100','inactive'),
('savita','pillai','savita.pillai@example.com','finance',58000.00,'2022-07-07','india','+91-7766441100','active'),
('mahesh','reddy','mahesh.reddy@example.com','marketing',49000.00,'2020-08-08','india','+91-6655331100','active'),
('kamala','nair','kamala.nair@example.com','sales',52000.00,'2021-09-09','india','+91-9988774433','inactive'),
('vivek','gupta','vivek.gupta@example.com','it',67000.00,'2022-10-10','india','+91-8877554433','active'),
('shilpa','verma','shilpa.verma@example.com','hr',54000.00,'2020-11-11','india','+91-7766554433','active'),
('dinesh','roy','dinesh.roy@example.com','finance',59000.00,'2021-12-12','india','+91-6655444433','inactive'),
('sarita','banerjee','sarita.banerjee@example.com','marketing',50000.00,'2022-01-01','india','+91-9988773322','active'),
('kiran','das','kiran.das@example.com','sales',53000.00,'2020-02-02','india','+91-8877663322','active'),
('rekha','iyer','rekha.iyer@example.com','it',68000.00,'2021-03-03','india','+91-7766443322','inactive'),
('suresh','paul','suresh.paul@example.com','hr',55000.00,'2022-04-04','india','+91-6655333322','active'),
('nisha','fernandes','nisha.fernandes@example.com','finance',60000.00,'2020-05-05','india','+91-9988772210','active'),
('arun','desai','arun.desai@example.com','marketing',51000.00,'2021-06-06','india','+91-8877552210','inactive'),
('rekha','sen','rekha.sen@example.com','sales',54000.00,'2022-07-07','india','+91-7766552210','active'),
('manju','george','manju.george@example.com','it',69000.00,'2020-08-08','india','+91-6655442210','active'),
('alok','chowdhury','alok.chowdhury@example.com','hr',56000.00,'2021-09-09','india','+91-9988771109','inactive'),
('geeta','thomas','geeta.thomas@example.com','finance',61000.00,'2022-10-10','india','+91-8877661109','active');