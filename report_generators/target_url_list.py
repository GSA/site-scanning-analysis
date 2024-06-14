import pandas as pd


class TargetUrlList:
    def __init__(self, df):
        self.df = df

    def generate_report(self):
        return {
            'How many target urls are in the list?': self.num_records(),
            'How many unique base domains are in the list?': self.num_unique('base_domain'),
            'How many unique agencies are in the list?': self.num_unique('agency'),
            'How many unique bureaus are in the list?': self.num_unique('bureau'),
            'How many urls are sourced from the list of federal domains?': self.num_true('source_list_federal_domains'),
            'How many urls are sourced from pulse?': self.num_true('source_list_pulse'),
            'How many urls are sourced from DAP?': self.num_true('source_list_dap'),
            'How many urls are sourced from the other websites list?': self.num_true('source_list_other'),
            'How many blank cells are there in the target URL list?': self.num_blank(),
        }

    def num_records(self):
        return len(self.df.index)

    def num_true(self, field):
        return len(self.df.loc[self.df[field] == True])

    def num_unique(self, field):
        return len(pd.unique(self.df[field]))

    def num_na(self, field):
        return len(self.df.loc[self.df[field].isna()])

    def num_not_na(self, field):
        return len(self.df.loc[self.df[field].notna()])

    def num_blank(self):
        return self.df.isna().sum().sum()
