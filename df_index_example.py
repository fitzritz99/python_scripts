purchase_1 = pd.Series({'Name': 'Chris','Item Purchased': 'Dog Food','Cost': 22.50})

purchase_2 = pd.Series({'Name': 'Kevyn','Item Purchased': 'Kitty Litter','Cost': 2.50})

purchase_3 = pd.Series({'Name': 'Vinod','Item Purchased': 'Bird Seed','Cost': 5.00})


df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])



df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']

df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))

df

#adds new column with None values
df['Location'] = None

#adds new column from index values
df['country'] = df.index

#adds new row with values
df.loc['L'] = 'Bears'

#renaming columns and trimming the original names
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='?':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 

df.head()

#select from multiple index values
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]