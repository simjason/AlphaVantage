from AlphaVantage import AlphaVantage

av = AlphaVantage('ZDO88YHQRG97NEZL')
ts = av.StockTimeSeries
ts.get_Intraday('msft')