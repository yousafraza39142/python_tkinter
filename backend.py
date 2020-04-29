import sqlite3


def connect():
    conn=sqlite3.connect("back.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY,Title text,Author text,Year  integer,ISBN integer)")
    conn.commit()
    conn.close()

def insert(Title,Author,Year,ISBN):
    conn=sqlite3.connect("back.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(Title,Author,Year,ISBN))
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect("back.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(Title="",Author="",Year="",ISBN=""):
    conn=sqlite3.connect("back.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE Title=? OR Author=? OR Year=? OR ISBN=?",(Title,Author,Year,ISBN))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(ID):
    conn=sqlite3.connect("back.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE ID=?",(ID,))
    conn.commit()
    conn.close()


def update(ID,Title,Author,Year,ISBN):
    conn=sqlite3.connect("back.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET Title=?,Author=?,Year=?,ISBN=? WHERE ID=?",(Title,Author,Year,ISBN,ID))
    conn.commit()
    conn.close()



connect()
#insert("FOOD DIARY","MKF",1983,33344123)
#delete(2)

#print(search(Author="J.M"))
#update(2,"JERRY","LAWLER",1244,4523462)
#delete(1)
#delete(2)
#print(view())
