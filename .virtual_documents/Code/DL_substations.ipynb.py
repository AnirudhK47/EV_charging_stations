import pandas as pd


d = pd.read_html('http://dtl.gov.in/content/326_1_ListofSubstations.aspx')


dfa = d[0]
dfb = d[1]


dfa['Voltage Class'] = '400 kV'
dfb['Voltage Class'] = '220 kV'


df = dfa.append(dfb, ignore_index=True)


df.to_csv('Substation_list_Delhi.csv')



