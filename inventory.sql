create database inventory

use inventory
go

create table  customer(customer_id  INTEGER  primary key identity(1,1) ,
                                                    first_name  nvarchar(40) not null,
                                                    last_name  nvarchar(40) not null,
                                                    [address]   nvarchar(255)  null,
                                                    contact_number    nvarchar(40)  not null);

create table  Employee(employee_id   INTEGER  PRIMARY KEY identity(1,1)  ,
                                                    first_name  nvarchar(40) not null,
                                                    last_name  nvarchar(40) not null,
                                                    address   nvarchar(255) null,
                                                    contact_number    nvarchar(40) not null,
                                                      position  nvarchar(40)   not null);
                                                        


create table  supplier(supplier_id   INTEGER  PRIMARY KEY identity(1,1) ,
                                                         [name]  nvarchar(40)  not null,
                                        [address]   nvarchar(255) null,
                                          contact_number    nvarchar(40)   not null,
                                                 brand_id  int    not null)
												 ;



create table  orders(order_id   INTEGER   PRIMARY KEY identity(1,1) ,
                                                                customer_id int not null,
                                                                employee_id  int not null,
                                                                invoice_number int   not null,
                                                                total_price int not null,
                                                                date_order  date not null,
                                                                quantity  int not null,
                                                                brand_id   int not null,
                                                              
                                                                foreign key(customer_id)   references  customer(customer_id),
                                                                foreign key(employee_id) references Employee(employee_id) );


create table cash_order(cash_order_id   INTEGER  PRIMARY KEY identity(1,1),
                              invoice_number  int not null,
                              brand_name nvarchar(50) null,
                              model nvarchar(50) null,
                              serial_number  int  not null,
                              price int not null,
                              unit_type  nvarchar(55) null );




create table  product(product_id   INTEGER primary key identity(1,1) ,
                                                   date_received  date,
                                                   brand_id   int not null,
                                                   brand_name nvarchar(55),
                                                   model    nvarchar(55),
                                                   serial_number   int   not null,
                                                   [availability]    nvarchar(55)  not null,
                                                   date_sold     date,
                                                   customer_id    int not null,
                                                   unit_type   nvarchar(55)  not null,
                                                   foreign key(customer_id) references customer(customer_id));



create table  charge_order(chargeoder_id   INTEGER  primary key identity(1,1),
                                                        invoice_number int,
                                                        brand_name   nvarchar(50),
                                                        model	nvarchar(50),
                                                        unit_Type	nvarchar(50),
                                                        serial_Number	int not null,
                                                        price	 int not null,
                                                        down_Payment	Int	not null,
                                                        month_Term	nvarchar(255),
                                                        monthly_Payment int not null);

alter table        supplier add constraint brand_product  foreign key     
(Brand_id) REFERENCES product (product_id)     ;                            


alter table        orders add constraint order_product
foreign key(brand_id) references product(product_id);


create view trial as
select b.brand_id,b.brand_name ,o.invoice_number,o.quantity from product b 
inner join orders o on o.customer_id=b.customer_id



