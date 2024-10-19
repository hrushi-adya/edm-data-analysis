import logging
from contextlib import closing
import mysql
import mysql.connector
from benchmark_util import create_images_list

def get_data():
    logging.info("setting up db configuration")
    db_config = {
        'user': '',
        'password': '',
        'host': 'localhost',
        'database': 'articles'
    }

    conn = mysql.connector.connect(**db_config)

    logging.info(conn)
    logging.info("database configuration setup successful")

    logging.info("executing query with connection.cursor to rerieve records from database")    
    with closing(conn.cursor()) as c:

        c.execute("SELECT content from articles")
        data_rows = list(c.fetchall())
        data_rows = [str(data) for data in data_rows]

        # print("PRITING DATA ROWS:" )
        # for data in data_rows:
        #     print(data)

        c.execute("SELECT images from images")
        images_rows = list(c.fetchall())  
        images_list = create_images_list(images_rows)
        final_img_list = [item for sublist in images_list for item in sublist]

        for img in images_list:
            print(img)
    conn.close()

    return data_rows, final_img_list
