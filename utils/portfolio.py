from pandas import DataFrame
import numpy as np
import pandas as pd

from utils.transform import Transform

class RebalStrategy:
    def has_to_rebalance(self, count, cur_value, cur_percentages, perc_diff, diff_amount) -> bool:
        raise NotImplementedError

class RebalDays(RebalStrategy):
    def __init__(self, days_rebalance):
        self.days_rebalance = days_rebalance

    def has_to_rebalance(self, count, cur_value, cur_percentages, perc_diff, diff_amount) -> bool:
        return count == self.days_rebalance

    def __str__(self):
        return str(self.days_rebalance)+" days"
    
class RebalThreshold(RebalStrategy):
    def __init__(self, threshold):
        self.threshold = threshold

    def has_to_rebalance(self, count, cur_value, cur_percentages, perc_diff, diff_amount) -> bool:
        return [ abs(pdiff) > self.threshold for (asset, pdiff) in perc_diff] != [ False for i in range(len(perc_diff)) ]

    def __str__(self):
        return str(self.threshold)+" percent"

class Portfolio(Transform):
    def __init__(self, amount, rebal_strat=RebalDays(25), days_before=1000):
        """
        asset_percent_list of the form [ ('asset',percent), ... ]
        """
        self.amount = amount
        self.days_before = days_before
        self.rebal_strat = rebal_strat

    def apply(self, df: DataFrame) -> DataFrame:
        days_before = max([self.days_before, len(df)])
        asset_percent_list = [ (asset, 1/len(df.columns)) for asset in df.columns ]
        start_price = df.tail(days_before).iloc[0]
        print(asset_percent_list)
        print('start_price: ' + str(start_price))
        start_investment = [ (asset, self.amount * percent) for (asset, percent) in asset_percent_list ]
        start_quote_num = [ ( asset, inv / start_price[asset] ) for (asset, inv) in start_investment ]
        cur_quote_num = start_quote_num
        print('cur_quote_num: ' + str(cur_quote_num))
        print('start_investment: ' + str(start_investment))
        values = []
        count = 0
        first_time = 0
        for i in range(len(df.tail(days_before))):
            price = df.tail(days_before).iloc[i].to_frame().T
            #[ print(f'price {asset}: ' + str(price[asset].iat[0])) for (asset, quote_num) in cur_quote_num ]
            cur_value = [ ( asset, quote_num * price[asset].iat[0] ) for (asset, quote_num) in cur_quote_num ]
            total_value = sum([price for (asset, price) in cur_value ])
            #print('====')
            #print(cur_value)
            #print(total_value)
            #print('====')
            values.append(total_value)
            cur_percentages = [ ( asset, price / total_value ) for (asset, price) in cur_value ]
            perc_diff = [ (asset1, perc - cur_perc) for (asset1, cur_perc) in cur_percentages \
                            for (asset2, perc) in asset_percent_list if asset1==asset2 ]
            diff_amount = [ (asset1, value * diff) for (asset1, diff) in perc_diff \
                            for (asset2, value) in cur_value if asset1==asset2 ]
            if self.rebal_strat.has_to_rebalance(count, cur_value, cur_percentages, perc_diff, diff_amount):
                #print(count)
                #print('rebalancing perc_diff: ' + str(perc_diff))
                #print('rebalancing cur_value: ' + str(cur_value))
                first_time += 1
                count = 0
                diff_quotes = [ (asset, diff_amt / price[asset].iat[0]) for (asset, diff_amt) in diff_amount ]
                if first_time == 1:
                    print('diff_quotes: ' + str(diff_quotes))
                new_quotes = [ (asset1, old_quotes + diff_q) for (asset1, diff_q) in diff_quotes \
                                for (asset2, old_quotes) in cur_quote_num if asset1==asset2 ] 
                if first_time == 1:
                    print('new_quotes: ' + str(new_quotes))
                cur_quote_num = new_quotes
            count += 1
        print('len(df): ' + str(len(df.tail(days_before))))
        print('len(values): ' + str(len(values)))
        roi = [ (value - self.amount) / self.amount for value in values ]
        new_df = DataFrame(list(zip(values, roi)), columns=['Portfolio', 'ROI'])
        #new_df = pd.concat([new_df, df.index], axis=1)
        #new_df['Date'] = new_df['Date'].astype('datetime64')
        new_df = new_df.set_index(df.tail(days_before).index)
        #new_df = pd.concat([new_df, df], axis=1)

        # TODO bring out relative plot logic!
        #for c in new_df.columns:
        #    try:
        #        new_df[c] = new_df[c] / max(new_df[c]) 
        #    except:
        #        print(new_df[c])
        print(values[0])
        print(values[len(values)-1])
        return DataFrame(new_df['ROI'], columns=['ROI'])

    def __str__(self):
        return "Portfolio<"+str(self.rebal_strat)+">"
