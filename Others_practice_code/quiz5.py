import pandas as pd

df = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6]
})


filtered_df = df[df['A'] >1]
filtered_df['B'] = 100  #https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy 
                        # please visit this site for more details 





# r = df[df['A'] >0]
# print(r)

print(df.loc[1,'B'])

