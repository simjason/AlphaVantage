'''
REST API Wrapper for Alpha Vantage StockTimeSeries
'''
from Util import TimeSeries
import numpy as np
import pandas as pd

class StockTimeSeries(TimeSeries):

	def __init__(self,base_url,api_key):
		self.BASE_URL = base_url
		self.API_KEY = api_key

	def StockDataFrame(req_str,ts_json_key):
		"""
		Extracts values from json response and returns a Pandas DataFrame
		Structure of json response for Stock Time Series:
			-The first key returns a dictionary containing metadata about the series
			-The second key returns a dictionary containing OHLC and other information, with
			 timestamps as the key values.
		"""

		jsonDict = GETRequest(req_str)	

		time_series = jsonDict[ts_json_key]

		df = pd.DataFrame.from_dict(time_series,orient='index',columns = [key for key in time_series])

		return df

	def get_Intraday(self,symbol,interval=15,outputsize='compact',datatype='json'):
		"""
		Returns intraday time series (timestamp, open, high, low, close, volume) 
		of the equity specified.
		"""

		function = 'TIME_SERIES_INTRADAY'

		# Key to extract time series data from json dict

		ts_json_key = 'Time Series (%smin)'%(interval)

		req_str = '%sfunction=%s&symbol=%s&interval=%smin&outputsize=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,interval,outputsize,self.API_KEY,datatype)

			
		return StockDataFrame(req_str,ts_json_key)

	def get_Daily(symbol,adjusted=True,outputsize='full',datatype='json'):	
		"""
		Returns daily time series (date, daily open, daily high, daily low, daily 
		close, daily volume) of the global equity specified, covering 20+ years of 
		historical data. The most recent data point is the cumulative prices and volume 
		information of the current trading day, updated realtime.
		"""
		
		function = 'TIME_SERIES_DAILY'

		# Key to extract time series data from json dict
		
		ts_json_key = 'Time Series (Daily)'
		
		if(adjusted):
			function+='_ADJUSTED'

		request_string = '%sfunction=%s&symbol=%s&outputsize=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,outputsize,self.API_KEY,datatype)

		return 1

	def get_Weekly(symbol,adjusted=True,datatype='json'):
		"""
		Returns weekly time series (last trading day of each week, weekly open, weekly high, 
		weekly low, weekly close, weekly volume) of the global equity specified, covering 20+ 
		years of historical data. The latest data point is the cumulative prices and volume 
		information for the week (or partial week) that contains the current trading day, 
		updated realtime.
		"""

		function = 'TIME_SERIES_WEEKLY'
		
		# Key to extract time series data from json dict
		
		ts_json_key = 'Weekly Time Series'
		
		if(adjusted):
			function+='_Adjusted'
			ts_json_key = 'Weekly Adjusted Time Series'

		request_string = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)
							
		return request_string

	def get_Monthly(symbol,adjusted=True,datatype='json'):
		"""
		This API returns monthly time series (last trading day of each month, monthly open, 
		monthly high, monthly low, monthly close, monthly volume) of the global equity specified, 
		covering 20+ years of historical data. The latest data point is the cumulative prices 
		and volume information for the month (or partial month) that contains the current trading 
		day, updated realtime.
		"""
		
		function = 'TIME_SERIES_MONTHLY'
		
		# Key to extract time series data from json dict		
		
		ts_json_key = 'Monthly Time Series'		

		if(adjusted):
			function+='_Adjusted'
			ts_json_key = 'Monthly Adjusted Time Series'

		request_string = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)

		return request_string

	def get_Quote_Endpoint(symbol,datatype='json'):
		"""
		A lightweight alternative to the time series APIs, this service returns the latest 
		price and volume information for a security of your choice.
		"""

		function = 'GLOBAL_QUOTES'
		
		ts_json_key = 'Global Quote'
		
		request_string = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)

		return request_string

	def get_Search_Endpoint():
		"""
		TODO for whenever a search box is implemented
		"""		
		pass