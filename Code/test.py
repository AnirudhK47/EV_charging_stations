import pandas as pd
df = pd.read_html("https://mybmtc.karnataka.gov.in/info-1/Depots/en")
dfa = df[0]
dfa.to_csv('depots.csv')