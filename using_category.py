s = pd.Series([168, 180, 174, 190, 170, 185, 179, 181, 175, 169, 182, 177, 180, 171])



pd.cut(s, 3)


# You can also add labels for the sizes [Small < Medium < Large].

pd.cut(s, 3, labels=['Small', 'Medium', 'Large'])