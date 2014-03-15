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

