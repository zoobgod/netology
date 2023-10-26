import pandas as pd

df = pd.read_csv('visit_log.csv', sep=';')

df['source_type'] = df['traffic_source'].apply(lambda x: 'organic' if x in ['yandex', 'google'] else 'ad' if x in ['paid', 'email'] and df['region'].iloc[0] == 'Russia' else 'other' if x in ['paid', 'email'] else x)

print(df)