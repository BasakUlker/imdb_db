import sqlite3
def insertName(name):

    with sqlite3.connect('vt.sqlite') as vt:

        im = vt.cursor()
    
        im.execute("""CREATE TABLE IF NOT EXISTS imdblist4 (topratedtvshows)""")

        im.execute("""INSERT INTO imdblist4 VALUES (?)""",[name])
        vt.commit()
        im.execute("SELECT * FROM imdblist4")
        al = im.fetchall()

        for i in al:
            print(i)
        im.close()

