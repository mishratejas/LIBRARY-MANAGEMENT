# PYTHON MODULE : BOOK 
import mysql.connector 
from mysql.connector import errorcode 
from datetime import date, datetime, timedelta 
from mysql.connector import (connection) 
import os 
import platform 
def clrscreen(): 
    if platform.system()=="Windows": 
        print(os.system("cls")) 
def display(): 
    try: 
        os.system('cls') 
        cnx = connection.MySQLConnection(user='root',   
        password='Tejas#04',host='localhost',database='My_library') 
        Cursor = cnx.cursor() 
        query = ("SELECT * FROM BookRecord") 
        Cursor.execute(query) 
        for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in Cursor: 
            print("===========================================================") 
            print("Book Code : ",Bno) 
            print("Book Name : ",Bname) 
            print("Author of Book : ",Author) 
            print("Price of Book : ",price) 
            print("Publisher : ",publ) 
            print("Total Quantity in Hand : ",qty) 
            print("Purchased On : ",d_o_purchase) 
            print("===========================================================") 
        Cursor.close() 
        cnx.close() 
        print("You have done it!!!!!!") 
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
            print("Something is wrong with your user name or password") 
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
            print("Database does not exist") 
        else: 
            print(err) 
    #else: 
    #cnx.close() 
def insertData(): 
    try: 
        cnx = connection.MySQLConnection(user='root',password='Tejas#04',host='localhost', 
        database='My_library') 
        Cursor = cnx.cursor() 
        bno=input("Enter Book Code : ") 
        bname=input("Enter Book Name : ") 
        Auth=input("Enter Book Author's Name : ") 
        price=int(input("Enter Book Price : ")) 
        publ=input("Enter Publisher of Book : ") 
        qty=int(input("Enter Quantity purchased : ")) 
        print("Enter Date of Purchase (Date/MOnth and Year seperately: ") 
        DD=int(input("Enter Date : ")) 
        MM=int(input("Enter Month : ")) 
        YY=int(input("Enter Year : ")) 
        Qry = ("INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s, %s, %s)") 
        data = (bno,bname,Auth,price,publ,qty,date(YY,MM,DD)) 
        Cursor.execute(Qry,data) 
        # Make sure data is committed to the database 
        cnx.commit() 
        Cursor.close() 
        cnx.close() 
        print("Record Inserted..............") 
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
            print("Something is wrong with your user name or password") 
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
            print("Database does not exist") 
        else: 
            print(err) 
        #cnx.close() 
def deleteBook(): 
    try: 
        cnx = connection.MySQLConnection(user='root',password='Tejas#04',host='localhost', 
        database='My_library') 
        Cursor = cnx.cursor() 
        bno=input("Enter Book Code of Book to be deleted from the My_library : ") 
        Qry =("""DELETE FROM BookRecord WHERE BNO = %s""") 
        del_rec=(bno,) 
        Cursor.execute(Qry,del_rec) 
        # Make sure data is committed to the database 
        cnx.commit() 
        Cursor.close() 
        cnx.close() 
        print(Cursor.rowcount,"Record(s) Deleted Successfully.............") 
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
            print("Something is wrong with your user name or password") 
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
            print("Database does not exist") 
        else: 
            print(err) 
        #cnx.close() 
def SearchBookRec(): 
    try: 
        cnx = connection.MySQLConnection(user='root',password='Tejas#04',host='localhost', 
        database='My_library') 
        Cursor = cnx.cursor() 
        bno=input("Enter Book No to be Searched from the My_library : ") 
        query = ("SELECT * FROM BookRecord where BNo = %s ") 
        rec_srch=(bno,) 
        Cursor.execute(query,rec_srch) 
        Rec_count=0 
        for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in Cursor: 
            Rec_count+=1 
            print("===========================================================") 
            print("Book Code : ",Bno) 
            print("Book Name : ",Bname) 
            print("Author of Book : ",Author) 
            print("Price of Book : ",price) 
            print("Publisher : ",publ) 
            print("Total Quantity in Hand : ",qty) 
            print("Purchased On : ",d_o_purchase) 
            print("===========================================================") 
            if Rec_count%2==0: 
                input("Press any key to continue") 
                clrscreen() 
        print(Rec_count, "Record(s) found") 
        # Make sure data is committed to the database 
        cnx.commit() 
        Cursor.close() 
        cnx.close() 
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
            print("Something is wrong with your user name or password") 
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
            print("Database does not exist") 
        else: 
            print(err) 
        #cnx.close() 
def UpdateBook(): 
    try: 
        cnx = mysql.connector.connect(host="localhost", user="root", password="Tejas#04",    
        database="library") 
        Cursor = cnx.cursor() 
        bno=input("Enter Book Code of Book to be Updated from the My_library : ") 
        #query = ("SELECT * FROM BookRecord where BNo = %s ") 
        #rec_srch=(bno,) 
        print("Enter new data ") 
        bname=input("Enter Book Name : ") 
        Auth=input("Enter Book Author's Name : ") 
        price=int(input("Enter Book Price : ")) 
        publ=input("Enter Publisher of Book : ") 
        qty=int(input("Enter Quantity purchased : ")) 
        print("Enter Date of Purchase (Date/MOnth and Year seperately: ") 
        DD=int(input("Enter Date : ")) 
        MM=int(input("Enter Month : ")) 
        YY=int(input("Enter Year : ")) 
        Qry = ("UPDATE BookRecord SET bname=%s,Author=%s,price=%s,publisher=%s,qty=%s,d_o_purchase=%s WHERE BNO=%s") 
        data = (bname,Auth,price,publ,qty,date(YY,MM,DD),bno) 
        Cursor.execute(Qry,data) 
        # Make sure data is committed to the database''' 
        cnx.commit() 
        Cursor.close() 
        cnx.close() 
        print(Cursor.rowcount,"Record(s) Updated Successfully.............") 
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
            print("Something is wrong with your user name or password") 
        elif err.errno == errorcode.ER_BAD_DB_ERROR: 
            print("Database does not exist") 
        else: 
            print(err) 
        #cnx.close() 
