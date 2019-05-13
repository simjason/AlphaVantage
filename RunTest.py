from tests.TestUtil import TestUtil
from tests.TestStockTimeSeries import TestStockTimeSeries
import time 

apikey = 'RPHZYNTKRYDVELOR'

"""
Test Util Class
"""
u = TestUtil(apikey)
r = u.test_GETRequest()
df = u.test_toDataFrame()

"""
Test Stock Time Series
"""
ts = TestStockTimeSeries(apikey)
ts.test_get_Intraday()
ts.test_get_Daily()
ts.test_get_Weekly()
ts.test_get_Monthly()
ts.test_get_Quote_Endpoint()