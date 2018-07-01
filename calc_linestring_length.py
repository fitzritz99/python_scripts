#this code presumes a dataframe and column with LINESTRING values exist
distance.VincentyDistance.ELLIPSOID = 'WGS-84'
dist = distance.distance

length_meters = []

for l, row in sa_lax_df.iterrows():
    line = loads(row.wkt_geom)
    xy = line.xy
# convert the coordinates to xy array elements, compute the distance, format: ((lat1,lon1),(lat2,lon2))
# for the length of the line segment loop through and get each distance pair
    for i in range(1,len(xy)):
        length_meters.append(dist((xy[1][i-1],xy[0][i-1]),(xy[1][i],xy[0][i])).meters)

#np.sum([mcd.dist_from_pt(xypairs[i-1][0],xypairs[i-1][1], xypairs[i][0],xypairs[i][1]) for i in range(1,len(xypairs))])
sa_lax_df['length_meters'] = length_meters
#print sa_bos_df['length_meters']