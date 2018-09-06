#ASSIGNMENT- DATABASES USING PYTHON

#Q.1- Write a python script to create a databse of students named Students.
import sqlite3
con=sqlite3.connect('Students.db')
print("connection is successful")
con.close()

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type       //COMBINED
import sqlite3
con=sqlite3.connect('Students.db')
cursor = con.cursor()
query = 'create table student_marks(name varchar(10),marks int(3))'
cursor.execute(query)
con.commit()
for i in range(1,11):
    names=input("enter name")
    m=int(input("enter marks"))
    cursor.execute("insert into student_marks values(?, ?);",(names,m))
con.commit()    
print("inserted 10 rows successfully")


#Q.4- Print the names of all the students who scored more than 80 marks.
import sqlite3
con=sqlite3.connect('Students.db')
cursor = con.cursor()
query = 'select * from Student_marks where marks>80'
cursor.execute(query)
data = cursor.fetchall()
for row in data:
        print('name: {}, marks: {}'\
             .format(row[0], row[1]))
    
cursor.close()
con.close()
print('DONE!!')
