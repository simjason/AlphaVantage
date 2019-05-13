'''
REST API Wrapper for Alpha Vantage StockTimeSeries
'''
from api.Util import Util

class StockTimeSeries(Util):

	def __init__(self,base_url,api_key):
		self.BASE_URL = base_url
		self.API_KEY = api_key

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

		return self.toDataFrame(req_str,ts_json_key)

	def get_Daily(self,symbol,adjusted=True,outputsize='full',datatype='json'):	
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

		req_str = '%sfunction=%s&symbol=%s&outputsize=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,outputsize,self.API_KEY,datatype)

		return self.toDataFrame(req_str,ts_json_key)

	def get_Weekly(self,symbol,adjusted=True,datatype='json'):
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

		req_str = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)
							
		return self.toDataFrame(req_str,ts_json_key)

	def get_Monthly(self,symbol,adjusted=True,datatype='json'):
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

		req_str = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)
		return self.toDataFrame(req_str,ts_json_key)

	def get_Quote_Endpoint(self,symbol,datatype='json'):
		"""
		A lightweight alternative to the time series APIs, this service returns the latest 
		price and volume information for a security of your choice.
		"""

		function = 'GLOBAL_QUOTE'
		
		ts_json_key = 'Global Quote'
		
		req_str = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)

		df = self.toDataFrame(req_str,ts_json_key)
		df.rename(index=str, columns={0: "Info"},inplace = True)
		return df 

	def get_Search_Endpoint():
		"""
		TODO for whenever a search box is implemented
		"""		
		pass		