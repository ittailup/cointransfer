#from price_call import PriceCall
import datetime
#from pay_checker import PayChecker

class Transfer:
    
    def __init__(self, params):
        # validation hash
        self.amountin = params['amount_in'] # receiving amount
        self.price = params['price']
        if bool(params['amount_out']): # if 
            self.amountout = params['amount_out']
        else:
            if self.flipdirection == False:
                self.amountout = self.amountin * self.price[self.currencypair] # sending amount
            else:
                self.amountout = self.amountin / self.price[self.currencypair] # sending amount        
        
        self.currencypair = params['currency_pair']
        self.flipdirection = False #params['direction']  
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
        payment_info['amount_out'] = self.amountout
        payment_info['currency_pair'] = self.currencypair
        payment_info['receiving_address'] = self.receivingaddress
        payment_info['source'] = self.sourceaddress
        payment_info['destination'] = self.destaddress
        payment_info['email'] = self.email
        payment_info['pay_order'] = self.flipdirection # if false, first currency is source, second currency is destination
        if self.flipdirection == False:
            payment_info['dest_currency'] = payment_info['currency_pair'][3:]
            payment_info['source_currency'] = payment_info['currency_pair'][3]
        else:
            payment_info['dest_currency'] = payment_info['currency_pair'][:3]
            payment_info['source_currency'] = payment_info['currency_pair'][:3]
        #payment_info['email_out'] = self.emailout
        return payment_info
                
params = {  'amount_in':5, 
            'currency_pair':'dogebtc',
            'source_address':'1234',
            'receiving_address':'DHNMLUAdasGXizBYfXfGQsSo63sPR1dr1r',
            'destination_address':4321, 
            'email':'gg',
            'price':{'dogebtc':'8'}}

#trans = Transaction(params).payment_info()

