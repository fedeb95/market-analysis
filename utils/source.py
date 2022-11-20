from pandas_datareader import data as wb
from os.path import exists
import pandas as pd
from pandas import DataFrame

BASE_DIR = './'

class Source:
    def get_data(self, tickers: list[str], source='yahoo', start='2010-1-1') -> DataFrame:
        raise NotImplementedError("this is just an interface")

class DataSource(Source):
    def get_data(self, tickers, source='yahoo', start='2010-1-1'):
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
            data = pd.read_csv(filename)
            data['Date'] = data['Date'].astype('datetime64')
            data = data.set_index('Date')
            return data

        data = pd.DataFrame()
        if len([tickers]) ==1:
            data[tickers] = wb.DataReader(tickers, data_source='yahoo', start = start)['Adj Close']
        else:
            for t in tickers:
                data[t] = wb.DataReader(t, data_source='yahoo', start = start)['Adj Close']
        data.to_csv(filename)
        return(data)
