import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cmd = """
CREATE TABLE IF NOT EXISTS STUDENT(
        
        fullname text not null,
        usn varchar(10) not null,
        sem integer not null,
        cgpa integer not null

        )
"""
cursor.execute(cmd)
connection.commit()
cmd="INSERT INTO STUDENT(fullname,usn,sem,cgpa)values(?,?,?,?)"
#cursor.execute(cmd,('Neha','AD023',5,9))
#cursor.execute(cmd,('Niha','CS023',5,8))
cursor.execute(cmd,('Nikitha','CS023',5,8))

connection.commit()
f=cursor.execute("SELECT * FROM STUDENT").fetchall()
print(f)
r=cursor.execute("select * from student where fullname=?",('Nikitha',)).fetchall()
print(r)
connection.close()