import pickle
import json
import sqlite3

con = sqlite3.connect("db.sqlite")


def write_db(name, datetime, save):
    cur = con.cursor()
    res = cur.execute(
        """SELECT name FROM Saving
            WHERE name = ?""",
        (name),
    ).fetchall()
    cur = con.cursor()
    if res:
        cur.execute(
            """UPDATE Saving
                SET datetime = ?,
                    save = ?
                WHERE name = ?""",
            (str(datetime)[:19], pickle.dumps(save), name),
        )
        con.commit()
    else:
        cur.execute(
            """INSERT INTO Saving (name, datetime, save) VALUES (?, ?, ?)""",
            (name, str(datetime)[:19], pickle.dumps(save)),
        )
        con.commit()


def read_db():
    cur = con.cursor()
    result = cur.execute(
        """SELECT name, datetime, save FROM Saving""",
    ).fetchall()
    return [(i[0], i[1], pickle.loads(i[2])) for i in result]


def write_txt(*args, **kwargs):
    sl = read_txt()
    with open("records.txt", "w", encoding="utf8") as f:
        for i in args:
            sl[i] += 1
        for k, v in kwargs.items():
            if k in sl["records"] and v < sl["records"][k]:
                sl["records"][k] = v
        f.write(json.dumps(sl))


def read_txt():
    with open("records.txt", encoding="utf8") as f:
        return json.loads(f.read())
