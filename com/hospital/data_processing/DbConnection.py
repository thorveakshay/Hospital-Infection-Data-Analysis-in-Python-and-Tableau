from builtins import ValueError

import pymysql

db = pymysql.connect(host='localhost',
                             user='root',
                             port=3306,
                             passwd='1234',
                             db='hospital_db'
                             )

def  getConnection():
    try:
        cursor = db.cursor()

    except ValueError:
        print('Error:')
 
    finally:
        return cursor,db;
        
def  closeConnection(cursor,db):
    cursor.close()
    db.close();