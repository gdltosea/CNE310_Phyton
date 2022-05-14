import pandas as pd

data = {
  "names": ['a', 'b', 'c', 'd'],
  "ages": [50, 40, 45, 20],
  "relations": ['', '', '', '']
}
rel_list = [('a', 'b'), ('a', 'c'), ('c', 'd')]

df = pd.DataFrame(data)

for rel_tuple in rel_list:
  head = rel_tuple[0]
  tail = rel_tuple[1]

  df.loc[df.names == head, 'relations'] = tail

print(df)
