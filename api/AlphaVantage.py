'''
REST API Wrapper for Alpha Vantage
'''
import requests
import os
import sys

from api.StockTimeSeries import StockTimeSeries

class AlphaVantage:
    BASE_URL = 'https://www.alphavantage.co/query?'
    def __init__(self,apikey=None):
        self.API_KEY = apikey
        self.StockTimeSeries = StockTimeSeries(base_url = self.BASE_URL,api_key = self.API_KEY)