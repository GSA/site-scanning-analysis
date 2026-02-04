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
            'How many urls are sourced from DAP?': self.num_true('source_list_dap'),
            'How many urls are sourced from pulse?': self.num_true('source_list_pulse'),
            'How many urls are sourced from OMB IDEA?': self.num_true('source_list_omb_idea'),
            'How many urls are sourced from EOTW?': self.num_true('source_list_eotw'),
            'How many urls are sourced from USA.gov?': self.num_true('source_list_usagov'),
            'How many urls are sourced from Gov Manual?': self.num_true('source_list_gov_man'),
            'How many urls are sourced from US Courts?': self.num_true('source_list_uscourts'),
            'How many urls are sourced from OIRA?': self.num_true('source_list_oira'),
            'How many urls are sourced from other?': self.num_true('source_list_other'),
            'How many urls are sourced from MIL 1?': self.num_true('source_list_mil_1'),
            'How many urls are sourced from MIL 2?': self.num_true('source_list_mil_2'),
            'How many urls are sourced from DOD Public?': self.num_true('source_list_dod_public'),
            'How many urls are sourced from dotmil?': self.num_true('source_list_dotmil'),
            'How many urls are sourced from final URL websites?': self.num_true('source_list_final_url_websites'),
            'How many urls are sourced from House 117th?': self.num_true('source_list_house_117th'),
            'How many urls are sourced from Senate 117th?': self.num_true('source_list_senate_117th'),
            'How many urls are sourced from GPO FDLP?': self.num_true('source_list_gpo_fdlp'),
            'How many urls are sourced from CISA?': self.num_true('source_list_cisa'),
            'How many urls are sourced from DOD 2025?': self.num_true('source_list_dod_2025'),
            'How many urls are sourced from DAP 2?': self.num_true('source_list_dap_2'),
            'How many urls are sourced from USA.gov clicks?': self.num_true('source_list_usagov_clicks'),
            'How many urls are sourced from USA.gov clicks MIL?': self.num_true('source_list_usagov_clicks_mil'),
            'How many urls are sourced from Search.gov?': self.num_true('source_list_search_gov'),
            'How many urls are sourced from Search.gov MIL?': self.num_true('source_list_search_gov_mil'),
            'How many urls are sourced from public inventory?': self.num_true('source_list_public_inventory'),
            'How many blank cells are there in the target URL list?': self.num_blank(),
        }

    def num_records(self):
        return len(self.df.index)

    def num_true(self, field):
        return len(self.df.loc[self.df[field] == True])

    def num_false(self, field):
        return len(self.df.loc[self.df[field] == False])

    def num_unique(self, field):
        return len(pd.unique(self.df[field]))

    def num_na(self, field):
        return len(self.df.loc[self.df[field].isna()])

    def num_not_na(self, field):
        return len(self.df.loc[self.df[field].notna()])

    def num_blank(self):
        return self.df.isna().sum().sum()

    def num_blank_without_omb_idea_public(self):
        temp_df = self.df.drop(columns=['omb_idea_public'])
        return temp_df.isna().sum().sum()

    def num_omb_idea_public(self):
        return self.df['omb_idea_public'].notna().sum()
