import pymongo
import tabula
import pandas as pd

class Converter:
    client = ''
    collection = ''
    db = ''
    df = ''
    category = ''
    names = []
    semester = ''

    def __init__(self, url):
        self.client = pymongo.MongoClient(url)

        

    def set_collection(self, db_name, collection_name, semester):
        # self.collection = self.client.test.courses
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
        self.semester = semester


    def pdf2csv(self, file_url):
        tabula.convert_into(file_url, "output.csv", output_format="csv", pages='all')
        self.df = pd.read_csv('./output.csv')
        self.category = self.df.columns
        self.names = ['classNbr', 'subj', 'crs', 'courseTitle', 'sbc', 'cmp', 'sctn', 'credits', 'day', 'startTime', 'endTime', 'room', 'instructor', 'likes', 'reviews', 'instructor_names']
    
    def courses2db(self, reset_db=True): 
        if (reset_db):
            self.collection.delete_many({})
            
        for i in range(len(self.df)):
            # subj, crs, course title, sctn 같을 시 이미 있는 데이터로 취급 
            find_it = self.collection.find_one({self.names[1]: self.df[self.category[1]].iloc[i],
                                        self.names[2]: self.df[self.category[2]].iloc[i],
                                        self.names[3]: self.df[self.category[3]].iloc[i],
                                        self.names[6]: self.df[self.category[6]].iloc[i]
                                        })
            
            # 수업 이미 있을 경우
            if find_it != None and self.df[self.category[1]].iloc[i] != 'Subj':
                find_it[self.names[8]].append({self.semester: self.df[self.category[8]].iloc[i]})
                find_it[self.names[9]].append({self.semester: self.df[self.category[9]].iloc[i]})
                find_it[self.names[10]].append({self.semester: self.df[self.category[10]].iloc[i]})
                find_it[self.names[11]].append({self.semester: self.df[self.category[11]].iloc[i]})
                find_it[self.names[12]].append({self.semester: self.df[self.category[12]].iloc[i]})
                find_it[self.names[15]] += ', ' + str(self.df[self.category[12]].iloc[i])

                self.collection.find_one_and_update({self.names[1]: self.df[self.category[1]].iloc[i],
                                            self.names[2]: self.df[self.category[2]].iloc[i],
                                            self.names[3]: self.df[self.category[3]].iloc[i],
                                            self.names[6]: self.df[self.category[6]].iloc[i]
                                            }, 
                                            {'$set': {
                                            self.names[8]: find_it[self.names[8]],
                                            self.names[9]: find_it[self.names[9]],
                                            self.names[10]: find_it[self.names[10]],
                                            self.names[11]: find_it[self.names[11]],
                                            self.names[12]: find_it[self.names[12]],
                                            self.names[15]: find_it[self.names[15]]}
                                            })
                print("Exsiting course modified! : " + str(find_it[self.names[3]]))

            # 수업 정보 없으면 새로 만듦
            else:
                self.collection.insert_one({
                self.names[0]: self.df[self.category[0]].iloc[i],
                self.names[1]: self.df[self.category[1]].iloc[i],
                self.names[2]: self.df[self.category[2]].iloc[i],
                self.names[3]: self.df[self.category[3]].iloc[i],
                self.names[4]: self.df[self.category[4]].iloc[i],
                self.names[5]: self.df[self.category[5]].iloc[i],
                self.names[6]: self.df[self.category[6]].iloc[i],
                self.names[7]: self.df[self.category[7]].iloc[i],
                self.names[8]: [{self.semester: self.df[self.category[8]].iloc[i]}],
                self.names[9]: [{self.semester: self.df[self.category[9]].iloc[i]}],
                self.names[10]: [{self.semester: self.df[self.category[10]].iloc[i]}],
                self.names[11]: [{self.semester: self.df[self.category[11]].iloc[i]}],
                self.names[12]: [{self.semester: self.df[self.category[12]].iloc[i]}],
                self.names[13]: [],
                self.names[14]: [],
                self.names[15]: str(self.df[self.category[12]].iloc[i])
                })
                print("New course added! : " + str(self.df[self.category[3]].iloc[i]))
   