from yahoo_finance import Share

def rec(p):
	yahoo = Share(p)
	a=yahoo.get_prev_close()
	b=yahoo.get_year_high()
	c=yahoo.get_year_low()
	d=yahoo.get_open()
	e=yahoo.get_ebitda()
	f=yahoo.get_market_cap()
	g=yahoo.get_avg_daily_volume()
	h=yahoo.get_dividend_yield()
	i=yahoo.get_earnings_share()
	j=yahoo.get_days_low()
	k=yahoo.get_days_high()
	l=yahoo.get_50day_moving_avg()
	m=yahoo.get_200day_moving_avg()
	n=yahoo.get_price_earnings_ratio()
	o=yahoo.get_price_earnings_growth_ratio()
	print p
	print "Previous Close: ",a
	print "Year High",b
	print "Year Low",c
	print "Open:",d
	print "EBIDTA",e 
	print "Market Cap",f
	print "Average Daily Volume",g 
	print "Dividend Yield",h
	print "Earnings per share",i 
	print "Days Range:", j ,"-",k
	print "50 Days Moving Average",l 
	print "200 Days Moving Average",m
	print"Price Earnings Ratio", n
	print"Price Earnings Growth Ratio",o

	import MySQLdb
	db = MySQLdb.connect(host="127.0.0.1", user="root",passwd="1111", db="stocks",local_infile = 1)  
	cur=db.cursor()
	cur.execute ("""
	            INSERT INTO stockapp_info (symbol, prev_close, year_high, year_low, open_price , ebidta, market_cap, avg_daily_vol , dividend_yield, eps , days_low ,days_high, moving_avg_50, moving_avg_200, price_earnings_ratio, price_earnings_growth_ratio)
	            VALUES
	                (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

	        """, (p,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o))
	db.commit() 
	cur.close()


stocklist=list()
with open ('stock_list.txt','r') as input_data:
	for each_stock in input_data:
		stocklist.append(str(each_stock).strip())


for stock in stocklist:
	rec(stock)




