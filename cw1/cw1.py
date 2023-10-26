import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), 'transactions.csv')

df = pd.read_csv("transactions.csv")