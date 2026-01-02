create database insta;
use insta;
create table accounts(
    username varchar(255),
    firstname varchar(50),
    posts int,
    country varchar(50)
);

insert into accounts values('_sravss_123','sravani',7,'india'),
                           ('_mouni456','mouni',5,'india');

select * from accounts;
