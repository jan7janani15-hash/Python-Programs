class Transaction:
    def __init__(self,txn_id,customer,price,qty,discount):
        self.txn_id=txn_id
        self.customer=customer
        self.total=price*qty*(1-discount)
    def get_net_total(self):
        return self.total
    def to_dict(self):
        return {"txn_id":self.txn_id,
                "name":self.customer,
                "total":self.total}
t=Transaction("TXN_501","Asha",500.0,2,0.10)
print(t.get_net_total())
print(t.to_dict())