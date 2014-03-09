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


class PriceCall:
    def __init__(self, params):
        self.currencypair = params['currencypair']
        if self.currencypair == 'dogebtc':
            self.prices = self.doge2btc
    
    def prices(self):
        return self.prices
            
    def dogebtc(self):
        try:
            for i in range(0,5):
                while True:
                    try:
                        data = json.load(urllib2.urlopen("http://pubapi.cryptsy.com/api.php?method=marketdatav2"))['return']
                        self.prices['dogebtc'] = data['markets']['DOGE/BTC']['lasttradeprice'] # cryptsy hardcoded for now
                        return self.prices
                    except:
                        continue
                    break
        except:
            # log error, price failed after 5 tries
            raise IOError

        
        #self.prices['dogeltc'] = cryptsydata['markets']['DOGE/LTC']['lasttradeprice']
        

class Checker:
    def __init__(self,params):
        self.startttime = datetime.now
        self.payments = params['transactions']
        self.received = []
        self.not_received = []
    
    def check(self):
        for transaction in self.payments:
            payment_info = transaction.payment_info
            
            if payment_info['currencypair'][3:] == 'btc':
                try:
                    self.check_btc(payment_info)
                except:
                    print "Check failed" #log
                    self.not_received.append(transaction)
                    
    def check_btc(self, payment_info):
        # check it is btc        
        if payment_info['currencypair'][3:] = 'btc':
            print payment_info['currencypair'][3:]
            # check bitcoin blockchain
                 
    
class Payer:
    
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
        self.receivingaddress = params['receiving_address'] # where we're picking it up from, should be same altcoin as sourceaddress
        self.destaddress = params['destination_address']
        self.email = params['email']
        #self.emailout = params['email_out']
        self.createtime = datetime.now
        self.price = self.get_price
        if self.flipdirection = False:
            self.amountout = self.amountin * self.price[self.currencypair] # sending amount
        else:
            self.amountout = self.amountin / self.price[self.currencypair] # sending amount        
    
    def payment_info(self):
        payment_info = {}
        payment_info['amount_out'] = self.amountout
        payment_info['currencypair'] = self.currencypair
        payment_info['receiving_address'] = self.receivingaddress
        payment_info['source'] = self.sourceaddress
        payment_info['destination'] = self.destaddress
        payment_info['email'] = self.email
        if self.flipdirection = False:
            payment_info['dest_currency'] = payment_info['currencypair'][:3]
            payment_info['source_currency'] = payment_info['currencypair'][3:]
        else:
            payment_info['dest_currency'] = payment_info['currencypair'][3:]
            payment_info['source_currency'] = payment_info['currencypair'][:3]
        #payment_info['email_out'] = self.emailout
        return payment_info
                
    def get_price(self):
        callparams = {'currencypair':self.currencypair}
        return PriceCall(callparams).prices
       