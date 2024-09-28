import sqlite3
def create_db():
    con = sqlite3.connect(database='rms.db')
    cursr = con.cursor()
    cursr.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text,duration text , charges text, description text)")
    con.commit()

    cursr.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()

    cursr.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text,name text , course text, mark_obt text,full_mark,per text)")
    con.commit()

    con.close()  # Connection Close

create_db()