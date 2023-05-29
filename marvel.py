import pandas as pd

col = {
    'MarvalHero':['Captain America','IronMan','SpiderMan','HawkEye','Hulk'],
    'Avenger':['Yes','Yes','No','Yes','Yes'],
}
df = pd.DataFrame(col)
df.set_index('MarvalHero',inplace=True)
print(df)