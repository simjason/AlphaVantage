import unittest
import numpy as np
import pandas as pd
from api.AlphaVantage import AlphaVantage
from api.StockTimeSeries import StockTimeSeries

class TestStockTimeSeries(unittest.TestCase):

    def __init__(self,apikey=None):
        print("TestStockTimeSeries")
        self.apikey = apikey
        self.av = AlphaVantage(apikey)
        self.ts = self.av.StockTimeSeries

    def test_get_Intraday(self):
        print(" Test get_Intraday")
        df = self.ts.get_Intraday('msft')
        assert(isinstance(df,pd.DataFrame))
        assert(len(df)>0)
        assert(len(df.columns)==5)
        print(df.head())


    def test_get_Daily(self):
        print(" Test get_Daily")
        df = self.ts.get_Daily('msft')
        assert(isinstance(df,pd.DataFrame))
        assert(len(df)>0)
        assert(len(df.columns)==8)
        print(df.head())


    def test_get_Weekly(self):
        print(" Test get_Weekly")        
        df = self.ts.get_Weekly('msft')
        assert(isinstance(df,pd.DataFrame))
        assert(len(df)>0)
        assert(len(df.columns)==7)
        print(df.head())


    def test_get_Monthly(self):
        print(" Test get_Monthly")                    
        df = self.ts.get_Monthly('msft')
        assert(isinstance(df,pd.DataFrame))
        assert(len(df)>0)
        assert(len(df.columns)==7)
        print(df.head())


    def test_get_Quote_Endpoint(self):
        print(" Test Quote_Endpoint")                            
        df = self.ts.get_Quote_Endpoint('msft')
        assert(isinstance(df,pd.DataFrame))
        assert(len(df)==10)
        assert(len(df.columns)==1)
        print(df.head())
