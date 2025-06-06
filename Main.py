import json
class nocourse(Exception):
    def __init__(self):
        print("Not a valid course")
class notfound(Exception):
    def __init__(self):
        print("No Student found")
class nochoice(Exception):
    def __init__(self):
        print("Not a valid choice")
import pymysql
con=pymysql.connect(host="localhost",user="root",password="root@123",database="Student")
cur=con.cursor()
class Registration:
    def register(self):
        try:
            print("Enter details for registration")
            id=int(input("Enter Student ID:"))
            nm=input("Enter Name:")
            l=['CSE','AIDS','CSM','MECH','ECE','EEE','IT','ASE']
            for i in range(1,len(l)+1):
                print(f"{i} {l[i-1]}")
            c=int(input("Choose your course in the number format:"))
            if c>len(l) or c<1:
                raise nocourse
            else:
                co=l[c-1]
            dob=tuple(input("Enter Date of birth in the format of dd-mm-yyyy").split("-"))
            db=str(dob)
            street = input("Enter your street address: ")
            city = input("Enter your city: ")
            state = input("Enter your state: ")
            pincode = input("Enter your pincode: ")
            ad = {
            'street': street,
            'city': city,
            'state': state,
            'pincode': pincode
            }
            adm=input("Are you admin? true or false").strip().lower()=="true"
        except nocourse as e:
            print(end="")
        except Exception as e:
            print(e)
        sql="insert into register values(%s,%s,%s,%s,%s,%s)"
        vals=(id,nm,co,db,json.dumps(ad),adm)
        cur.execute(sql,vals)
        print("Inserted Successfully")
    def printdetails(self):
        sql="select * from register"
        cur.execute(sql)
        res=cur.fetchall()
        for i in res:
            print(i)
class Student(Registration):
    def getStudent(self):
        try:
            id=int(input("Enter Student id to get details:"))
            sql=f"select * from register where id={id}"
            cur.execute(sql)
            res=cur.fetchall()
            if not res:
                raise notfound
            for i in res:
                print(i)
        except notfound as e:
            print(end="")
        except Exception as e:
            print(e)
    def updStudentnm(self):
        try:
            id = int(input("Enter Student id to update:"))
            sql = f"select * from register where id={id}"
            cur.execute(sql)
            res = cur.fetchall()
            if not res:
                raise notfound
            nm = input("Enter Student Correct name to update:")
            sql = "update register set name = %s where id = %s"
            cur.execute(sql, (nm, id))
            print("Student name updated successfully!")
        except notfound as e:
            print(end="")
        except Exception as e:
            print("Error:", e)
    def dltStudent(self):
        try:
            id = int(input("Enter Student id to delete:"))
            sql = f"delete from register where id={id}"
            cur.execute(sql)
            if cur.rowcount == 0:
                print("No student found to delete.")
            else:
                print("Deleted")
        except notfound as e:
            print(end="")
        except Exception as e:
            print("Error:", e)
a=input("Want to perform an action?yes or no").lower()
while(a=='yes'):
    print("Choose operation to be performed:")
    print("1)Register\n2)Print Details\n3)Get Student Details\n4)Update Student Name\n5)Delete Student Details")
    b=int(input())
    try:
        if b<1 or b>5:
            raise nochoice
        s=Student()
        match(b):
            case 1:
                s.register()
            case 2:
                s.printdetails()
            case 3:
                s.getStudent()
            case 4:
                s.updStudentnm()
            case 5:
                s.dltStudent()
    except nochoice as e:
        pass
    a = input("Want to perform an action?yes or no").lower()
con.commit()
con.close()
