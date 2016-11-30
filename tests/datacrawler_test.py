import unittest
from datacrawler.stock_crawler_factory import StockCrawlerFactory

class DataCrawlerTest(unittest.TestCase):
    def setUp(self):
        self.stock_crawler = StockCrawlerFactory('TuShare').getStockCrawler()

    def test_get_stock_basics(self):
        self.assertIsNotNone(self.stock_crawler.get_stock_basics, None)

if __name__ == '__main__':
    unittest.main()
