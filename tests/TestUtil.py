import unittest
import numpy as np
import pandas as pd
from api.Util import Util
from api.AlphaVantage import AlphaVantage

class TestUtil(unittest.TestCase):

    def __init__(self,apikey=None):
        print("TestUtil")
        self.apikey = apikey
        self.av = AlphaVantage(apikey)
        self.u = Util()

    def test_GETRequest(self):
        print(" Test GETRequest")
        req_str ='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey='
        req_str += self.apikey
        r = self.u.GETRequest(req_str);
        assert('Error Message' not in r)        
        print(req_str)

    def test_toDataFrame(self):
        print(" Test toDataFrame")        
        req_str ='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=15min&apikey='
        req_str += self.apikey
        df = self.u.toDataFrame(req_str,'Time Series (15min)')
        assert(isinstance(df,pd.DataFrame))
        assert(len(df)>0)
        assert(len(df.columns)==5)
        print(df.head())