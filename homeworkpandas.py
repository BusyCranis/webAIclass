import pandas as pd



csv_data = pd.read_csv('my_data.csv')
print(type(csv_data))


df = pd.DataFrame(csv_data)
print(type(df))


df = df.drop('Unnamed: 0', axis=1)
print(df)


# df['name'] = 0


df.loc[0, 'name'] = '한글이름'
df.loc[1, 'name'] = '영어이름'

print(df)



df.to_csv('basedata.csv')






