from __future__ import unicode_literals

from django.db import models


class info(models.Model):
               symbol = models.CharField(max_length=6)
               prev_close = models.CharField(max_length=20,null=True)
               year_high = models.CharField(max_length=20,null=True)
               year_low = models.CharField(max_length=20,null=True)
               open_price = models.CharField(max_length=20,null=True)
               ebidta = models.CharField(max_length=20,null=True)
               market_cap = models.CharField(max_length=20,null=True)
               avg_daily_vol = models.CharField(max_length=20,null=True)
               dividend_yield = models.CharField(max_length=20,null=True)
               eps = models.CharField(max_length=20,null=True)
               days_low = models.CharField(max_length=20,null=True)
               days_high = models.CharField(max_length=20,null=True)
               moving_avg_50 = models.CharField(max_length=20,null=True)
               moving_avg_200 = models.CharField(max_length=20,null=True)
               price_earnings_ratio = models.CharField(max_length=20,null=True)
               price_earnings_growth_ratio = models.CharField(max_length=20,null=True)
               def __str__(self):
                   return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.symbol, self.prev_close,self.year_high, self.year_low, self.open_price , self.ebidta, self.market_cap, self.avg_daily_vol , self.dividend_yield, self.eps , self.days_low ,self.days_high, self.moving_avg_50, self.moving_avg_200, self.price_earnings_ratio, self.price_earnings_growth_ratio)

class history(models.Model):
  symbol=models.CharField(max_length=6)
  date= models.DateField()
  Open=models.DecimalField(max_digits=20, decimal_places=10)
  high=models.DecimalField(max_digits=20, decimal_places=10)
  low=models.DecimalField(max_digits=20, decimal_places=10)
  close= models.DecimalField(max_digits=20, decimal_places=10)
  volume= models.IntegerField()
  adj_close= models.DecimalField(max_digits=20, decimal_places=10)
  def __str__(self):
    return '%s %s %s %s %s %s %s %s' % (self.symbol, self.date, self.Open, self.high, self.low, self.close, self.volume, self.adj_close)

class current(models.Model):
  symbol=models.CharField(max_length=6)
  date= models.DateField()
  time=models.TimeField()
  Open=models.DecimalField(max_digits=20, decimal_places=10)
  high=models.DecimalField(max_digits=20, decimal_places=10)
  low=models.DecimalField(max_digits=20, decimal_places=10)
  close= models.DecimalField(max_digits=20, decimal_places=10)
  volume= models.IntegerField()
  def __str__(self):
    return '%s %s %s %s %s %s %s %s' % (self.symbol, self.date, self.time, self.Open, self.high, self.low, self.close, self.volume)


class prediction(models.Model):
  symbol=models.CharField(max_length=6)
  ann_prediction=models.DecimalField(max_digits=20, decimal_places=10)
  bayesian_prediction=models.DecimalField(max_digits=20, decimal_places=10)
  svm_prediction=models.DecimalField(max_digits=20, decimal_places=10)
  def __str__(self):
    return '%s %s %s' % (self.ann_prediction, self.bayesian_prediction, self.svm_prediction)

class COMP(models.Model):
  symbol=models.CharField(max_length=6)