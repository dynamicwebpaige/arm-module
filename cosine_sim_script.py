import json
import pandas as pd
from collections import Counter
import numpy as np

with open('dirs_with_resources.json', 'r') as f:
   jsondump = json.load(f)

def cosine_similarity(a, b):
   a_vals = Counter(a)
   b_vals = Counter(b)

   # Convert to word-vectors
   words = list(set(a_vals) | set(b_vals))
   a_vect = [a_vals.get(word, 0) for word in words]
   b_vect = [b_vals.get(word, 0) for word in words]
  
   # Find cosine similarity.
   len_a = sum(av*av for av in a_vect) ** 0.5
   len_b = sum(bv*bv for bv in b_vect) ** 0.5
   dot = sum(av*bv for av,bv in zip(a_vect, b_vect))
   cosine = dot / (len_a * len_b)

   return cosine

cosines_dict = {}

for i in jsondump.items():
   holder = []
   for j in jsondump.items():
      try:
         holder.append(cosine_similarity(i[1], j[1]))
      except:
         holder.append(0.0)
   cosines_dict[i[0]] = holder

df = pd.DataFrame.from_dict(cosines_dict, orient='index')
df.to_csv('heatmap_values.csv')
