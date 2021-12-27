# ===============================================================================
#  DB - Python
# ===============================================================================
import psycopg2
import os
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn=None
    try:
        # read connection parameters
        params = config()
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        return [conn,cur]
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def disconnect(conn,cur):
    # close the communication with the PostgreSQL
    cur.close()
    if conn is not None:
        conn.close()
        print('Database connection closed.')

if __name__ == '__main__':
    arr = connect()
    conn=arr[0]
    cur=arr[1]
    while(1):
        print("")
        print("1 - number of distinct cities whose name starts with 'L' ")
        print("2 - distinct countries that hosted the FIFA World Cup ")
        print("3 - various types of tournaments played by Greece")
        print("4 - the country with the most wins in shootouts")
        print("5 - exit")
        ans = input("select an option:")
        lines=""
        if ans=="1":
            lines = open("dbm.q1" , "r").read()
            cur.execute(lines)
            x=cur.fetchall()
            for row in x:
                for el in row:
                    print(str(el) + "\t",end="")
                print("")
        elif ans=="2":
            lines = open("dbm.q2", "r").read()
            cur.execute(lines)
            x=cur.fetchall()
            for row in x:
                for el in row:
                    print(str(el) + "\t",end="")
                print("")
        elif ans=="3":
            lines = open("dbm.q3").read()
            cur.execute(lines)
            x=cur.fetchall()
            for row in x:
                for el in row:
                    print(str(el) + "\t",end="")
                print("")
        elif ans=="4":
            lines = open("dbm.q4").read()
            cur.execute(lines)
            x=cur.fetchall()
            for row in x:
                for el in row:
                    print(str(el) + "\t",end="")
                print("")
        elif ans=="5":
            break
        else:
            print("Unvalid input!")
    disconnect(conn,cur)








