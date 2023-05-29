import pandas as pd

col = {
    'Name':['Karan','Rohan','Ganga'],
    'Marks':[90,96,81],
    'Subject':['Maths','Science','Hindi']
}
df = pd.DataFrame(col)
df.sort_values(by='Marks',inplace=True)
df.set_index('Name',inplace=True)
print(df)