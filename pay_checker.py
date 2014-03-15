from transaction import Transfer
import datetime
import dogecoinrpc


class PayChecker:
    def __init__(self,params):
        self.startttime = datetime.datetime.now
        self.payments = params['transactions']
        self.received = []
        self.not_received = []
        self.failed = []
        self.conn = dogecoinrpc.connect_to_remote('dogecoinrpc','5zdrSvJq5957iVZxhpGkJTGFRZ9oGf6JNHisGVLsJ')
        
    
    def check(self):
        for transaction in self.payments:       
            try:
                if transaction.source_currency == 'btc':
                    if self.checkbtc == True:
                        self.received.append(transaction)
                    else:
                        self.not_received.append(transaction)
                if transaction.source_currency == 'doge':
                    transaction.payment_received = self.checkdoge
                    if transaction.payment_received == True:
                        self.received.append(transaction)
                    else:
                        self.not_received.append(transaction)
            except:
                print "Check failed" #log
                self.failed.append(transaction)
                    
    #def check_btc(self, transaction):
        # check it is btc        
       # if transaction.currencypair[3] =='btc':
            
    
    def check_doge(self, transaction):
        print self.conn.getreceivedbyaddress(transaction['receiving_address'])
        
            
            
            # check bitcoin blockchain
params = {  'amount_in':5, 
            'currency_pair':'dogebtc',
            'source_address':'1234',
            'receiving_address':'DHNMLUAdasGXizBYfXfGQsSo63sPR1dr1r',
            'destination_address':4321, 
            'email':'gg',
            'price':{'dogebtc':'8'}}

trans = Transfer(params).payment_info()


checker = PayChecker({'transactions':[trans]})

checker.check_doge

