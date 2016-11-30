import tushare as ts

class TushareStockCrawler(object):
    def __init__(self):
        pass

    def get_stock_basics(self):
        return ts.get_stock_basics()
