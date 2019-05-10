import requests

class TimeSeries(object):

    def GETRequest(self,req_str,datatype='json'):
        
        try:
            response = request.get_request(req_str)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            sys.exit(1)

        if datatype == 'json':
            # dictionary of json reponse is returned
            return response.json()
        else:
            print('CSV Downloaded.')








