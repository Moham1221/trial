create procedure employee_insert @first_name nvarchar(55),
@last_name nvarchar(55),@address nvarchar(255),@contact_number nvarchar(55),@position nvarchar(55)
AS
insert into  [dbo].Employee (first_name, last_name, [address], contact_number, position) 
	   values(@first_name ,@last_name ,@address ,@contact_number,@position );


EXEC  employee_insert @first_name='lol' ,@last_name='habob',@address='msh hena' ,
@contact_number='55345',@position='part time';



create procedure  product_insert   @date_received date,
@brand_id int,@brand_name nvarchar(255),@model nvarchar(55),  @serial_number int,@availability nvarchar(55),
@date_sold date ,@customer_id int ,@unit_type  nvarchar(55)
AS
insert into  [dbo].[product] (date_received, brand_id, brand_name,
model, serial_number, [availability], date_sold,customer_id, unit_type) 
	   values(@date_received ,@brand_id ,@brand_name,@model,@serial_number 
	   ,@availability,@date_sold,@customer_id,@unit_type );

exec product_insert @date_received='2019-2-20 ',@brand_id=1 ,@brand_name='mo',@model='re',@serial_number=65 
	   ,@availability='yes',@date_sold='2019-2-22',@customer_id=1,@unit_type ='ll';



create procedure supplier_insert @name nvarchar(55),
@address nvarchar(55),@contact_number nvarchar(255),@brand_id int
AS
insert into  [dbo].[supplier] ([name],[address],contact_number,brand_id) 
	   values(@name ,@address ,@contact_number ,@brand_id );


exec supplier_insert   @name='mo' ,@address='lo' ,@contact_number='564' ,@brand_id=4;
exec supplier_insert   'mo','moo','so',3;



create procedure order_insert @customer_id int,
@employee_id int,@invoice_number int,@total_price int,@date_order date,
@quantity int ,@brand_id int
AS
insert into  [dbo].[orders] (customer_id, employee_id, 
invoice_number, total_price, date_order, quantity, brand_id) 
	   values(@customer_id ,@employee_id ,@invoice_number ,@total_price,@date_order,
	   @quantity,@brand_id);


exec order_insert @customer_id=1 ,@employee_id=1 ,@invoice_number=3242 ,@total_price=34,
@date_order='2019-2-20',
	   @quantity=4,@brand_id=6



create procedure customer_insert @first_name nvarchar(55),
@last_name nvarchar(55),@address nvarchar(255),@contact_number nvarchar(55)
AS
insert into  [dbo].[customer] (first_name, last_name, [address], contact_number) 
	   values(@first_name ,@last_name ,@address ,@contact_number );

EXEC  customer_insert @first_name='lol' ,@last_name='r',@address='msh hena' ,
@contact_number='55345' ;




create procedure chargeorder_insert @invoice_number int,
@brand_name nvarchar(55),@model nvarchar(255),@unit_Type nvarchar(55),@serial_number int
,@price int,@down_Payment int,@month_Term nvarchar(255),@monthly_Payment int
AS
insert into  [dbo].[charge_order] (invoice_number, brand_name, model, unit_Type
, serial_number, price, down_Payment, month_Term, monthly_Payment) 
	   values(@invoice_number, @brand_name, @model, @unit_Type
, @serial_number, @price, @down_Payment, @month_Term, @monthly_Payment );


exec chargeorder_insert @invoice_number=2134, @brand_name='', @model='', @unit_Type=''
, @serial_number=32243345, @price=44444, @down_Payment=4334, @month_Term=43, @monthly_Payment=43 ;



create procedure cashorder_insert @invoice_number int,
@brand_name nvarchar(55),@model nvarchar(255),@serial_number int,@price int,@unit_type nvarchar(55)
AS
insert into  [dbo].[cash_order] (invoice_number,brand_name, model, serial_number, price, unit_type) 
	   values(@invoice_number,@brand_name, @model, @serial_number, @price, @unit_type );


exec cashorder_insert @invoice_number=576,@brand_name='ojl', @model='jk', @serial_number=78789
, @price=43, @unit_type='';

select * from [dbo].[customer]