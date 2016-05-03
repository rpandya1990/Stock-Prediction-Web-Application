
from django.shortcuts import *
from django.http import *
import json
#from .forms import FavForm
from track.models import *
from stockapp.models import info
from django.contrib.auth.decorators import login_required


@login_required
def track(request):
	user = request.user	
	stocks = Fav.objects.filter(username=user)
	#a=[]
	information=[]
	try:
		if len(stocks) is not 0:
			for x in xrange(len(stocks)):
				#.append(stocks[i].stock.upper())
				#print a
				#b=  stocks[1].stock.upper()

				info1 = 	info.objects.filter(symbol=stocks[x].stock)
				# information.append(info.objects.filter(symbol=stock.stock))
				stocks[x].info = info1
				# print stock.__dict__
				# print information
				#information1=info.objects.filter(symbol=b)
			# print len(stock)
			print len(stocks)
	except:
		pass
	return render_to_response("track/track.html", locals())

@login_required
def track_ajax(request):
	if request.method=="GET":
		stock1=request.GET["stock_name"]
		if len(stock1) is not 0:

			try:
				if request.user.is_authenticated():
					user1=request.user
					s=Fav(username=user1, stock=stock1)
					s.save()
					i = info.objects.filter(symbol=stock1)
					print i[0].prev_close
					data={
						"message": "Successfully inserted",
						"price" : i[0].prev_close
					}

					return HttpResponse(json.dumps(data), content_type="application/json")
			except:
				pass

	data={
	"message":"Error"
	}
	return HttpResponse(json.dumps(data), content_type="application/json")


@login_required
def track_ajax1(request):
	# console.log("Inside track track_ajax1")
	if request.method=="GET":
		stock2=request.GET["stock_name1"]
		if len(stock2) is not 0:
			try:
				if request.user.is_authenticated():
					# console.log("Authentication success")
					user1=request.user
					Fav.objects.filter(username=user1,stock=stock2).delete()
					data={
						"message": "Successfully deleted"
					}

					return HttpResponse(json.dumps(data), content_type="application/json")
			except:
				pass

	data={
	"message":"Error"
	}
	return HttpResponse(json.dumps(data), content_type="application/json")


