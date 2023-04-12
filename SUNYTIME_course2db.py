# You need to install pymongo, tabula, and pandas libraries
import pymongo
import tabula
import pandas as pd

import course2db

# 1. Input your MongdoDB's USERNAME and PASSWORD
converter = course2db.Converter(url='YOUR_DB_ADDRESS')

# 2. Set the client and make a db and a collection
converter.set_collection(db_name='DB_NAME', collection_name='COLLECTION_NAME', semester='SEMESTER')

# 3. convert the pdf file to make a table - Please write the path of the course list pdf file
converter.pdf2csv(file_url='PDF_FILE_PATH')

# 4. Add course info to your database 
# reset_db is adding course info after reset the existing db
# Warning - if you choose 'reset_db' parameter to True, the likes and reviews part will be reset!
converter.courses2db(reset_db=True) 



