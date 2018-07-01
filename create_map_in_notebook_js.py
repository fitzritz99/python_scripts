#Use the following to create a map in jupyter notebook. An existing dataframe is a prerequisite for using the code.  Run each piece of code in a new cell.  Refer to the following website for more info: https://www.ryanbaumann.com/blog/2016/4/3/embedding-mapbox-plots-in-jupyter-notebooks

#create test dataframe if desired
import pandas as pd

#data = {'Latitude' : [45, 46, 47, 48],
#        'Longitude' : [-120, -121, -122, -123]}
#data_df = pd.DataFrame(data)
#data_df

#Converts a dataframe to a geojson Point output
def df_to_geojson(data_df, properties, lat='Latitude', lon='Longitude'):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in data_df.iterrows():
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson

#

cols = []
geojson = df_to_geojson(data_df, cols)
center = [data_df.Longitude.mean(), data_df.Latitude.mean()]

#

from IPython.display import Javascript
Javascript("""window.vizObj={};""".format(geojson))

#

Javascript("""window.cenObj={};""".format(center))

#

from IPython.display import HTML
HTML("""
<style> #map {
  position: relative;
  width: auto;
  height: 650px;
  overflow:visible;
}
</style>
""")

#

%%javascript
require.config({
  paths: {
      mapboxgl: 'https://api.tiles.mapbox.com/mapbox-gl-js/v0.21.0/mapbox-gl',
      bootstrap: 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min'
  }
});

#

%%javascript
IPython.OutputArea.auto_scroll_threshold = 9999;
require(['mapboxgl', 'bootstrap'], function(mapboxgl, bootstrap){
    mapboxgl.accessToken = 'pk.eyJ1IjoibmZpdHpwYXRyaWNrIiwiYSI6ImNqMmpkZDM3MzAxaHoyd211ZWprejFna2EifQ.eoC9DVtUZTWUGVxy9VlE4w';
    var map = new mapboxgl.Map({
        container: 'map', // container id
        style: 'mapbox://styles/mapbox/light-v9', //stylesheet location
        center: window.cenObj, //[-39.14586151999999, -16.505109735999998],// starting position
        zoom: 6, // starting zoom
        pitch: 1 // pitch in degrees
    });


    function addSegLayer(mapid) {
        // Mapbox GL JS Api - import segment
        var segment_src = new mapboxgl.GeoJSONSource({
            data: window.vizObj,
            maxzoom: 18,
            buffer: 1,
            tolerance: 1
        });
        try {
            mapid.addSource('points', segment_src);
            mapid.addLayer({
                id: 'points',
                type: 'circle',
                source: 'points',
                paint: {
                    "circle-radius": 8,
                    "circle-color": 'chartreuse',
                }
            });
        } catch (err) {
            console.log(err);
        }
    };

    map.once('style.load', function(e) {
        addSegLayer(map);
        map.addControl(new mapboxgl.Navigation({
            position: 'top-left'
        }));
    });
    //map.setPitch(1);

});
element.append("<div id='map'></div>"); //style=width: 1500px; height: 1500px;
