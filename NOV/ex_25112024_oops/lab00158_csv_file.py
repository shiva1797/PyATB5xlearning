import pandas as pd1
import  csv

class Test_READ():
    def test_read_csv(self):
        with open('userdata.csv') as csvfile1:
          read_data = csv.reader(csvfile1)

          for row in read_data:
                print(row[0],row[1])


    def test_read_pandas(self):
        df = pd1.read_csv('userdata.csv')
        print(df)