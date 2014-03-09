class PayChecker:
    def __init__(self,params):
        self.startttime = datetime.now
        self.payments = params['transactions']
        self.received = []
        self.not_received = []
    
    def check(self):
        for transaction in self.payments:
            payment_info = transaction.payment_info
        
            if payment_info[ == 'btc':
                try:
                    self.check_btc(payment_info)
                except:
                    print "Check failed" #log
                    self.not_received.append(transaction)
                    
    def check_btc(self, payment_info):
        # check it is btc        
        if payment_info['currencypair'][3] =='btc':
            print payment_info['currencypair'][3]
            
            # check bitcoin blockchain
