# You need install pymongo, tabula, and pandas libraries
import pymongo
import tabula
import pandas as pd

import course2db

# 1. Input your MongdoDB's USERNAME and PASSWORD
converter = course2db.Converter(
    username = 'markkim1',
    password = 'Mrlaalstn12'
)

# 2. Set the client and make a db and a collection
converter.set_collection(db_name='test', collection_name='courses')

# 3. convert the pdf file to make a table - Please write the path of the course list pdf file
converter.pdf2csv(file_url='./sk-sbu sp23 course list_20230314.pdf')

# 4. Add course info to your database
converter.courses2db(reset_db=True) 



