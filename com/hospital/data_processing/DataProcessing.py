from builtins import ValueError


from com.hospital.data_processing.DbConnection import getConnection, closeConnection


def fetch_infection_data():
    query = "select * from hospital_infection where hospital_infection.measure_id LIKE '%_SIR' and score!=0  order by `hospital _name`, measure_id ASC;"
    
    try:
        
        cursor, db = getConnection()
        print("Connection Established")
        
        cursor.execute("TRUNCATE TABLE processed_infection_data;")
        db.commit()
        
        print("Updating infection data into: processed_infection_data Table ")
        cursor.execute(query);
        
        print("Processing #",cursor.rowcount, " Records...")

        infectionsData = ''
        qSQLresults = cursor.fetchall()
        for row in qSQLresults:
            id1 = row[0]
            city = row[2] 
            city1 = row[10] 
            city2 = row[12] 
            if row[10] == "HAI_1_SIR":
                infectionsData = 'CLABSI'
            elif row[10] == "HAI_2_SIR":
                infectionsData = 'CAUTI'
            elif row[10] == "HAI_3_SIR":
                infectionsData = 'SSI: Colon'
            elif row[10] == "HAI_4_SIR":
                infectionsData = 'SSI: Hysterectomy'
            elif row[10] == "HAI_5_SIR":
                infectionsData = 'MSRA'
            else :
                infectionsData = 'Intestinal Infections'
           
             
            
            cursor.execute('''INSERT into processed_infection_data (infection_id,hospital_name,measure_id,score, infection_name)
                  values (%s, %s,%s, %s,%s)''',
                  (id1, city, city1, city2, infectionsData))

            # Commit your changes in the database
            
            
    except ValueError:
        print('Error in inserting records.')
 
    finally:
        
        db.commit()
        print("Records updated successfully!")
        print("Closing connection")
        closeConnection(cursor, db)


def main():
    
    fetch_infection_data()
 
if __name__ == '__main__':
    main()
