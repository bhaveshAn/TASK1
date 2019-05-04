import pandas as pd


class Patch(object):

    def __init__(self, name):
        self.name = name
        # self.dataframe = pd.read_csv('{0}.csv'.format(self.name.upper()))

    def rd(self, rd):
        self.df = pd.read_csv('{0}.csv'.format(rd), parse_dates=True)
        if 'Open' not in self.df and 'High' not in self.df and 'Low' not in self.df and 'Close' not in self.df:
            for col in self.df.columns:
                if self.df[col].dtype == 'float64':
                    float_col = col
                    break            
            self.df = self.df[float_col].resample('1Day').ohlc()
        patched_rd = self.df.head()
        return patched_rd.values.tolist()

    def datt(self, datt):
        self.df.columns =[column.replace(" ", "_") for column in self.df.columns]
        query = ''
        c = 0
        nos = len(datt.keys())
        for key in datt:
            query = key + ' == ' + str(datt[key])
            c += 1
            if c < nos:
                query += ' and '
        patched_datt = self.df.query(query)
        return patched_datt.to_dict()

    def label(self, label):
        self.df['Label'] = str(label) if not 'Label' in self.df.columns or not self.df['Label'] else self.df['Label'] 
        return self.df.to_dict()

    def time_label(self, time_label):
        self.df['Time Label'] = str(time_label) if not 'Time Label' in self.df.columns or not self.df['Time Label'] else self.df['Time Label']
        return self.df.to_dict()
'''
patch = Patch('ibm')
print(patch.rd('IBM'))
print(patch.datt({'Open': 143.619995, 'Close': 142.779999, 'Volume': 12525700}))
print(patch.label('New'))
print(patch.time_label('2019-01-01'))
'''
