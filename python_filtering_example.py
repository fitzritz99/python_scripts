import pandas as pd

data1 = {'ID': [1,2,3,4],
        'Latitude' : [45, 46, 47, 48],
        'Longitude' : [-120, -121, -122, -123]}
data_df1 = pd.DataFrame(data1)

data2 = {'ID': [1,2,3,4],
        'Latitude' : [45, 50, 55, 60],
        'Longitude' : [-120, -125, -130, -135]}
data_df2 = pd.DataFrame(data2)

new_df = data_df1[(data_df1.Longitude != data_df2.Longitude) & (data_df1.ID == data_df2.ID)]