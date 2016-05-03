import urllib,time,datetime
import MySQLdb  
import csv  
import os  


class Quote(object):
  
  DATE_FMT = '%Y-%m-%d'
  TIME_FMT = '%H:%M:%S'
  
  def __init__(self):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))
    self.entry_host = "127.0.0.1"
    self.entry_user = "root"
    self.entry_password = "1111"
    self.entry_database = "stocks"


  def append(self,dt,open_,high,low,close,volume):
    self.date.append(dt.date())
    self.time.append(dt.time())
    self.open_.append(float(open_))
    self.high.append(float(high))
    self.low.append(float(low))
    self.close.append(float(close))
    self.volume.append(int(volume))
      
  def to_csv(self):
    return ''.join(["{0},{1},{2},{3:.2f},{4:.2f},{5:.2f},{6:.2f},{7}\n".format(self.symbol,
              self.date[bar].strftime('%Y-%m-%d'),self.time[bar].strftime('%H:%M:%S'),
              self.open_[bar],self.high[bar],self.low[bar],self.close[bar],self.volume[bar]) 
              for bar in xrange(len(self.close))])
    
  def write_csv(self,filename):
    with open(filename,'w') as f:
      f.write(self.to_csv())
        
  def read_csv(self,filename):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))
    for line in open(filename,'r'):
      symbol,ds,ts,open_,high,low,close,volume = line.rstrip().split(',')
      self.symbol = symbol
      dt = datetime.datetime.strptime(ds+' '+ts,self.DATE_FMT+' '+self.TIME_FMT)
      self.append(dt,open_,high,low,close,volume)
    return True

  def __repr__(self):
    return self.to_csv()

class GoogleIntradayQuote(Quote):
  ''' Intraday quotes from Google. Specify interval seconds and number of days '''
  def __init__(self,symbol,interval_seconds=60,num_days=2):
    super(GoogleIntradayQuote,self).__init__()
    self.symbol = symbol.upper()
    url_string = "http://www.google.com/finance/getprices?q={0}".format(self.symbol)
    url_string += "&i={0}&p={1}d&f=d,o,h,l,c,v".format(interval_seconds,num_days)
    csv = urllib.urlopen(url_string).readlines()
    for bar in xrange(7,len(csv)):
      if csv[bar].count(',')!=5: continue
      offset,close,high,low,open_,volume = csv[bar].split(',')
      if offset[0]=='a':
        day = float(offset[1:])
        offset = 0
      else:
        offset = float(offset)
      open_,high,low,close = [float(x) for x in [open_,high,low,close]]
      dt = datetime.datetime.fromtimestamp(day+(interval_seconds*offset))
      self.append(dt,open_,high,low,close,volume)

   

  def mysql_connect(self,stock_number):  
       print "connecting to mysql..."  
         
       print "MySQL host: " + self.entry_host 
       print "MySQL user: " + self.entry_user  
       print "MySQL database: " + self.entry_database  
       db = MySQLdb.connect(host=self.entry_host, user=self.entry_user,passwd=self.entry_password, db=self.entry_database,local_infile = 1)  
       cur = db.cursor()  
       current_path = os.getcwd() 
       #based on the stock number the correct filename should be formed
       filename1 = current_path + "/" + stock_list[stock_number]+"_Real.csv"
       print filename1
       csv_data1 = csv.reader(file(filename1))
       sql = """LOAD DATA LOCAL INFILE '"""+stock_list[stock_number]+"""_Real.csv' INTO TABLE stockapp_current FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' IGNORE 1 LINES (symbol, date,time,Open,high,low,close,volume);"""       
       print sql 
       cur.execute(sql) 
       db.commit() 
       cur.close()
       db.close()
 
if __name__ == '__main__':
	
  
  stock_list= list()
  with open('stock_list.txt','r') as ListOfStocks:
    for each_line in ListOfStocks:
    	stock_list.append(each_line.rstrip('\n'))
  for stock_number in xrange(len(stock_list)):
      q = GoogleIntradayQuote(str(stock_list[stock_number]))
      q.write_csv(str(stock_list[stock_number])+'_Real.csv')
      q.mysql_connect(stock_number)                                    
