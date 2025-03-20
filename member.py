#PYTHON MODULE : MEMBER 
import mysql.connector 
from mysql.connector import errorcode 
from datetime import date, datetime, timedelta 
from mysql.connector import (connection) 
import os 
def clrscreen(): 
    print('\n' *5) 
def display(): 
    try: 
        os.system('cls') 
        cnx = connection.MySQLConnection(user='root', password='Tejas#04',host='localhost', 
        database='My_library') 
        Cursor = cnx.cursor() 
        query = ("SELECT * FROM Member") 
        Cursor.execute(query) 
        for (Mno,Mname,MOB,DOP,ADR) in Cursor: 
            print("===========================================================") 
            print("Member Code : ",Mno) 
            print("Member Name : ",Mname) 
            print("Mobile No.of Member : ",MOB) 
            print("Date of Membership : ",DOP) 
            print("Address : ",ADR) 
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
    #    cnx.close() 
 
def insertMember(): 
    try: 
        cnx = connection.MySQLConnection(user='root',password='Tejas#04',host='localhost', 
        database='My_library') 
        Cursor = cnx.cursor() 
        mno=input("Enter Member Code : ") 
        mname=input("Enter Member Name : ") 
        mob=input("Enter Member Mobile No. : ") 
        print("Enter Date of Membership (Date/MOnth and Year seperately: ") 
        DD=int(input("Enter Date : ")) 
        MM=int(input("Enter Month : ")) 
        YY=int(input("Enter Year : ")) 
        addr=input("Enter Member Adress : ") 
        Qry = ("INSERT INTO Member VALUES (%s, %s, %s, %s, %s)") 
        data = (mno,mname,mob,date(YY,MM,DD),addr) 
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
 
def deleteMember(): 
    try: 
        cnx = connection.MySQLConnection(user='root',password='Tejas#04',host='localhost', 
        database='My_library') 
        Cursor = cnx.cursor() 
        mno=input("Enter Member Code to be deleted from the My_library : ") 
        Qry =("""DELETE FROM Member WHERE MNO = %s""") 
        del_rec=(mno,) 
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
 
def SearchMember(): 
    try: 
        cnx = connection.MySQLConnection(user='root',password='Tejas#04',host='localhost', 
        database='My_library') 
        Cursor = cnx.cursor() 
        mnm=input("Enter the Member Code to be Searched : ") 
        query = ("SELECT * FROM Member where mno = %s") 
        rec_srch=(mnm,) 
        Cursor.execute(query,rec_srch) 
        Rec_count=0 
        for (Mno,Mname,MOB,DOP,ADR) in Cursor: 
            print("===========================================================") 
            print("Member Code : ",Mno) 
            print("Member Name : ",Mname) 
            print("Mobile No.of Member : ",MOB) 
            print("Date of Membership : ",DOP) 
            print("Address : ",ADR) 
            print("===========================================================") 
            if Rec_count%2==0: 
                input("Press any key to continue") 
                clrscreen() 
        print(Rec_count, "Record(s) found") 
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
 
def UpdateMember(): 
    try: 
        cnx = mysql.connector.connect(user='root', password='Tejas#04',host='localhost',database="my_library") 
        Cursor = cnx.cursor() 
        mno=input("Enter the Member Code to be Updated : ") 
        print("Enter new data ") 
        mname=input("Enter Member Name : ") 
        mob=input("Enter Member Mobile No. : ") 
        print("Enter Date of Membership (Date/MOnth and Year seperately: ") 
        DD=int(input("Enter Date : ")) 
        MM=int(input("Enter Month : ")) 
        YY=int(input("Enter Year : ")) 
        addr=input("Enter Member Adress : ") 
        Qry = ("UPDATE member SET mname=%s,mob=%s,dop=%s,adr=%s WHERE mno=%s") 
        data = (mname,mob,date(YY,MM,DD),addr,mno) 
        Cursor.execute(Qry,data) 
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
