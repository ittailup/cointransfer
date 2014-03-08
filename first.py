'''from bitcoinrpc.authproxy import AuthServiceProxy
access = ServiceProxy("http://user:password@127.0.0.1:8332")
access.getinfo()
access.listreceivedbyaddress(6)'''

import bitcoinrpc

from datetime import datetime, date, time
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from testspiders.spiders.followall import FollowAllSpider
import json
import urllib2


class RateCall:
    
    def __init__(self, params):
        self.currencypair = params['currencypair']
        if self.currencypair = 'dogebtc':
            self.prices = self.doge2btc
    
    def prices:
        return self.prices
            
    def doge2btc(self):
        cryptsydata = json.load(urllib2.urlopen("http://pubapi.cryptsy.com/api.php?method=marketdatav2"))['return']
        self.prices['dogebtc'] = cryptsydata['markets']['DOGE/BTC']['lasttradeprice']
        #self.prices['dogeltc'] = cryptsydata['markets']['DOGE/LTC']['lasttradeprice']
        return self.prices

class Checker:
    
    def __init__(self,params):
        self.startttime = datetime.now
        self.payments = params['transactions']
    
    def check:
        for transaction in self.payments:
            payment_info = transaction.payment_info
            
            if payment_info['source_currencty'] = 'btc':
                try:
                    self.check_btc(payment_info)
                except:
                    print "Check failed"
                    raise
    def check_btc
                
    
class PaymentWorker:
    
    def __init__(self, params):
        self.starttime = datetime.now
        self.payments = params['transactions']
    
    def pay:
        for transaction in self.payments:
            payment_info = transaction.payment_info
            
            if payment_info['dest_currency'] = 'doge':
                try:
                    self.pay_doge(payment_info)
                    
                except:
                    print "Payment failed"
                    raise
    
    def pay_doge(self, payment_info):
            dogecoind = dogecoinrpc.connect_to_local()
            
    
    #def pay_btc:

class Transaction:
    
    def __init__(self, params):
        self.amountin = params['amount_in'] # receiving amount
        self.currencypair = params['currency_pair']
        self.flipdirection = False #params['direction']  
        self.sourceaddress = params['source_address'] # client address
        self.receivingaddress = params['receiving_address'] # where we're picking it up from, should be same coin as sourceaddress
        self.destaddress = params['destination_address']
        self.email = params['email']
        #self.emailout = params['email_out']
        self.createtime = datetime.now
        self.prices = self.get_prices
        if self.flipdirection = False:
            self.amountout = self.amountin * self.prices[self.currencypair] # sending amount
        else:
            self.amountout = self.amountin / self.prices[self.currencypair] # sending amount
            
    
    def receive_info:
        receive_info = {}
        receive_info['amount_in'] = self.amountin
        receive_info['source_address'] = self.sourceaddress
        receive_info['receivingaddress'] self.receivingaddress
        receive_info['email'] = self.email
        
    
    def payment_info:
        payment_info = {}
        payment_info['amount_out'] = self.amountout
        payment_info['currencypair'] = self.currencypair
        payment_info['source'] = self.sourceaddress
        payment_info['destination'] = self.destaddress
        payment_info['email'] = self.email
        if self.flipdirection = False:
            payment_info['dest_currency'] = payment_info['currencypair'][:3]
        else:
            payment_info['dest_currency'] = payment_info['currencypair'][3:]
        
        #payment_info['email_out'] = self.emailout
        return payment_info
                
    def get_prices(self):
        # run scrapy
        return RateCall({'currencypair':self.currencypair}).prices
       