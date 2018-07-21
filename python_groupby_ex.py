import pandas as pd

data = {'Country' : ['USA', 'USA', 'CAN', 'MEX', 'USA'],
        'Value1' : [1, 2, 3, 4, 5],
       'Value2': [10, 16, 15, 16, 16]}
data_df = pd.DataFrame(data)
#data_df

count_unique = data_df.groupby(['Country','Value2']).size().groupby(level=0).agg({'ValueCount':'size'}).reset_index()

count_by_group = data_df.groupby('Country')['Country'].agg({'Count':'count'}).reset_index()

count_by_group = count_by_group.merge(count_unique,on=['Country'])
print (count_by_group)


print(df.groupby('Category').apply(lambda df,a,b: sum(df[a] * df[b]), 'Weight (oz.)', 'Quantity'))

%%timeit -n 10
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
    print('Counties in state ' + group + ' have an average population of ' + str(avg))
    
