from pickle import dumps, loads
import sqlite3

con = sqlite3.connect("db.sqlite")


def write_db(name, datetime, save):
    cur = con.cursor()
    cur.execute(
        """INSERT INTO Saving (name, datetime, save) VALUES (?, ?, ?)""",
        (name, str(datetime)[:19], dumps(save)),
    )
    con.commit()


def read_db():
    cur = con.cursor()
    result = cur.execute(
        """SELECT name, datetime, save FROM Saving""",
    ).fetchall()
    return [(i[0], i[1], loads(i[2])) for i in result]
