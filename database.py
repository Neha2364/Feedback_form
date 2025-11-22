import sqlite3

connection = sqlite3.connect("feedback.db")
cursor = connection.cursor()

cmd = """
CREATE TABLE IF NOT EXISTS FEEDBACK(
        id integer primary key,
        fullname text not null,
        usn varchar(10) not null,
        contact varchar(10) not null,
        email text not null,
        message text not null
        )
"""
cursor.execute(cmd)
connection.commit()
cmd="INSERT INTO FEEDBACK(fullname,usn,contact,email,message)values(?,?,?,?,?)"
#cursor.execute(cmd,('Neha','AD023','8088308477','neha.23ad023@sode-edu.in','learning devops'))
cursor.execute(cmd,('Niha','CS023','8078308477','niha.23cs023@sode-edu.in','learning python'))
connection.commit()
f=cursor.execute("SELECT * FROM FEEDBACK").fetchall()
print(f)
connection.close()