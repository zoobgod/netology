import pandas as pd

df = pd.read_csv('URLs.txt', header=None, names=['url'])

df = df[df['url'].str.contains(r'\/\d{8}\-')]

print(df)