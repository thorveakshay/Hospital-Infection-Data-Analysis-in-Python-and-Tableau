from builtins import ValueError


from com.hospital.data_processing.DbConnection import getConnection, closeConnection


def fetch_infection_data():
    query = "select * from hospital_survey where HCAHPS_measure_id='H_STAR_RATING' and survey_rating not in (0,10)  order by `hospital_name` ASC;"
    
    try:
        
        cursor, db = getConnection()
        print("Connection Established")
        
        cursor.execute("TRUNCATE TABLE survey_processed_data;")
        db.commit()
        
        print("Updating infection data into: survey_processed_data Table ")
        cursor.execute(query);
        
        print("Processing #",cursor.rowcount, " Records...")

        qSQLresults = cursor.fetchall()
        for row in qSQLresults:
            id = row[0]
            hospitalName = row[2] 
            measureId = row[9] 
            surveyRating = row[12] 
            print("survey rating #",surveyRating)
            
            cursor.execute('''INSERT into survey_processed_data (`survey_process_id`,`hospital_name`,`HCAHPS_measure_id`,`survey_rating`)
                  values (%s,%s,%s,%s)''',
                  (id, hospitalName, measureId,surveyRating))

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
