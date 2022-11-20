from pandas_datareader import data as wb
from os.path import exists
import pandas as pd

BASE_DIR = './'

def import_from_source(tickers, source='yahoo', start='2010-1-1'):
    """
    Imports data of a list of assets from a certain date. If already downloaded,
    use cached file.
    
    Parameters
    ----------
    tickers : list of str
        List of tickers for asset prices
    source: str
        String representing data source. Accepted: yahoo
    start : str
        Date in yyyy-MM-dd format
        
    Returns
    -------
    pandas.DataFrame [tickers]
    """

    tickers.sort()
    filename = BASE_DIR+'assets_' + '_'.join(tickers) + '_' + start + '.csv'

    if exists(filename):
        return pd.read_csv(filename)
        #data['Date'] = data['Date'].astype('datetime64')
        #data = data.set_index('Date')

    data = pd.DataFrame()
    if len([tickers]) ==1:
        data[tickers] = wb.DataReader(tickers, data_source='yahoo', start = start)['Adj Close']
    else:
        for t in tickers:
            data[t] = wb.DataReader(t, data_source='yahoo', start = start)['Adj Close']
    data.to_csv(filename)
    return(data)
