class StockTimeSeries:

	def __init__(self,base_url,api_key):
		self.BASE_URL = base_url
		self.API_KEY = api_key

	def get_Intraday(self,symbol,interval=15,outputsize='compact',datatype='json'):
		"""
		Returns intraday time series (timestamp, open, high, low, close, volume) 
		of the equity specified.
		"""
		function = 'TIME_SERIES_INTRADAY'
		request_string = '%sfunction=%s&symbol=%s&interval=%smin&outputsize=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,interval,outputsize,self.API_KEY,datatype)

		return request_string

	def get_Daily(symbol,adjusted=True,outputsize='full',datatype='json'):	
		"""
		Returns daily time series (date, daily open, daily high, daily low, daily 
		close, daily volume) of the global equity specified, covering 20+ years of 
		historical data. The most recent data point is the cumulative prices and volume 
		information of the current trading day, updated realtime.
		"""
		function = 'TIME_SERIES_DAILY'
		if(adjusted):
			function+='_ADJUSTED'
		request_string = '%sfunction=%s&symbol=%s&outputsize=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,outputsize,self.API_KEY,datatype)

		return request_string
		
	def get_Weekly(symbol,adjusted=True,datatype='json'):
		"""
		Returns weekly time series (last trading day of each week, weekly open, weekly high, 
		weekly low, weekly close, weekly volume) of the global equity specified, covering 20+ 
		years of historical data. The latest data point is the cumulative prices and volume 
		information for the week (or partial week) that contains the current trading day, 
		updated realtime.
		"""
		function = 'TIME_SERIES_WEEKLY'
		if(adjusted):
			function+='_Adjusted'
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
		if(adjusted):
			function+='_Adjusted'
		request_string = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)

		return request_string

	def get_Quote_Endpoint(symbol,datatype='json'):
		"""
		A lightweight alternative to the time series APIs, this service returns the latest 
		price and volume information for a security of your choice.
		"""
		function = 'GLOBAL_QUOTES'
		request_string = '%sfunction=%s&symbol=%s&apikey=%s&datatype=%s'%\
							(self.BASE_URL,function,symbol,self.API_KEY,datatype)

		return request_string

	def get_Search_Endpoint():
		"""
		TODO for whenever a search box is implemented
		"""		
		pass