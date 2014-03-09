import json
import urllib2

class PriceCall:
    def __init__(self, params):
        self.currencypair = params['currencypair']
        if self.currencypair == 'dogebtc':
            self.price = self.dogebtc()
    
    def __str__(self):
        return str(self.price)
    
    def price(self):
        return self.price
    
    def dogebtc(self):
        return self.get_data('DOGE/BTC')
        
                    
    def get_data(self, pair):
        price = int
        set = False
        while bool(set) == False:
            try:
                data = json.load(urllib2.urlopen("http://pubapi.cryptsy.com/api.php?method=marketdatav2"))['return']
                price = data['markets'][pair]['lasttradeprice']
                set = True
                break
            except:
                print str(Exception)
                continue
        return price
        

price = PriceCall({'currencypair':'dogebtc'})
print price