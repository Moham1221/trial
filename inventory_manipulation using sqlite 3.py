import sqlite3
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()


def addcustomer(first_name, last_name, address, contact_number):
    try:
        cursor.execute("insert into  customer\
        (first_name,last_name,address,contact_number) values(?,?,?,?) ", (first_name, last_name, address, contact_number))
        conn.commit()
        interface()
    except:
        print('database error')
        interface()

   #  interface()


def addsupplier(name, address, contact_number, brand_id):
    try:
        cursor.execute('insert into  supplier\
        (name,address,contact_number,brand_id) values(?,?,?,?)',
                       (name, address, contact_number, brand_id))
        conn.commit()
        interface()
    except:
        print('database error')
        interface()


def addEmployee(first_name, last_name, address, contact_number, position):
    try:
        cursor.execute('insert into  Employee\
       (first_name, last_name, address, contact_number, position) values(?,?,?,?,?)',
                       (first_name, last_name, address, contact_number, position))
        conn.commit()
        interface()
    except:
        print('database error')
        interface()


def addorders(customer_id, employee_id, invoice_number, total_price, date_order, quantity, brand_id):
    try:
      cursor.execute('insert into  orders\
      (customer_id, employee_id, invoice_number, total_price, date_order, quantity, brand_id) values(?,?,?,?,?,?,?)',
                     (customer_id, employee_id, invoice_number, total_price, date_order, quantity, brand_id))
      conn.commit()
      interface()

    except:
        print('database error')
    interface()


def addcash_order(invoice_number,brand_name, model, serial_number, price, unit_type):
    try:
        cursor.execute('insert into  cash_order (invoice_number,brand_name, model, serial_number, price, unit_type)\
        values(?,?,?,?,?,?)',
                       (invoice_number,brand_name, model, serial_number, price, unit_type))
        conn.commit()
        interface()
    except:
        print('database error')
        interface()


def addproduct(date_received, brand_id, brand_name, model, serial_number, availability, date_sold, customer_id, unit_type):
    try:
      cursor.execute('insert into  product\
      (date_received, brand_id, brand_name, model, serial_number, availability, date_sold, customer_id, unit_type) values(?,?,?,?,?,?,?,?,?)',
                     (date_received, brand_id, brand_name, model, serial_number, availability, date_sold, customer_id, unit_type))
      conn.commit()
      interface()

    except:
        print('database error')
        interface()


def addcharge_order(invoice_number, brand_name, model, unit, serial_number, price, down_Payment, month_Term, monthly_Payment):
    try:
      cursor.execute('insert into  charge_order\
      (invoice_number, brand_name, model, unit, serial_number, price, down_Payment, month_Term, monthly_Payment) values(?,?,?,?,?,?,?,?,?)',
                     (invoice_number, brand_name, model, unit, serial_number, price, down_Payment, month_Term, monthly_Payment))
      conn.commit()
      interface()
    except:
        print('database error')
        interface()




def add_data():
    print('pls choose a table: 1-customer 2-supplier 3-Employee 4-orders 5-cash_order 6-product  7-charge_order')
    tableselect = input('1,2,3,4,5,6,7:')
    if tableselect == '1':
        addcustomer(input('firstname:'), input('lastname:'),
                    input('address:'), input('phone:'))

    elif tableselect == '2':
        addsupplier(input('name:'), input('address:'), input('contact_number:'), int(input('brand_id:')))

    elif tableselect == '3':
        addEmployee(input('first_name:'), input('last_name:'), input(
            'address:'), input('contact_number:'), input('position:'))

    elif tableselect == '4':
        addorders(int(input('customer_id:')), int(input('employee_id:')), int(input('invoice_number:')),
                   int(input('total_price:')), input('date_order:'), int(input("quantity:")),int(input("brand_id:")))

    elif tableselect == '5':
        addcash_order(int(input('invoice_number')),input('brand_name:'), input('model:'), int(input('serial_number:')),
                     int(input('price:')), input('unit_type:'))


    elif tableselect == '6':
        addproduct(input("date_received:"),int(input("brand_id:")),input("brand_name:"),input("model:"),
        int(input("serial_number:")),input("availability:"),input("date_sold:"),int(input("customer_id:")),input("unit_type:"))

    elif tableselect == '7':
        addcharge_order(int(input("invoice_number:")),input("brand_name:"),input("model:"),input("unit:"),
        int(input("serial_number:")),int(input("price:")),int(input("down_Payment:")),int(input("month_Term:")),int(input("monthly_Payment:")))
    else:
        print('wrong operation')
        interface()


def viewcustomer():
    cursor.execute('select * from  customer')
    res = cursor.fetchall()
    print(f'there are {len(res)} record')
    print('customer_id  ,first_name  ,last_name  ,address  ,contact_number')
    for i in res:
       print(i)
    interface()


def viewEmployee():
   cursor.execute('select * from  Employee')
   res = cursor.fetchall()
   print(f'there are {len(res)} record')
   print('employee_id  ,first_name  ,last_name  ,address  ,contact_number  ,position')
   for i in res:
      print(i)
   interface()


def viewsupplier():
   cursor.execute('select * from  supplier')
   res = cursor.fetchall()
   print(f'there are {len(res)} record')
   print('supplier_id  ,name  ,address  ,contact_number  ,brand_id  ')
   for i in res:
      print(i)
   interface()


def vieworders():
   cursor.execute('select * from  orders')
   res = cursor.fetchall()
   print(f'there are {len(res)} record')
   print('order_id  ,customer_id  ,employee_id  ,invoice_number  ,total_price  ,date_order  ,quantity  ,brand_id  ')
   for i in res:
      print(i)
   interface()


def viewcash_order():

   cursor.execute('select * from  cash_order')
   res = cursor.fetchall()
   print(f'there are {len(res)} record')
   print('cash_order_id  ,invoice_number  ,brand_name  ,model  ,serial_number  ,price  ,unit_type   ')
   for i in res:
      print(i)
   interface()

def viewproduct():
   cursor.execute('select * from  product')
   res = cursor.fetchall()
   print(f'there are {len(res)} record')
   print('product_id  ,date_received  ,brand_id  ,brand_name  ,model  ,serial_number  ,availability  ,date_sold  ,customer_id  ,unit_type   ')
   for i in res:
      print(i)
   interface()

def viewcharge_order():
   cursor.execute('select * from  charge_order')
   res = cursor.fetchall()
   print(f'there are {len(res)} record')
   print('chargeoder_id  ,invoice_number  ,brand_name  ,model  ,unit_Type  ,serial_Number  ,price  ,down_Payment  ,month_Term  ,monthly_Payment   ')
   for i in res:
      print(i)
   interface()


def viewing_data():
    print('pls select table to view:1-customer 2-supplier 3-Employee 4-orders 5-cash_order 6-product  7-charge_order')
    tableselect = input('1,2,3,4,5,6,7:')
    if tableselect == '1':
        viewcustomer()
    elif tableselect == '2':
        viewsupplier()
    elif tableselect == '3':
        viewEmployee()
    elif tableselect == '4':
        vieworders()
    elif tableselect == '5':
        viewcash_order()
    elif tableselect == '6':
        viewproduct()
    elif tableselect == '7':
        viewcharge_order()        
    else:
        print('wrong operation')
        interface()


def customerertainciew():
    s1 = input('which element to search with:1-customer_id  \
        2-first_name  3-last_name  4-contact_number :')
    if s1 == '1':
        sear = int(input('customer_id:'))
        try:
            cursor.execute(
                f'select customer_id from  customer where customer_id={sear}')
            res1=cursor.fetchone()
            for i in res1:
                c=i
            if c==sear:  
                    cursor.execute(
                            f'select * from  customer where customer_id={sear}')
                    res = cursor.fetchall()
                    for i in res:
                        print(i)
        except:
            print('id not found')              
        interface()
    elif s1 == '2':
        sear = input('first_name:')
        try:
            cursor.execute(
                f'select customer_id from  customer where first_name={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  customer where first_name='{sear}'")
                res = cursor.fetchall()
                for i in res:
                        print(i)

        except:
            print('first name not found')  
            
        interface()
    elif s1 == '3':
        sear = input('last_name :')
        try:
            cursor.execute(
                f'select customer_id from  customer where last_name={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                f"select * from  customer where last_name='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('first name not found')         
        interface()
    elif s1 == '4':
        sear = input('contact_number :')
        try:
            cursor.execute(
                f'select customer_id from  customer where contact_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  customer where contact_number='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('contact_number not found')
        interface()
    else:
        print('wrong operation')
        interface()


def Employee_certainview():
    s1 = input('which element to search with:1-employee_id  \
        2-first_name  3-last_name  4-contact_number   5-position:')
    if s1 == '1':
        sear = int(input('employee_id:'))
        try:
            cursor.execute(
                f'select employee_id from  Employee where employee_id={sear}')
            res1=cursor.fetchone()
            for i in res1:
                c=i
            if c==sear:  
                cursor.execute(
                    f'select * from  Employee where employee_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('employee_id not found')
        interface()    

    elif s1 == '2':
        sear = input('first_name:')
        try:
            cursor.execute(
                f'select first_name from  Employee where first_name={sear}')
            res1=cursor.fetchone()
            for i in res1:
                c=i
            if c==sear:  
                cursor.execute(
                    f'select * from  Employee where first_name={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('first_name not found')
        interface()

    elif s1 == '3':
        sear = input('last_name :')
        try:
            cursor.execute(
                f'select last_name from  Employee where last_name={sear}')
            res1=cursor.fetchone()
            for i in res1:
                c=i
            if c==sear:  
                cursor.execute(
                    f"select * from  Employee where last_name='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('last_name not found')
        interface()

    elif s1 == '4':
        sear = input('contact_number:')
        try:
            cursor.execute(
                f'select contact_number from  Employee where contact_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  Employee where contact_number='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('contact_number not found')
        interface()

    elif s1 == '5':
        sear = input('position:')
        try:
            cursor.execute(
                f'select position from  Employee where position={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  Employee where position='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('position not found')
        interface()
    else:
        print('wrong operation')
        interface()


def suppliercertainview():
    s1 = input('which element to search with:1-supplier_id  \
        2-name  3-contact_number  4-position :')
    if s1 == '1':
        sear = int(input('supplier_id:'))
        try:
            cursor.execute(
                f'select supplier_id from  supplier where supplier_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  supplier where supplier_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('supplier_id not found')            
        interface()
    elif s1 == '2':
        sear = input('name:')
        try:
            cursor.execute(
                f'select name from  supplier where name={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  supplier where name='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('name not found')
        interface()
    elif s1 == '3':
        sear = input('contact_number :')
        try:
            cursor.execute(
                f'select contact_number from  supplier where contact_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  supplier where contact_number='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('contact_number not found')
        interface()
    elif s1 == '4':
        sear = int(input('brand_id:'))
        try:
            cursor.execute(
                f'select brand_id from  supplier where brand_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  supplier where brand_id='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('brand_id not found')
        interface()

    else:
        print('wrong operation')
        interface()


def orderscertainsview():
    s1 = input('which element to search with:1-order_id  \
        2-customer_id  3-employee_id 4-invoice_number   5-total_price 6-quantity 7-brand_id :')
    if s1 == '1':
        sear = int(input('order_id :'))
        try:
            cursor.execute(
                f'select order_id from  orders where order_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  orders where order_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('order_id not found')
        interface()
    elif s1 == '2':
        sear = int(input('customer_id :'))
        try:
            cursor.execute(
                f'select customer_id from  orders where customer_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  orders where customer_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)

        except:
            print('customer_id not found')
        interface()

    elif s1 == '3':
        sear = int(input('employee_id :'))
        try:
            cursor.execute(
                f'select employee_id from  orders where employee_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  orders where employee_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('employee_id not found')
        interface()
    elif s1 == '4':
        sear = int(input('invoice_number:'))
        try:
            cursor.execute(
                f'select invoice_number from  orders where invoice_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  orders where invoice_number='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('invoice_number not found')
        interface()
    elif s1 == '5':
        sear = int(input('total_price:'))
        try:
            cursor.execute(
                f'select total_price from  orders where total_price={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  orders where total_price='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('total_price not found')
        interface()
    elif s1 == '6':
        sear = int(input('quantity:'))
        try:
            cursor.execute(
                f'select quantity from  orders where quantity={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  orders where quantity='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('quantity not found')
        interface()
    elif s1 == '7':
        sear = int(input('brand_id:'))
        try:
            cursor.execute(
                f'select brand_id from  orders where brand_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  orders where brand_id='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('brand_id not found')
        interface()    
    else:
        print('wrong operation')
        interface()


def cash_ordercertainview():
    s1 = input('which element to search with:1-cash_order_id  \
        2-invoice_number  3-brand_name  4-model   5-serial_number  6-price :')
    if s1 == '1':
        sear = int(input('cash_order_id :'))
        try:
            cursor.execute(
                f'select cash_order_id from  cash_order where cash_order_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  cash_order where cash_order_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('cash_order_id not found')
        interface()
    elif s1 == '2':
        sear = int(input('invoice_number:'))
        try:
            cursor.execute(
                f'select invoice_number from  cash_order where invoice_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  cash_order where invoice_number={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('invoice_number not found')                  
        interface()
    elif s1 == '3':
        sear = input('brand_name :')
        try:
            cursor.execute(
                f'select brand_name from  cash_order where brand_name={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  cash_order where brand_name='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('brand_name not found')
        interface()
    elif s1 == '4':
        sear = input('model:')
        try:
            cursor.execute(
                f'select model from  cash_order where model={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  cash_order where model='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('model not found')
        interface()
    elif s1 == '5':
        sear = input('serial_number:')
        try:
            cursor.execute(
                f'select serial_number from  cash_order where serial_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  cash_order where serial_number='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('serial_number not found')
        interface()
    elif s1 == '6':
        sear = int(input('price:'))
        try:
            cursor.execute(
                f'select price from  cash_order where price={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  cash_order where price='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('price not found')
        interface()    
    else:
        print('wrong operation')
        interface()


def productcertainview():
    s1 = input('which element to search with:1-product_id  \
        2-brand_id  3-brand_name  4-serial_number   5-date_sold  6-date_received :')
    if s1 == '1':
        sear = int(input('product_id :'))
        try:
            cursor.execute(
                f'select product_id from  product where product_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  product where product_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('product_id not found')
        interface()
    elif s1 == '2':
        sear = int(input('brand_id:'))
        try:
            cursor.execute(
                f'select brand_id from  product where brand_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  product where brand_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('brand_id not found')
        interface()
    elif s1 == '3':
        sear = input('brand_name :')
        try:
            cursor.execute(
                f'select brand_name from  product where brand_name={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  product where brand_name='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('brand_name not found')                  
        interface()
    elif s1 == '4':
        sear = int(input('serial_number:'))
        try:
            cursor.execute(
                f'select serial_number from  product where serial_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  product where serial_number='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('serial_number not found')                  
        interface()
    elif s1 == '5':
        sear = input('date_sold:')
        try:
            cursor.execute(
                f'select date_sold from  product where date_sold={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  product where date_sold='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('date_sold not found')                  
        interface()
    elif s1 == '6':
        sear = input('date_received:')
        try:
            cursor.execute(
                f'select date_received from  product where date_received={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  product where date_received='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('date_received not found')
        interface()    
    else:
        print('wrong operation')
        interface()


def charge_ordercertainview():
    s1 = input('which element to search with:1-chargeoder_id  \
        2-invoice_number  3-brand_name  4-model   5-serial_number  6-price 7-down_Payment:')
    if s1 == '1':
        sear = int(input('chargeoder_id :'))
        try:
            cursor.execute(
                f'select chargeoder_id from  charge_order where chargeoder_id={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  charge_order where chargeoder_id={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('chargeoder_id not found')                  
        interface()
    elif s1 == '2':
        sear = int(input('invoice_number:'))
        try:
            cursor.execute(
                f'select invoice_number from  charge_order where invoice_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f'select * from  charge_order where invoice_number={sear}')
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('invoice_number not found')                  
        interface()
    elif s1 == '3':
        sear = input('brand_name :')
        try:
            cursor.execute(
                f'select brand_name from  charge_order where brand_name={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  charge_order where brand_name='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('brand_name not found')                  
        interface()
    elif s1 == '4':
        sear = input('model:')
        try:
            cursor.execute(
                f'select model from  charge_order where model={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  charge_order where model='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('model not found')
        interface()
    elif s1 == '5':
        sear = int(input('serial_number:'))
        try:
            cursor.execute(
                f'select serial_number from  charge_order where serial_number={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  charge_order where serial_number='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('serial_number not found')
        interface()
    elif s1 == '6':
        sear = int(input('price:'))
        try:
            cursor.execute(
                f'select price from  charge_order where price={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  charge_order where price='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('price not found')                  
        interface()
    elif s1 == '7':
        sear = int(input('down_Payment:'))
        try:
            cursor.execute(
                f'select down_Payment from  charge_order where down_Payment={sear}')
            res1 = cursor.fetchone()
            for i in res1:
                c = i
            if c == sear:
                cursor.execute(
                    f"select * from  charge_order where down_Payment='{sear}'")
                res = cursor.fetchall()
                for i in res:
                    print(i)
        except:
            print('down_Payment not found')
        interface()    
    else:
        print('wrong operation')
        interface()


def viewing_certain_data():
    print('pls select table to view:1-customer 2-supplier 3-Employee 4-orders 5-cash_order 6-product  7-charge_order :')
    tableselect = input('1,2,3,4,5,6,7:')
    if tableselect == '1':
        customerertainciew()
    elif tableselect == '2':
        suppliercertainview()
    elif tableselect == '3':
        Employee_certainview()
    elif tableselect == '4':
        orderscertainsview()
    elif tableselect == '5':
        cash_ordercertainview()
    elif tableselect == '6':
        cash_ordercertainview()
    elif tableselect == '7':
        cash_ordercertainview()
    else:
        print('wrong operation')
        interface()





def modifycustomer():
    selection = input(
        'which element u want to modify:1-first_name 2-last_name 3-address 4-contact_number:')
    if selection == '1':
        id = int(input('customer id to change:'))
        change = input('customer new first_name:')
        cursor.execute(
            f"update  customer set first_name='{change}'   where customer_id={id} ")
        conn.commit()
        try:
            cursor.execute(
            f"select  first_name from customer   where customer_id={id} ")
            res=cursor.fetchone()
            for i in res:
                c=i
            c==change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')    
        
        interface()
    elif selection == '2':
        id = int(input('customer id to change:'))
        change = input('customer new last_name:')
        cursor.execute(
            f"update  customer set last_name='{change}'   where customer_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  last_name from customer   where customer_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()

    elif selection == '3':
        id = int(input('customer id to change:'))
        change = input('customer new address:')
        cursor.execute(
            f"update customer set address='{change}'   where customer_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  address from customer   where customer_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()

    elif selection == '4':
        id = int(input('customer id to change:'))
        change = input('customer new contact_number:')
        cursor.execute(
            f"update customer set contact_number='{change}'   where customer_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  contact_number from customer   where customer_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()    
    else:
        print('wrong operation')
        interface()


def modifyEmployee():
    selection = input(
        'which element u want to modify:1-first_name 2-last_name 3-address 4-contact_number 5-position:')
    if selection == '1':
        id = int(input('cashier id to change:'))
        change = input('new emplyee first_name:')
        cursor.execute(
            f"update Employee set first_name='{change}'   where employee_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  first_name from Employee   where employee_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()

    elif selection == '2':
        id = int(input('cashier id to change:'))
        change = input('new emplyee last_name:')
        cursor.execute(
            f"update Employee set last_name='{change}'   where employee_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  last_name from Employee   where employee_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '3':
        id = int(input('cashier id to change:'))
        change = input('new emplyee address:')
        cursor.execute(
            f"update Employee set address='{change} '  where employee_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  address from Employee   where employee_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '4':
        id = int(input('cashier id to change:'))
        change = input('new emplyee contact_number:')
        cursor.execute(
            f"update Employee set contact_number='{change}'   where employee_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  contact_number from Employee   where employee_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '5':
        id = int(input('cashier id to change:'))
        change = input('new emplyee position:')
        cursor.execute(
            f"update Employee set position='{change}'   where employee_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  position from Employee   where employee_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    else:
        print('wrong operation')
        interface()


def modifysupplier():
    selection = input(
        'which element u want to modify:1-name 2-address 3-contact_number 4-brand_id:')
    if selection == '1':
        id = int(input('emplyee id to change:'))
        change = input('new supplier name:')
        cursor.execute(
            f"update supplier set name='{change}'   where supplier_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  name from supplier   where supplier_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '2':
        id = int(input('emplyee id to change:'))
        change = input('new supplier address:')
        cursor.execute(
            f"update supplier set address='{change}'   where supplier_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  address from supplier   where supplier_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '3':
        id = int(input('emplyee id to change:'))
        change = input('new supplier contact_number:')
        cursor.execute(
            f"update supplier set contact_number='{change}'   where supplier_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  contact_number from supplier   where supplier_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '4':
        id = int(input('emplyee id to change:'))
        change = int(input('new supplier brand_id:'))
        cursor.execute(
            f"update supplier set brand_id='{change}'   where supplier_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  brand_id from supplier   where supplier_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()

    else:
        print('wrong operation')
        interface()


def modifyorders():
    selection = input(
        'which element u want to modify:1-customer_id 2-employee_id 3-invoice_number 4-total_price\
             5-brand_id 6-quantity:')
    if selection == '1':
        id = int(input(' id to change:'))
        change = int(input('new orders  customer_id:'))
        cursor.execute(
            f"update orders set customer_id='{change} '  where order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  customer_id from orders   where order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '2':
        id = int(input(' id to change:'))
        change = int(input('new  orders employee_id:'))
        cursor.execute(
            f"update orders set employee_id='{change} '  where order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  employee_id from orders   where order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '3':
        id = int(input(' id to change:'))
        change = int(input('new orders invoice_number:'))
        cursor.execute(
            f"update orders set invoice_number='{change} '  where order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  invoice_number from orders   where order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '4':
        id = int(input(' id to change:'))
        change = int(input('orders total_price:'))
        cursor.execute(
            f"update orders set total_price='{change}'   where order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  total_price from orders   where order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '5':
        id = int(input(' id to change:'))
        change = int(input('new orders brand_id:'))
        cursor.execute(
            f"update orders set brand_id='{change} '  where order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  brand_id from orders   where order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '6':
        id = int(input(' id to change:'))
        change = int(input('new orders quantity:'))
        cursor.execute(
            f"update orders set quantity='{change} '  where order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  quantity from orders   where order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()    
    else:
        print('wrong operation')
        interface()


def modifycash_order():
    selection = input(
        'which element u want to modify:1-invoice_number 2-serial_number 3-brand_name 4-price')
    if selection == '1':
        id = int(input('cash_order_id to change:'))
        change = int(input('new invoice_number:'))
        cursor.execute(
            f"update cash_order set invoice_number='{change}'   where cash_order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  invoice_number from cash_order   where cash_order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '2':
        id = int(input('cash_order_id to change:'))
        change = int(input('new serial_number:'))
        cursor.execute(
            f"update cash_order set serial_number='{change}'   where cash_order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  serial_number from cash_order   where cash_order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '3':
        id = int(input('cash_order_id to change:'))
        change = input('new brand_name:')
        cursor.execute(
            f"update cash_order set brand_name='{change}'   where cash_order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  brand_name from cash_order   where cash_order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '4':
        id = int(input('cash_order_id to change:'))
        change = int(input('price change:'))
        cursor.execute(
            f"update cash_order set price='{change}'   where cash_order_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  price from cash_order   where cash_order_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    else:
        print('wrong operation')
        interface()


def modifyproduct():
    selection = input(
        'which element u want to modify:1-brand_id 2-serial_number 3-customer_id 4-availability')
    if selection == '1':
        id = int(input('product_id to change:'))
        change = int(input('new brand_id:'))
        cursor.execute(
            f"update product set brand_id='{change}'   where product_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  brand_id from product   where product_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '2':
        id = int(input('product_id to change:'))
        change = int(input('new serial_number:'))
        cursor.execute(
            f"update product set serial_number='{change}'   where product_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  serial_number from product   where product_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '3':
        id = int(input('product_id to change:'))
        change = int(input('new customer_id:'))
        cursor.execute(
            f"update product set customer_id='{change}'   where product_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  customer_id from product   where product_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '4':
        id = int(input('product_id to change:'))
        change = input('availability change:')
        cursor.execute(
            f"update product set availability='{change}'   where product_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  availability from product   where product_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    else:
        print('wrong operation')
        interface()


def modifycharge_order():
    selection = input(
        'which element u want to modify:1-invoice_number 2-serial_number 3-brand_name 4-price 5-down_Payment')
    if selection == '1':
        id = int(input('chargeoder_id to change:'))
        change = int(input('new invoice_number:'))
        cursor.execute(
            f"update charge_order set invoice_number='{change}'   where chargeoder_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  invoice_number from charge_order   where chargeoder_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '2':
        id = int(input('chargeoder_id to change:'))
        change = int(input('new serial_number:'))
        cursor.execute(
            f"update charge_order set serial_number='{change}'   where chargeoder_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  serial_number from charge_order   where chargeoder_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '3':
        id = int(input('chargeoder_id to change:'))
        change = input('new brand_name:')
        cursor.execute(
            f"update charge_order set brand_name='{change}'   where chargeoder_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  brand_name from charge_order   where chargeoder_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '4':
        id = int(input('chargeoder_id to change:'))
        change = int(input('price change:'))
        cursor.execute(
            f"update charge_order set price='{change}'   where chargeoder_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  price from charge_order   where chargeoder_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()
    elif selection == '5':
        id = int(input('chargeoder_id to change:'))
        change = int(input('down_Payment change:'))
        cursor.execute(
            f"update charge_order set down_Payment='{change}'   where chargeoder_id={id} ")
        conn.commit()
        try:
            cursor.execute(
                f"select  down_Payment from charge_order   where chargeoder_id={id} ")
            res = cursor.fetchone()
            for i in res:
                c = i
            c == change
            print('successfully modified')
        except:
            print('not modified prbably not existent id')
        interface()    
    else:
        print('wrong operation')
        interface()


def modify():
    print('pls select table to modify:1-customer 2-supplier 3-Employee 4-orders 5-cash_order 6-product  7-charge_order  :')
    tableselect = input('1,2,3,4,5,6,7:')
    if tableselect == '1':
        modifycustomer()
    elif tableselect == '2':
        modifysupplier()
    elif tableselect == '3':
        modifyEmployee()
    elif tableselect == '4':
        modifyorders()
    elif tableselect == '5':
        modifycash_order()
    elif tableselect == '6':
        modifyproduct()
    elif tableselect == '7':
        modifycharge_order()
    else:
        print('wrong operation')
        interface()

def interface():
    print('-----HELLO TO DATABASE-----')
    print('1-adding data       2-viewing data  \
        3-viewing certain data  4-modify data   5-exit  ')
    selection = input('1 ,2 ,3 ,4 ,5:  ')

    if selection == "1":
        add_data()
    elif selection == "2":
        viewing_data()
    elif selection == "3":
        viewing_certain_data()
    elif selection == "4":
        modify()
    elif selection == '5':
        exita = input('do u want to exit ? 1-exit 2-continue:')
        if exita == '2':
            interface()
        else:
            exit()
    else:
        print('wrong operation')
        exita = input('do u want to exit:1-exit 2-continue:')
        if exita == '2':
            interface()
        else:
            exit()

interface()
