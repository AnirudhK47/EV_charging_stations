import pandas as pd
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_Namma_Metro_stations")
dfa = df[1]
dfa.to_csv('test.csv')