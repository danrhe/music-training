import cPickle as pickle
import pandas as pd
from credentials import *
from sqlalchemy import *

class User_data(object):
    def __init__(self, uid):
        self.filename = "user_" + uid + '.pkl'

    def export_data(self):
        with open('cache/' + self.filename, 'wb') as output:
            pickle.dump(self.data, output, -1)

    def get_local_data(self):
        with open(self.filename, 'rb') as input:
            self.data = pickle.load(input)

    def get_db_data(self):
        engine = create_engine('mysql://' + user_id + ":" + password + '@' + host + '/' + user_db + '?charset=utf8&use_unicode=0', pool_recycle=3600)
        con = engine.connect()
        self.data = pd.read_sql_table('Raw', con)
        con.close()

    def calc_hitrate(self):
        hit_rate = pd.pivot_table(self.data, values='rt', index=['clef', 'note'], columns='hit', aggfunc='count')
        hit_rate.fillna(0)

        hr2 = pd.crosstab([self.data.clef, self.data.note],self.data.hit)
        hr2.perc = hr2.correct / (hr2.correct + hr2.wrong) * 100
        hr2.perc = hr2.perc.to_frame()
        hr2.perc.columns = ['perc']
        self.perc = hr2.perc.reset_index()

    def get_bad_performance(self):
        self.bad = self.perc[self.perc.perc < self.perc.perc.quantile(0.4)].dropna()

    def make_selection(self, allnotes):
        self.selection = list();

        for index, row in self.perc.iterrows():
            correct_clef = [x for x in allnotes if x['clef'] in row.clef]
            exact_note = [x for x in correct_clef if x['key'] == row.note]
            self.selection.append(exact_note[0])



