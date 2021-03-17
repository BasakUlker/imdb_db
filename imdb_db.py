import sqlite3
import os
def insertName(name,x):

    with sqlite3.connect('imdb.sqlite') as imdb:

        im = imdb.cursor()
    
        im.execute("""CREATE TABLE IF NOT EXISTS imdblist (topratedtvshows)""")

        if not os.path.exists("imdb.sqlite"):

            im.execute("""INSERT INTO imdblist VALUES (?)""",[name])
            imdb.commit()
        if(x==1):
            im.execute("SELECT * FROM imdblist")
            al = im.fetchall()
            j=1
            for i in al:
                print(j,i)
                j+=1
            my_list=[]
            while(1==1):

                j = int(input("Begendiginiz dizi, film ya da tv showlarini listenize eklemek icin numarasini girin."))
                im.execute("SELECT * FROM imdblist LIMIT {},1".format(j-1))
                al=im.fetchall()
                my_list.append(al)
                print(my_list)
                o= input("Secmeye devam etmek icin: 'C' ya da 'c'ye basin\nCikmak icin: 'Q' ya da 'q' ya basin")
                if(o=="C" or o=="c"):
                    continue
                elif(o=="Q" or o=="q"):
                    break
        im.close()
        return imdb



