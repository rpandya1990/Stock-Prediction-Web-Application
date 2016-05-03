from time import sleep, strftime, localtime  
from datetime import datetime
from Tkinter import *  
import MySQLdb  
import urllib  
import csv  
import os  
   
class App:  
   DATE_FMT = '%Y-%m-%d'
   
   def __init__(self):  
     self.entry_host = "127.0.0.1"  
     self.entry_user = "root"     
     self.entry_password = "1111"   
     self.entry_database = "stocks"  
     self.stock_list= list()
     with open('stock_list.txt', 'r') as input_data:
        for each_line in input_data:
            self.stock_list.append(str(each_line.rstrip('\n')))
   
   def tws_connect(self,stock_number):  
     print "downloading "+ self.stock_list[stock_number]+" csv file from yahoo..."  
     csv1 = urllib.urlopen("http://ichart.finance.yahoo.com/table.csv?s=" + self.stock_list[stock_number])  
     csv = csv1.readlines()
     fileName = self.stock_list[stock_number] + "_His.csv"  
     localFile1 = open(fileName.split('/')[-1], "w") 
     localFile1.write("Symbol,Date,Open,High,Low,Close,Volume,Adj Close\n") 
     for bar in xrange(1,len(csv)):
        if csv[bar].count(',')<6: continue
        list = csv[bar].split(',')
        dt_obj = datetime.strptime(list[0], '%Y-%m-%d')
        date = dt_obj.strftime(self.DATE_FMT)
        list[0] = date
        list.insert(0,self.stock_list[stock_number])
        str =",".join(list)
        localFile1.write(str)  
     csv1.close()  
     localFile1.close()   
   
   
   def mysql_connect(self,stock_number):  
     db = MySQLdb.connect(host=self.entry_host, user=self.entry_user,passwd=self.entry_password, db=self.entry_database,local_infile = 1)  
     cur = db.cursor()  
     current_path = os.getcwd()	
     filename = current_path + "/" + self.stock_list[stock_number] + "_His.csv"
     print "Storing ", self.stock_list[stock_number]
     csv_data = csv.reader(file(filename))
     l = os.listdir(".")
     sql = """LOAD DATA LOCAL INFILE '"""+ self.stock_list[stock_number]+"""_His.csv' INTO TABLE stockapp_history FIELDS TERMINATED BY ','  OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\\n' IGNORE 1 LINES (symbol, date,Open,high,low,close,volume,adj_close);"""
     cur.execute(sql) 
     db.commit() 
     cur.close()
     db.close()

   
   def contract_info(self,stock_number):  
     print "contract info..."  
     print "Symbol: " + self.stock_list[stock_number]  

   def download(self, stock_number):
     self.tws_connect(stock_number)

   def import_csv(self,stock_number):
     self.mysql_connect(stock_number)
   

app = App()
for stock_number in xrange((len(app.stock_list))):
    q= app.download(stock_number)
    
for stock_number in xrange((len(app.stock_list))):
    app.import_csv(stock_number)



