import requests
import numpy as np
import pandas as pd

class Util(object):

    def GETRequest(self,req_str,datatype='json'):
        
        try:
            response = requests.get(req_str)
            response.raise_for_status()

            if datatype == 'json':
            # dictionary of json reponse is returned
                return response.json()
            else:
                return ('CSV Downloaded.')
        except requests.exceptions.HTTPError as err:
            return(err)


    def toDataFrame(self,req_str,ts_json_key):
        
        """
        Extracts values from json response and returns a Pandas DataFrame
        Structure of json response for Stock Time Series:
        -The first key returns a dictionary containing metadata about the series
        -The second key returns a dictionary containing OHLC and other information, with
        timestamps as the key values.       
        """
        jsonDict = self.GETRequest(req_str)

        assert(ts_json_key in jsonDict)

        time_series = jsonDict[ts_json_key] 

        df  = pd.DataFrame.from_dict(time_series,orient='index')

        return df