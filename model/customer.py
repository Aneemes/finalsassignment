class customer:
    def __init__(self,customername, customerid):
        self.customername = customername
        self.customerid = customerid

    def set_customername(self,customername):
        self.customername=customername

    def get_customername(self):
        return self.customername

    def set_customerid(self,customerid):
        self.customerid=customerid

    def get_customerid(self):
        return self.customerid