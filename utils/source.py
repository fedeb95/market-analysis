from pandas_datareader import data as wb
import pandas as pd

def import_yahoo_close(tickers, start = '2010-1-1'):
    """
    Imports data of a list of assets from a certain date.
    
    Parameters
    ----------
    tickers : list of str
        List of tickers for asset prices
    start : str
        Date in yyyy-MM-dd format
        
    Returns
    -------
    pandas.DataFrame [tickers]
    """
    data = pd.DataFrame()
    if len([tickers]) ==1:
        data[tickers] = wb.DataReader(tickers, data_source='yahoo', start = start)['Adj Close']
    else:
        for t in tickers:
            data[t] = wb.DataReader(t, data_source='yahoo', start = start)['Adj Close']
    return(data)
