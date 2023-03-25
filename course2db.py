import pymongo
import tabula
import pandas as pd

class Converter:
    client = ''
    collection = ''
    db = ''
    df = ''
    category = ''
    semester = []

    def __init__(self, username, password):
        self.client = pymongo.MongoClient('YOUR_DB_ADDRESS')

        
        

    def set_collection(self, db_name, collection_name, semester):
        # self.collection = self.client.test.courses
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.semester.append(semester)


    def pdf2csv(self, file_url):
        tabula.convert_into(file_url, "output.csv", output_format="csv", pages='all')
        self.df = pd.read_csv('./output.csv')
        self.category = self.df.columns
        # print(self.category)
        # self.category = pd.DataFrame(['classNbr', 'subj', 'crs', 'courseTitle', 'sbc', 'cmp', 'sctn', 'credits', 'day', 'startTime', 'endTime', 'room', 'instructor'])
    
    def courses2db(self, reset_db=True): 
        result = True
        if (reset_db):
            self.collection.delete_many({})
        try:
            for i in range(len(self.df)):
                self.collection.insert_one({
                    'semester': self.semester,
                    self.category[0]: self.df[self.category[0]].iloc[i],
                    self.category[1]: self.df[self.category[1]].iloc[i],
                    self.category[2]: self.df[self.category[2]].iloc[i],
                    self.category[3]: self.df[self.category[3]].iloc[i],
                    self.category[4]: self.df[self.category[4]].iloc[i],
                    self.category[5]: self.df[self.category[5]].iloc[i],
                    self.category[6]: self.df[self.category[6]].iloc[i],
                    self.category[7]: self.df[self.category[7]].iloc[i],
                    self.category[8]: self.df[self.category[8]].iloc[i],
                    self.category[9]: self.df[self.category[9]].iloc[i],
                    self.category[10]: self.df[self.category[10]].iloc[i],
                    self.category[11]: self.df[self.category[11]].iloc[i],
                    self.category[12]: self.df[self.category[12]].iloc[i],
                    'likes': [],
                    'reviews': []

                })
        except:
            result = False
        if result:
            print('The courses info succesfully added to your DB!')
        else:
            print('Sorry! Fail to add your courses info to your DB...')    