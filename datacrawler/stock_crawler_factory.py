from tushare_stock_crawler import TushareStockCrawler

class StockCrawlerFactory(object):
    def __init__(self, crawler = 'TuShare'):
        if crawler == 'TuShare':
            self.__crawler = TushareStockCrawler()

    def getStockCrawler(self):
        return self.__crawler
