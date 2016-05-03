from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import json
from django.template import RequestContext

#import djngo.core.context_processors import csrf
from stockapp.models import info
from stockapp.models import history
from stockapp.models import prediction
from stockapp.models import COMP
from django.core import serializers
# from stockapp.models import current
import math, random, string
import urllib2, time
from datetime import datetime, timedelta
from time import mktime
import MySQLdb
import numpy
from yahoo_finance import Share


from scipy.stats import norm
from sklearn.svm import SVR, SVC, LinearSVC
# from datetime import datetime

random.seed(0)
# Create your views here.
def index(request):
	return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def graph_data(request,name):
	h=history.objects.filter(symbol=name.upper())
	data=[]
	for i in h:
		d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
		data.append(d)
    # print data
	jsondata=json.dumps(data[:1000])
	return HttpResponse(jsondata)
	# return JsonResponse(list(h),safe=False)

def graph_data_time(request, name, days):
    h=history.objects.filter(symbol=name.upper())
    data=[]
    for i in h:
        d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
        data.append(d)
    # print data
    jsondata=json.dumps(data[:int(days)])
    return HttpResponse(jsondata)

def rsi_data(request, name):
    h=history.objects.filter(symbol=name.upper())
    data=[]
    for i in h:
        d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
        data.append(d)
    # print data
    jsondata=json.dumps(data[:200])
    return HttpResponse(jsondata)

def rsi(request,name):
    # books=info.objects.filter(symbol=name)
    # ANN= analyzeSymbol(name)
    # Bayt= bayesian(name)
    # # Bay= bayesian1(name)
    # s=svm(name,5)
    return render(request, 'rsi.html',{'name':name.upper()})

def candlestick_data(request, name):
    h=history.objects.filter(symbol=name.upper())
    data=[]
    for i in h:
        d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
        data.append(d)
    # print data
    jsondata=json.dumps(data[:200])
    return HttpResponse(jsondata)

def candlestick(request,name):
    # books=info.objects.filter(symbol=name)
    # ANN= analyzeSymbol(name)
    # Bayt= bayesian(name)
    # # Bay= bayesian1(name)
    # s=svm(name,5)
    return render(request, 'candlestick.html',{'name':name.upper()})

def trendline_data(request, name):
    h=history.objects.filter(symbol=name.upper())
    data=[]
    for i in h:
        d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
        data.append(d)
    # print data
    jsondata=json.dumps(data[:200])
    return HttpResponse(jsondata)

def trendline(request,name):
    # books=info.objects.filter(symbol=name)
    # ANN= analyzeSymbol(name)
    # Bayt= bayesian(name)
    # # Bay= bayesian1(name)
    # s=svm(name,5)
    return render(request, 'trendline.html',{'name':name.upper()})

def volume_data(request, name):
    h=history.objects.filter(symbol=name.upper())
    data=[]
    for i in h:
        d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
        data.append(d)
    # print data
    jsondata=json.dumps(data[:200])
    return HttpResponse(jsondata)

def volume(request,name):
    # books=info.objects.filter(symbol=name)
    # ANN= analyzeSymbol(name)
    # Bayt= bayesian(name)
    # # Bay= bayesian1(name)
    # s=svm(name,5)
    return render(request, 'volume.html',{'name':name.upper()})

def close_data(request, name):
    h=history.objects.filter(symbol=name.upper())
    data=[]
    for i in h:
        d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
        data.append(d)
    # print data
    jsondata=json.dumps(data[:200])
    return HttpResponse(jsondata)

def close(request,name):
    # books=info.objects.filter(symbol=name)
    # ANN= analyzeSymbol(name)
    # Bayt= bayesian(name)
    # # Bay= bayesian1(name)
    # s=svm(name,5)
    return render(request, 'close.html',{'name':name.upper()})

def macd_data(request, name):
    h=history.objects.filter(symbol=name.upper())
    data=[]
    for i in h:
        d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
        data.append(d)
    # print data
    jsondata=json.dumps(data[:200])
    return HttpResponse(jsondata)

def macd(request,name):
    # books=info.objects.filter(symbol=name)
    # ANN= analyzeSymbol(name)
    # Bayt= bayesian(name)
    # # Bay= bayesian1(name)
    # s=svm(name,5)
    return render(request, 'macd.html',{'name':name.upper()})

# def day1_data(request, name):
#     h=current.objects.filter(symbol=name.upper())
#     data=[]
#     for i in h:
#         d={'Date':str(i.date),'Open':float(str(i.Open)),'High':float(str(i.high)),'Low':float(str(i.low)),'Close':float(str(i.close)),'Volume':int(str(i.volume))}
#         data.append(d)
#     # print data
#     jsondata=json.dumps(data[:200])
#     return HttpResponse(jsondata)

# def day1(request,name):
#     # books=info.objects.filter(symbol=name)
#     # ANN= analyzeSymbol(name)
#     # Bayt= bayesian(name)
#     # # Bay= bayesian1(name)
#     # s=svm(name,5)
#     return render(request, '1day.html',{'name':name.upper()})

def search(request,name):
    books=info.objects.filter(symbol=name)
    p=prediction.objects.filter(symbol=name)
    yahoo = Share(name)
    c=yahoo.get_price()
    # print p[0]
    # a= p[0].ann_prediction
    # b= p[0].bayesian_prediction
    # shortterm=((p[0].ann_prediction+p[0].bayesian_prediction)/2)
    # print "mean", shortterm
    # print "current price", c
    # s= p[0].svm_prediction
    # a- ann
# b-bay
# c-current
# s-svm


    current=yahoo.get_price()
    a= p[0].ann_prediction
    svm=p[0].svm_prediction

    x,y=0,0
    if float(a)>1.1*float(current) or float(svm)>1.1*float(current):
        if float(a)>1.1*float(current):
            x=1
        elif float(svm)>1.1*float(current):
            y=1

        if float(a)>1.1*float(current) and float(svm)>1.1*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("Strong Buy for Short term gains")
            message="Strong Buy for Short term gains"

        elif (y==1 and x==0):
            print ("Strong Buy for Long term gains")
            message="Strong Buy for Long term gains"

        elif (y==1 and x==1):
            print ("Strong buy for short and long term gains")
            message="Strong buy for short and long term gains"




    if float(a)>float(current)+5 or float(svm)>1.05*float(current):
        x,y=0,0
        if float(a)>float(current)+5 and float(a)<=1.1*float(current):
            x=1
        elif float(svm)>1.05*float(current) and float(svm)<=1.1*float(current):
            y=1

        if float(a)>float(current)+5 and float(svm)>1.05*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("Buy for Short term gains")
            message="Buy for Short term gains"

        elif (y==1 and x==0):
            print ("Buy for Long term gains")
            message="Buy for Long term gains"

        elif (y==1 and x==1):
            print ("Buy for short and long term gains")
            message="Buy for short and long term gains"


    if float(a)<float(current)+5 and float(a)>float(current)-5 and float(svm)<=1.05*float(current) and float(svm)>0.95*float(current):
        x,y=0,0
        if float(a)<float(current)+5 and float(a)>float(current)-5:
            x=1
        elif float(svm)<=1.05*float(current) and float(svm)>0.95*float(current):
            y=1

        if float(a)<float(current)+5 and float(a)>float(current)-5 and float(svm)<=1.05*float(current) and float(svm)>0.95*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("HOLD")
            message="HOLD"

        elif (y==1 and x==0):
            print ("HOLD")
            message="HOLD"

        elif (y==1 and x==1):
            print ("HOLD")
            message="HOLD"



    if float(a)<float(current)-5 and float(a)>=0.90*float(current) or float(svm)<0.95*float(current) and float(svm)>0.90*float(current):
        x,y=0,0
        if float(a)>float(current)-5 and float(a)>0.90*float(current):
            x=1
        elif float(svm)>0.95*float(current) and float(svm)>0.90*float(current):
            y=1

        if float(a)>float(current)-5 and float(a)>=0.90*float(current) and float(svm)>0.95*float(current) and float(svm)>0.90*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("SELL")
            message="SELL"

        elif (y==1 and x==0):
            print ("SELL")
            message="SELL"

        elif (y==1 and x==1):
            print ("SELL")
            message="SELL"


    if float(a)<0.90*float(current) or float(svm)<0.90*float(current):
        if float(a)<0.90*float(current):
            x=1
        elif float(svm)<0.90*float(current):
            y=1

        if float(a)<0.90*float(current) or float(svm)<0.90*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("Strong SELL")
            message="Strong SELL"

        elif (y==1 and x==0):
            print ("Strong SELL")
            message="Strong SELL"

        elif (y==1 and x==1):
            print ("Strong SELL")
            message="Strong SELL"
    return render(request, 'search.html',{'name':name.upper(),'books': books,'p':p,'message':message})

def search1(request,name, day):
    books=info.objects.filter(symbol=name)
    p=prediction.objects.filter(symbol=name)
    yahoo = Share(name)
    c=yahoo.get_price()
    # print p[0]
    # a= p[0].ann_prediction
    # b= p[0].bayesian_prediction
    # shortterm=((p[0].ann_prediction+p[0].bayesian_prediction)/2)
    # print "mean", shortterm
    # print "current price", c
    # s= p[0].svm_prediction
    # a- ann
# b-bay
# c-current
# s-svm


    current=yahoo.get_price()
    a= p[0].ann_prediction
    svm=p[0].svm_prediction

    x,y=0,0
    if float(a)>1.1*float(current) or float(svm)>1.1*float(current):
        if float(a)>1.1*float(current):
            x=1
        elif float(svm)>1.1*float(current):
            y=1

        if float(a)>1.1*float(current) and float(svm)>1.1*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("Strong Buy for Short term gains")
            message="Strong Buy for Short term gains"

        elif (y==1 and x==0):
            print ("Strong Buy for Long term gains")
            message="Strong Buy for Long term gains"

        elif (y==1 and x==1):
            print ("Strong buy for short and long term gains")
            message="Strong buy for short and long term gains"




    if float(a)>float(current)+5 or float(svm)>1.05*float(current):
        x,y=0,0
        if float(a)>float(current)+5 and float(a)<=1.1*float(current):
            x=1
        elif float(svm)>1.05*float(current) and float(svm)<=1.1*float(current):
            y=1

        if float(a)>float(current)+5 and float(svm)>1.05*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("Buy for Short term gains")
            message="Buy for Short term gains"

        elif (y==1 and x==0):
            print ("Buy for Long term gains")
            message="Buy for Long term gains"

        elif (y==1 and x==1):
            print ("Buy for short and long term gains")
            message="Buy for short and long term gains"


    if float(a)<float(current)+5 and float(a)>float(current)-5 and float(svm)<=1.05*float(current) and float(svm)>0.95*float(current):
        x,y=0,0
        if float(a)<float(current)+5 and float(a)>float(current)-5:
            x=1
        elif float(svm)<=1.05*float(current) and float(svm)>0.95*float(current):
            y=1

        if float(a)<float(current)+5 and float(a)>float(current)-5 and float(svm)<=1.05*float(current) and float(svm)>0.95*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("HOLD")
            message="HOLD"

        elif (y==1 and x==0):
            print ("HOLD")
            message="HOLD"

        elif (y==1 and x==1):
            print ("HOLD")
            message="HOLD"



    if float(a)<float(current)-5 and float(a)>=0.90*float(current) or float(svm)<0.95*float(current) and float(svm)>0.90*float(current):
        x,y=0,0
        if float(a)>float(current)-5 and float(a)>0.90*float(current):
            x=1
        elif float(svm)>0.95*float(current) and float(svm)>0.90*float(current):
            y=1

        if float(a)>float(current)-5 and float(a)>=0.90*float(current) and float(svm)>0.95*float(current) and float(svm)>0.90*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("SELL")
            message="SELL"

        elif (y==1 and x==0):
            print ("SELL")
            message="SELL"

        elif (y==1 and x==1):
            print ("SELL")
            message="SELL"


    if float(a)<0.90*float(current) or float(svm)<0.90*float(current):
        if float(a)<0.90*float(current):
            x=1
        elif float(svm)<0.90*float(current):
            y=1

        if float(a)<0.90*float(current) or float(svm)<0.90*float(current):
            x,y=1,1

        if (x==1 and y==0):
            print ("Strong SELL")
            message="Strong SELL"

        elif (y==1 and x==0):
            print ("Strong SELL")
            message="Strong SELL"

        elif (y==1 and x==1):
            print ("Strong SELL")
            message="Strong SELL"

    # ANN= analyzeSymbol(name)
    # Bayt= bayesian(name)
    # # Bay= bayesian1(name)
    # s=svm(name,5)
    return render(request, 'search2.html',{'name':name.upper(),'days':day,'books': books,'p':p,'message':message})

# def macd(request,name,macd):
#     # books=info.objects.filter(symbol=name)
#     # ANN= analyzeSymbol(name)
#     # Bayt= bayesian(name)
#     # # Bay= bayesian1(name)
#     # s=svm(name,5)
#     return render(request, 'macd.html',{'name':name.upper(),'macd':macd})

def register(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('../register_success.html')
		else:
			return HttpResponseRedirect('../invalid_register.html')
	args = {}
	args.update(csrf(request))
	
	args['form'] = MyRegistrationForm()
	return render_to_response('register.html', args)
	
def register_success(request):
	return render_to_response('register_success.html')
	
def invalid_register(request):
	return render_to_response('invalid_register.html')
	
# def search(request,name):
# 	books=info.objects.filter(symbol=name)
# 	ANN= analyzeSymbol(name)
# 	Bay1= bayesian1(name)
#     Bay= bayesian(name)
# 	return render(request, 'search.html', {
# 		'name':name.upper(),
# 		'books': books,
# 		'ANN':ANN,
#         'Bay':Bay,
#         'Bay1':Bay1,
# 		})



def getcurrent(name):
    db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='1111',db='stocks')
    cursor=db.cursor()
    sql = '''SELECT time,close FROM stockapp_current WHERE symbol LIKE "%''' + name + '''%"'''
    cursor.execute(sql)
    result=cursor.fetchall()
    # print result
    output=[]
    for i in range(0,len(result)):
        temp=[]
        temp1=result[i][0]
        temp.append(str(temp1))
        temp.append(float(result[i][1]))
        output.append(temp)
    return output


def gethistorical(name):
    try:
        db=MySQLdb.connect(host='127.0.0.1',user='root',passwd='1111',db='stocks')
        cursor=db.cursor()
        sql = '''SELECT date,Open,close FROM stockapp_history WHERE symbol LIKE "%''' + name + '''%"'''
        cursor.execute(sql)
        result=cursor.fetchall()
        output=[]
        for i in range(0,len(result)):
            temp=[]
            tempstr=str(result[i][0].day)+'/'+str(result[i][0].month)+'/'+str(result[i][0].year)
            temp.append(tempstr)
            temp.append(float(result[i][1]))
            temp.append(float(result[i][2]))
            output.append(temp)
        return output
    except:
        return 0


def bayesian(name):
    data1=getcurrent(name.lower())
    data=[]
    a=60-len(data)
    for i in range(0,len(data1)):
        data.append(data1[i][1])
    #print data 
    x_10 =[]
    for b in xrange(0,a):
        t_data = []
        for i in xrange(len(data) - 10, len(data)):
            t_data.append(data[i])
        for i in xrange(1, 11):
            x_10.append(i)
        t=[]
        t.append(t_data)
        t_data = t
        #print t_data
        N = 10
        M = 6

        rel_err_dr=0

        x=x_10[len(x_10) - 1] + 1

        for k in range(1):
            t = numpy.zeros((N,1),float)
            phi = numpy.zeros((M,1),float)
            phi_sum = numpy.zeros((M,1),float)
            phi_sum_t = numpy.zeros((M,1),float)

            for i in range(M):
                phi[i][0]=math.pow(x,i)

            for i in range(N):
               t[i][0]=t_data[k][i]
                
            for j in range(N):
                for i in range(M):
                    phi_sum[i][0]=phi_sum[i][0]+math.pow(x_10[j],i)
                    phi_sum_t[i][0]=phi_sum_t[i][0]+t[j][0]*math.pow(x_10[j],i)

        # Calculation of variance / standard deviation
            S=numpy.linalg.inv(0.005*numpy.identity(M)+11.1*numpy.dot(phi_sum,phi.T))

            var=numpy.dot((phi.T),numpy.dot(S,phi))
            var=var+1/11.1

        # Calculating the mean
            mean=11.1*numpy.dot(phi.T,numpy.dot(S,phi_sum_t))
           #error_n=0
            #error_n=error_n+math.fabs(t_actual[k]-mean)

            #abs_error=0
            #abs_error = abs_error + error_n
            mean = mean[0][0]
            #print 'mean', mean
            data.append(mean)

    t = t_data[0]
    t_data = t
    sum = 0
    avg = 0
    for i in t_data:
        sum += i
    mov = sum / len(t_data)
    #print 'mov', mov
    per = ((mean - mov) / mov) * 100
    #print 'per', per
    final = []
    mean = round(mean, 3)
    per = round(per, 3)
    final.append(mean)
    final.append(per)
    return final[0]

def bayesian1(name):
    data1=getcurrent(name.lower())
    data=[]
    a=390-len(data)
    for i in range(0,len(data1)):
        data.append(data1[i][1])
    #print data 
    x_10 =[]
    for b in xrange(0,a):
        t_data = []
        for i in xrange(len(data) - 10, len(data)):
            t_data.append(data[i])
        for i in xrange(1, 11):
            x_10.append(i)
        t=[]
        t.append(t_data)
        t_data = t
        #print t_data
        N = 10
        M = 6

        rel_err_dr=0

        x=x_10[len(x_10) - 1] + 1

        for k in range(1):
            t = numpy.zeros((N,1),float)
            phi = numpy.zeros((M,1),float)
            phi_sum = numpy.zeros((M,1),float)
            phi_sum_t = numpy.zeros((M,1),float)

            for i in range(M):
                phi[i][0]=math.pow(x,i)

            for i in range(N):
               t[i][0]=t_data[k][i]
                
            for j in range(N):
                for i in range(M):
                    phi_sum[i][0]=phi_sum[i][0]+math.pow(x_10[j],i)
                    phi_sum_t[i][0]=phi_sum_t[i][0]+t[j][0]*math.pow(x_10[j],i)

        # Calculation of variance / standard deviation
            S=numpy.linalg.inv(0.005*numpy.identity(M)+11.1*numpy.dot(phi_sum,phi.T))

            var=numpy.dot((phi.T),numpy.dot(S,phi))
            var=var+1/11.1

        # Calculating the mean
            mean=11.1*numpy.dot(phi.T,numpy.dot(S,phi_sum_t))
           #error_n=0
            #error_n=error_n+math.fabs(t_actual[k]-mean)

            #abs_error=0
            #abs_error = abs_error + error_n
            mean = mean[0][0]
            #print 'mean', mean
            data.append(mean)

    t = t_data[0]
    t_data = t
    sum = 0
    avg = 0
    for i in t_data:
        sum += i
    mov = sum / len(t_data)
    #print 'mov', mov
    per = ((mean - mov) / mov) * 100
    #print 'per', per
    final = []
    mean = round(mean, 3)
    per = round(per, 3)
    final.append(mean)
    final.append(per)
    return final[0]

def svm(name, day):
    '''
    Input: Name of the stock, How many days of after current day to get predicted price
    Output: Predicted Price for next n days
    '''
    data = gethistorical(name)
    data = data[::-1]
    open_price_list = []
    close_price_list = []
    predicted_price=[]
    for i in xrange(len(data)):
        open_price_list.append(data[i][1])
        close_price_list.append(data[i][2])
    for iterations in range(day):
        close_price_dataset=[]
        open_price_dataset=[]
        previous_ten_day_close_price_dataset=[]
        g=0
        h=50
        while h<len(close_price_list):
            previous_ten_day_close_price_dataset.append(close_price_list[g:h])
            open_price_dataset.append(open_price_list[h])
            close_price_dataset.append(close_price_list[h])
            g += 1
            h += 1
        moving_average_dataset=[]
        for x in previous_ten_day_close_price_dataset:
            i=0
            for y in x:
                i=i+y
            moving_average_dataset.append(i/10)
        feature_dataset = []
        for j in range(len(close_price_dataset)):
            list = []
            list.append(moving_average_dataset[j])
            list.append(open_price_dataset[j])
            feature_dataset.append(list)
        feature_dataset = numpy.array(feature_dataset)        
        close_price_dataset = numpy.array(close_price_dataset)
        clf = SVR(kernel='linear',degree=1)
        clf.fit(feature_dataset[-365:],close_price_dataset[-365:])
        target = []
        if iterations==0:
            url_string = "http://www.google.com/finance/getprices?q={0}".format(name)
            stock_info = Share(name)
            list = []
            list.append(stock_info.get_open())
            list.append(stock_info.get_50day_moving_avg())
            target.append(list)
            
        else:
            list = []
            list.append(moving_average_dataset[-1])
            list.append(open_price_dataset[-1])
            target.append(list)

        predicted_close_price = clf.predict(target)[0]
        predicted_price.append(predicted_close_price)
        open_price_list.append(close_price_list[-1])
        close_price_list.append(predicted_close_price)
    
    return predicted_price


## ================================================================

def normalizePrice(price, minimum, maximum):
    return ((2*price - (maximum + minimum)) / (maximum - minimum))

def denormalizePrice(price, minimum, maximum):
    return (((price*(maximum-minimum))/2) + (maximum + minimum))/2

## ================================================================

def rollingWindow(seq, windowSize):
    it = iter(seq)
    win = [it.next() for cnt in xrange(windowSize)] # First window
    yield win
    for e in it: # Subsequent windows
        win[:-1] = win[1:]
        win[-1] = e
        yield win

def getMovingAverage(values, windowSize):
    movingAverages = []
    
    for w in rollingWindow(values, windowSize):
        movingAverages.append(sum(w)/len(w))

    return movingAverages

def getMinimums(values, windowSize):
    minimums = []

    for w in rollingWindow(values, windowSize):
        minimums.append(min(w))
            
    return minimums

def getMaximums(values, windowSize):
    maximums = []

    for w in rollingWindow(values, windowSize):
        maximums.append(max(w))

    return maximums

## ================================================================

def getTimeSeriesValues(values, window):
    movingAverages = getMovingAverage(values, window)
    minimums = getMinimums(values, window)
    maximums = getMaximums(values, window)

    returnData = []

    # build items of the form [[average, minimum, maximum], normalized price]
    for i in range(0, len(movingAverages)):
        inputNode = [movingAverages[i], minimums[i], maximums[i]]
        price = normalizePrice(values[len(movingAverages) - (i + 1)], minimums[i], maximums[i])
        outputNode = [price]
        tempItem = [inputNode, outputNode]
        returnData.append(tempItem)

    return returnData

## ================================================================

def getHistoricalData(stockSymbol):
    historicalPrices = []
    
    # login to API
    urllib2.urlopen("http://api.kibot.com/?action=login&user=guest&password=guest")

    # get 14 days of data from API (business days only, could be < 10)
    url = "http://api.kibot.com/?action=history&symbol=" + stockSymbol + "&interval=daily&period=14&unadjusted=1&regularsession=1"
    apiData = urllib2.urlopen(url).read().split("\n")
    for line in apiData:
        if(len(line) > 0):
            tempLine = line.split(',')
            price = float(tempLine[1])
            historicalPrices.append(price)

    return historicalPrices

## ================================================================

def getTrainingData(stockSymbol):
    historicalData = getHistoricalData(stockSymbol)

    # reverse it so we're using the most recent data first, ensure we only have 9 data points
    historicalData.reverse()
    del historicalData[9:]

    # get five 5-day moving averages, 5-day lows, and 5-day highs, associated with the closing price
    trainingData = getTimeSeriesValues(historicalData, 5)

    return trainingData

def getPredictionData(stockSymbol):
    historicalData = getHistoricalData(stockSymbol)

    # reverse it so we're using the most recent data first, then ensure we only have 5 data points
    historicalData.reverse()
    del historicalData[5:]

    # get five 5-day moving averages, 5-day lows, and 5-day highs
    predictionData = getTimeSeriesValues(historicalData, 5)
    # remove associated closing price
    predictionData = predictionData[0][0]

    return predictionData

## ================================================================

def analyzeSymbol(stockSymbol):
    startTime = time.time()
    
    trainingData = getTrainingData(stockSymbol)
    
    network = NeuralNetwork(inputNodes = 3, hiddenNodes = 3, outputNodes = 1)

    network.train(trainingData)

    # get rolling data for most recent day
    predictionData = getPredictionData(stockSymbol)

    # get prediction
    returnPrice = network.test(predictionData)

    # de-normalize and return predicted stock price
    predictedStockPrice = denormalizePrice(returnPrice, predictionData[1], predictionData[2])

    # create return object, including the amount of time used to predict
    returnData = {}
    returnData['price'] = predictedStockPrice
    returnData['time'] = time.time() - startTime

    return returnData['price']

## ================================================================

    
## ================================================================

# calculate a random number a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

def makeMatrix(I, J, fill = 0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

def sigmoid(x):
    # tanh is a little nicer than the standard 1/(1+e^-x)
    return math.tanh(x)

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y**2

## ================================================================

class NeuralNetwork:
    def __init__(self, inputNodes, hiddenNodes, outputNodes):
        # number of input, hidden, and output nodes
        self.inputNodes = inputNodes + 1 # +1 for bias node
        self.hiddenNodes = hiddenNodes
        self.outputNodes = outputNodes

        # activations for nodes
        self.inputActivation = [1.0]*self.inputNodes
        self.hiddenActivation = [1.0]*self.hiddenNodes
        self.outputActivation = [1.0]*self.outputNodes
        
        # create weights
        self.inputWeight = makeMatrix(self.inputNodes, self.hiddenNodes)
        self.outputWeight = makeMatrix(self.hiddenNodes, self.outputNodes)
        # set them to random vaules
        for i in range(self.inputNodes):
            for j in range(self.hiddenNodes):
                self.inputWeight[i][j] = rand(-0.2, 0.2)
        for j in range(self.hiddenNodes):
            for k in range(self.outputNodes):
                self.outputWeight[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum   
        self.ci = makeMatrix(self.inputNodes, self.hiddenNodes)
        self.co = makeMatrix(self.hiddenNodes, self.outputNodes)

    def update(self, inputs):
        if len(inputs) != self.inputNodes-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.inputNodes-1):
            self.inputActivation[i] = inputs[i]

        # hidden activations
        for j in range(self.hiddenNodes):
            sum = 0.0
            for i in range(self.inputNodes):
                sum = sum + self.inputActivation[i] * self.inputWeight[i][j]
            self.hiddenActivation[j] = sigmoid(sum)

        # output activations
        for k in range(self.outputNodes):
            sum = 0.0
            for j in range(self.hiddenNodes):
                sum = sum + self.hiddenActivation[j] * self.outputWeight[j][k]
            self.outputActivation[k] = sigmoid(sum)

        return self.outputActivation[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.outputNodes:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.outputNodes
        for k in range(self.outputNodes):
            error = targets[k]-self.outputActivation[k]
            output_deltas[k] = dsigmoid(self.outputActivation[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.hiddenNodes
        for j in range(self.hiddenNodes):
            error = 0.0
            for k in range(self.outputNodes):
                error = error + output_deltas[k]*self.outputWeight[j][k]
            hidden_deltas[j] = dsigmoid(self.hiddenActivation[j]) * error

        # update output weights
        for j in range(self.hiddenNodes):
            for k in range(self.outputNodes):
                change = output_deltas[k]*self.hiddenActivation[j]
                self.outputWeight[j][k] = self.outputWeight[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change

        # update input weights
        for i in range(self.inputNodes):
            for j in range(self.hiddenNodes):
                change = hidden_deltas[j]*self.inputActivation[i]
                self.inputWeight[i][j] = self.inputWeight[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k] - self.outputActivation[k])**2
            
        return error


    def test(self, inputNodes):
        # print(inputNodes, '->', self.update(inputNodes))
        return self.update(inputNodes)[0]

    def weights(self):
        print('Input weights:')
        for i in range(self.inputNodes):
            print(self.inputWeight[i])
        print()
        print('Output weights:')
        for j in range(self.hiddenNodes):
            print(self.outputWeight[j])

    def train(self, patterns, iterations = 1000, N = 0.5, M = 0.1):
        # N: learning rate, M: momentum factor
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            # if i % 100 == 0:
            #     print('error %-.5f' % error)



def query1(request):
    db=MySQLdb.connect(host='localhost',user='root',passwd='1111',db='stocks')
    cursor=db.cursor()
    cursor.execute("SELECT symbol, prev_close  FROM `stockapp_info`")
    result=cursor.fetchall()
    for i in result:
        print i
    return render_to_response("query1.html/",{'result1' : result},context_instance=RequestContext(request))

def query2(request):
    db=MySQLdb.connect(host='localhost',user='root',passwd='1111',db='stocks')
    cursor=db.cursor()
    cursor.execute("SELECT MAX(close) FROM `stockapp_history` WHERE symbol='GOOG' and date>=(CURDATE()-INTERVAL 10 day)")
    result=cursor.fetchall()
    print "Answer of query2 ",float(round(result[0][0],3))
    print result
    result2=str(round(result[0][0],3))
    return render_to_response("query2.html/",{'result2' : result2},context_instance=RequestContext(request))
    #return render_to_response("query2.html/",context_instance=RequestContext(request))

def query3(request):
    db=MySQLdb.connect(host='localhost',user='root',passwd='1111',db='stocks')
    cursor=db.cursor()
    cursor.execute("SELECT AVG(close) FROM `stockapp_history` WHERE symbol='MSFT' and date>=(CURDATE()-INTERVAL 365 day)")
    
    result=cursor.fetchall()
    print "Hello"
    print result
    print "Query3", float(round(result[0][0],3))
    result3=str(round(result[0][0],3))
    return render_to_response("query3.html/",{'result3' : result3},context_instance=RequestContext(request))
    

def query4(request):
    db=MySQLdb.connect(host='localhost',user='root',passwd='1111',db='stocks')
    cursor=db.cursor()
    stock_list=[] 
    filename = 'stock_list.txt'
    with open('stock_list.txt', 'r') as input_data:

        for each_line in input_data:
            if each_line != ' ':
               stock_list.append(str(each_line.strip()))
    result4=[]
    for i in range(0,len(stock_list)):
        temp=[]
        #for stock in stock_list:
        cursor.execute("SELECT MIN(close) FROM `stockapp_history` where symbol='"+stock_list[i]+"'and date>=(CURDATE()-INTERVAL 365 day)")
        result=cursor.fetchall()
        # print type((result[0][0][0]))
        a= (str((round(float(str(result[0][0])),5))))
        print a
        #print 'Stockname: '+stock_list[0]+' -> Min Price: '+ a
        temp.append(stock_list[i])
        temp.append(a)
        result4.append(temp)
    
    return render_to_response("query4.html/",{'result4' : result4},context_instance=RequestContext(request))


def query5(request):
    db=MySQLdb.connect(host='localhost',user='root',passwd='1111',db='stocks')
    cursor=db.cursor()
    cur=db.cursor()
    cur1=db.cursor()
    cur2=db.cursor()
    names=[] 
    filename = 'stock_list.txt'
    with open('stock_list.txt', 'r') as input_data:

        for each_line in input_data:
            if each_line != ' ':
               names.append(str(each_line.strip()))
    print "Length",len(names)
    # for i in range(0,len(names)):
    #     cursor.execute("SELECT AVG(close) FROM `stockapp_history` where symbol='"+names[i]+"'")
    #     result=cursor.fetchall()
    #     query="INSERT INTO avgdata1 (stockname, avgclose) VALUES (%s,%s);"
    #     query_data=(names[i],round(result[0][0],5))
    #     cur.execute(query,query_data)
    #     db.commit()
    cur1.execute("SELECT MIN(close) FROM `stockapp_history` where symbol='GOOG' and date>=(CURDATE()-INTERVAL 365 day)")
    res=cur1.fetchall()
    target = round(res[0][0],3)
    print 'Target value -> ',target


    query2 = " select * from avgdata1 where avgclose < " + str(target) +"  order BY stockname"
    print query2
    cur2.execute(query2)
    result5=cur2.fetchall()
    print result5
    return render_to_response("query5.html/",{'result5name': result5},context_instance=RequestContext(request))
    
def compare(request):
    stocks=[]
    #COMP.objects.all().delete()
    s=COMP.objects.all().filter()
    if len(s) is not 0:
        print s[0].symbol
        print s[1].symbol
        stocks.append(str(s[0].symbol))
        stocks.append(str(s[1].symbol))
    #stocks=['GOOG','YHOO']
    #
    try:
        infox=dict()
        for stock in stocks:
            #.append(stocks[i].stock.upper())
            #print a
            #b=  stocks[1].stock.upper()

            i=info.objects.filter(symbol=stock)
            print i[0]
            #infox[1].append(i)
            infox[stock]=i[0]
            print infox
            #stocks[x].info = i
            # information.append(info.objects.filter(symbol=stock.stock))
            #stocks[x].info = info1
            #print stocks[x].info
            # print stock.__dict__
            # print information
            #information1=info.objects.filter(symbol=b)
        print len(stocks)
        #print infox
    except:
        pass
    return render_to_response("compare.html", locals())




def compare_ajax(request):
    if request.method=="GET":
        stocks=[]
        stock1=request.GET["stock_name"]
        stock2=request.GET["stock_name2"]
        print "hey there"
        stocks.append(stock1)
        stocks.append(stock2)
        #if len(stock1) is not 0:

        try:
            
            i = info.objects.filter(symbol=stock1)
            # print i[0]
            j = info.objects.filter(symbol=stock2)
            # print j[0]
            # COMP.objects.all().delete()
            # s=COMP(symbol=stock1)
            #print s
            # s.save()
            # t=COMP(symbol=stock2)
            # t.save()
            data={
                "message": "compare successfull",
                "info1" : serializers.serialize('json', [ i[0], ]),
                "info2": serializers.serialize('json', [ j[0], ]),
            }
            print data
            print json.dumps(data)
            return HttpResponse(json.dumps(data), content_type="application/json")
        except:
            print "hello"

    data={
    "message":"Error"
    }
    return HttpResponse(json.dumps(data), content_type="application/json")
