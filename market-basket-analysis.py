import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Import .csv file and convert to pandas dataframe
df = pd.read_csv('market-basket.csv')

# Obtain association rules

df_new = df.drop(df.columns[0], axis=1)
frequent_itemsets = apriori(df_new, min_support=0.07, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# print rules.head()

new_rules = rules[ (rules['lift'] >= 1) & (rules['confidence'] >= 0.8) ]

frequent_itemsets.to_csv('frequent-itemsets.csv')
new_rules.to_csv('rules.csv')

