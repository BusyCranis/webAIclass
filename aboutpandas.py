import pandas as pd



csv_data = pd.read_csv('my_data.csv')
print(type(csv_data))


df = pd.DataFrame(csv_data)
print(type(df))


df = df.drop('Unnamed: 0', axis=1)
print(df)


# df.loc[0, 'name'] = '한글이름'
# df.loc[1, 'name'] = '영어이름'


targetcol = "name"
kordict = {"Alice": "엘리스", "Bob": "밥", "Charlie": "찰리", "james": "제임스"}

for idx, value in enumerate(df[targetcol].values):
    df.at[idx, targetcol] = kordict[value]



print(df)


tar0getcol = "salary"
df[tar0getcol] = df[tar0getcol].apply(lambda x: '{:,}'.format(x))



print(df)





df.to_csv('basedata.csv')






