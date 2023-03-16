# You need install pymongo, tabula, and pandas libraries
import pymongo
import tabula
import pandas as pd

import course2db

# 1. Input your MongdoDB's USERNAME and PASSWORD
converter = course2db.Converter(
    username = 'YOUR_ID',
    password = 'YOUR_PASSWORD'
)

# 2. Set the client and make a db and a collection
converter.set_collection(db_name='DATABASE_NAME', collection_name='COLLECTION_NAME')

# 3. convert the pdf file to make a table - Please write the path of the course list pdf file
converter.pdf2csv(file_url='PDF_FILE_PATH')

# 4. Add course info to your database
converter.courses2db(reset_db=True) 



