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
        print 'why'
        for transaction in self.payments:       
            try:
                print 'what2'
                sourcecurrency = transaction['source_currency']
                if transaction['source_currency'] == 'btc':
                    if self.checkbtc == True:
                        print 'true'
                        self.received.append(transaction)
                        
                    else:
                        print 'false'
                        self.not_received.append(transaction)
                if transaction['source_currency'] == 'dog':
                    print "what"
                    transaction['payment_received'] = self.check_doge(transaction)
                    if transaction['payment_received'] == True:
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
        print self.conn.listtransactions(account = 'client1')
        received_amount = float(self.conn.getreceivedbyaddress(transaction['receiving_address']))
        if transaction['amount_in'] == received_amount:
            return True
        
            
            
            # check bitcoin blockchain
params = {  'amount_in':float(100), 
            'currency_pair':'dogbtc',
            'source_address':'1234',
            'source_currency':'doge',
            'receiving_address':'DHNMLUAdasGXizBYfXfGQsSo63sPR1dr1r',
            'destination_address':4321, 
            'email':'gg',
            'price':{'dogbtc':8}}

trans = Transfer(params).payment_info()


checker = PayChecker({'transactions':[trans]})

checker.check()

