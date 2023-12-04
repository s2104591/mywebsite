import plotly.express as px
import pandas as pd




df = px.data.gapminder().query('year==2007')
px.sunburst( data_frame=df, path=['country'], values='pop',color='pop' )
