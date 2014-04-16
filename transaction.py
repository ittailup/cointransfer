#from price_call import PriceCall
import datetime
#from pay_checker import PayChecker

class Transfer:
    
    def __init__(self, params):
        # validation hash
        self.amountin = params['amount_in'] # receiving amount
        self.price = params['price']
        self.currencypair = params['currency_pair']
        self.sourcecurrency = params['source_currency'] #params['direction']  
        try:
            # check for discrepancies
            self.amountout = params['amount_out']
        except KeyError:
            if self.currencypair == False:
                self.amountout = self.amountin * self.price[self.currencypair] # sending amount
            else:
                self.amountout = self.amountin / self.price[self.currencypair] # sending amount        
        
        self.sourceaddress = params['source_address'] # client address
        self.receivingaddress = 'DHNMLUAdasGXizBYfXfGQsSo63sPR1dr1r' #self.create_address # where we're picking it up from, should be same altcoin as sourceaddress
        self.destaddress = params['destination_address']
        self.email = params['email']
        #self.emailout = params['email_out']
        self.createtime = datetime.datetime.now
        self.payment_received = False
    
    def __str__(self):
        return str(self.payment_info())
        
    #def create_address(self, params):
        
        
    
    def payment_info(self):
        payment_info = {}
        # validation hash
        payment_info['amount_in'] = self.amountin
        payment_info['amount_out'] = self.amountout
        payment_info['currency_pair'] = self.currencypair
        payment_info['receiving_address'] = self.receivingaddress
        payment_info['source'] = self.sourceaddress
        payment_info['destination'] = self.destaddress
        payment_info['email'] = self.email
        if self.currencypair[3] == self.sourcecurrency:
            payment_info['dest_currency'] = payment_info['currency_pair'][3:]
            payment_info['source_currency'] = payment_info['currency_pair'][3]
            print payment_info['source_currency'] 
        else:
            payment_info['dest_currency'] = payment_info['currency_pair'][3]
            payment_info['source_currency'] = payment_info['currency_pair'][:3]
        #payment_info['email_out'] = self.emailout
        return payment_info
                
params = {  'amount_in':5,
            'amount_out':None,
            'currency_pair':'dogebtc',
            'source_currency':'doge',
            'source_address':'1234',
            'receiving_address':'DHNMLUAdasGXizBYfXfGQsSo63sPR1dr1r',
            'destination_address':4321, 
            'email':'gg',
            'price':{'dogebtc':'8'}}

#trans = Transaction(params).payment_info()

