import mysql.connector 

mycon = mysql.connector.connect(host="localhost", user = "root", passwd = "Deepak@774") #Connecting To MySQL Server And Creating a Connecter Object

if mycon.is_connected():    #Is Connected Method To Check the Connection With MySQL Server 
    print("*****PHONEBOOK INTIALISED*****")

mycursor=mycon.cursor()     #Creating a cursor Object To Manipulate Our Database And Tables
mycursor.execute("create database if not exists MYDB") #Creating a Database With Execute method Of Cursor Object To Give The SQL commands To Be Executed
mycursor.execute("use MYDB") #Using The Database "MYDB" If Already Exists
mycon.commit() 

mycursor.execute("CREATE TABLE if not exists Persons (PersonID int,FirstName varchar(255),LastName varchar(255),ContactNum char(10),City varchar(255))") #creating required table
mycon.commit()    #COMMITs statement to the MySQL server, committing the current transaction

while (True): #Active Loop Till User Exits 
    print("1=New Contact")
    print("2=Display a Contact")
    print("3=Delete  Contact")                     
    print("4=Display No. of Contacts")
    print("5=Exit")
    
    ch=int(input("Enter your choice:"))
    
    if(ch==1):
        #Inserting a new Entry
        print("\nEnter The Mandatory Information Asked For: ")
        PersonID = int(input("Enter The Person ID:"))
        FirstName = str( input("Fisrt Name Of The Person:"))
        LastName = str(input("Last Name Of The Person:"))
        Contact = str(input("Contact Number of The Person:"))
        City = str(input("City Of the Person: " ))
        mycursor.execute("insert into persons values('"+str(PersonID)+"','"+FirstName+"','"+LastName+"','"+Contact+"','"+City+"')")
        mycon.commit()
    
    elif(ch == 2):
        #Displaying Entry
        ch = int(input("\nEnter 1 To Display Each Entry or 2 To Display a Specific Entry"))
        
        if(ch == 1): #To Display Each Entry
            mycursor.execute("SELECT * FROM persons")
            for i in mycursor:  #Cursor Contains the tuples Of Row
                print(f"\nID: {i[0]} \nName: {i[1]} {i[2]} \nContact No.: {i[3]} \nCity: {i[4]}\n")    
            mycon.commit()
            
        elif(ch == 2): #To Display a Specific Entry
            FirstName = str(input("Enter The First Name of The Person :"))    
            mycursor.execute("SELECT * FROM persons where FirstName='"+FirstName+"' ")    
            for i in mycursor:
                print(f"\nID:{i[0]} \nName: {i[1]} {i[2]} \nContact No.: {i[3]} \nCity: {i[4]}\n") 
            else:
                print("\nContact Info Not Found!\n")    
        else:
            print("Invalid Choice !!") 
            pass
        
    elif(ch == 3):
        # Deleting An Entry
        FirstName = str(input("Enter The First Name of The Person :"))    
        mycursor.execute("DELETE FROM persons where FirstName='"+FirstName+"' ")  
        mycon.commit()
        
    elif(ch==4):
        #Counting The Number Of Entries In Person Table
        mycursor.execute("SELECT COUNT(*) FROM Persons")
        print(f"\nNumber of Entries in Ur PhoneBook: {mycursor.fetchone()[0]}\n")
    
    else:
        print("*******PHONEBOOK TERMINATED*******")
        mycon.close()
        break
        
        
            


