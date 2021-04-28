
from random import choice
import pandas as pd

randomlist = []

for j in range(1, 282):
    z_list = []
    while len(z_list) < 11:
        n = random.randint(1,30)
        if n not in z_list:
            z_list.append(n)
    converted_list = [str(element) for element in z_list]
    joined_string = ",".join(converted_list)
    randomlist.append([joined_string])


df = pd.DataFrame(randomlist)
df.to_csv(r'/Users/colinmason/Desktop/Personal/random_values.csv')

education = ['Educational', 'Non-Educational']
parent_ra = ['Parent', 'RA']


list_edu = []
list_par = []
for _ in range(1, 282):
    list_edu.append(choice(education))
    list_par.append(choice(parent_ra))

list_master = [list_edu, list_par]
print(list_master)

df = pd.DataFrame(list_master)
df = df.transpose()
df.columns = ['Heading1', 'Heading2']

df.to_csv(r'/Users/colinmason/Desktop/Personal/random_values2.csv')
