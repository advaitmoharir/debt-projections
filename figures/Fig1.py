# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:03:27 2020

@author: Advait Moharir
"""
import pandas as pd
import matplotlib as mpl
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
pio.renderers.default='jpeg'
px.defaults.height=700
px.defaults.width=500
#figure-1
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig1.csv')
df=pd.DataFrame(data)
fig = px.line(df, x='Year', y=['Gross Fiscal Deficit', '3% line'],
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes(tick0=0, tickvals=[0,1,2,3,4,5,6])
fig.update_xaxes(tick0=2004, dtick=2)
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()
#figure-2
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig2_3.csv')
df1=pd.DataFrame(data)
fig = px.line(df1, x='Year', y=['Debt/GDP', '60% line'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes(tick0=45, dtick=10)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=45,
            x1=1991,
            y1=90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=45,
            x1=1996,
            y1=90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=45,
            x1=2004,
            y1=90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2010,
            y0=45,
            x1=2010,
            y1=90,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()
#Figure 3
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig2_3.csv')
df2=pd.DataFrame(data)
fig = px.line(df2, x='Year', y=['Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400)
fig.update_yaxes(tick0=-5, dtick=5)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-2,
            x1=1991,
            y1=15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-2,
            x1=1996,
            y1=15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-2,
            x1=2004,
            y1=15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2010,
            y0=-2,
            x1=2010,
            y1=15,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()

#Figure 4
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig 4.csv')
df3=pd.DataFrame(data)
fig = px.line(df3, x='Year', y=['20% Line', 'Debt/GDP'], 
              labels={'value':'', 'variable':''}, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes( nticks=10)
fig.update_xaxes(nticks=20)
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()

#Figure 5
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig5_6.csv')
df4=pd.DataFrame(data)
fig = px.line(df4, x='Year', y='Debt/GSDP', 
              labels={'value':'', 'variable':'', 'Debt/GSDP': '', 
                      'Year':''}, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes( nticks=10)
fig.update_xaxes(nticks=10)
fig.show()

#Figure 6
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig5_6.csv')
df5=pd.DataFrame(data)
fig = px.line(df5, x='Year', y=['Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400)
fig.update_yaxes(tick0=-5, dtick=5)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-5,
            x1=1991,
            y1=20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-5,
            x1=1996,
            y1=20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-5,
            x1=2004,
            y1=20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-5,
            x1=2013,
            y1=20,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()



#Figure 7
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig7.csv')
df6=pd.DataFrame(data)
fig = px.line(df6, x='Year', y=['AP', 'BH', 'GJ', 'KT', 'MH',
                                'MP', 'RJ', 'TN', 'UP', 'WB'],
              labels={'value':'', 'variable':'', 'Year':'' }, 
              line_shape='spline', template='plotly_white')
fig.update_yaxes( nticks=10)
fig.update_xaxes(nticks=20, showgrid=False)
fig.show()

#Figure 9
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Fig9.csv')
df7=pd.DataFrame(data)
fig = px.line(df7, x='Year', y=['Madhya Pradesh', 'Tamil Nadu'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400)
fig.update_yaxes(tick0=15, dtick=5)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=15,
            x1=1991,
            y1=40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=15,
            x1=1996,
            y1=40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=15,
            x1=2004,
            y1=40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=15,
            x1=2013,
            y1=40,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
fig.show()

#Appendix Figures

#AP
data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Figure C1_a.csv')
df5=pd.DataFrame(data)
fig = px.line(df5, x='Year', y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Andhra Pradesh")
fig.update_yaxes(tick0=-5, dtick=15)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-40,
            x1=1991,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-40,
            x1=1996,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-40,
            x1=2004,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-40,
            x1=2013,
            y1=60,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1,
    xanchor="center",
    x=0.5
))
fig.show()

#BH

data=pd.read_csv(r'C:\Users\hp\Dropbox\Debt Paper\Data\Figure C1_b.csv')
df5=pd.DataFrame(data)
fig = px.line(df5, x='Year', y=['Debt/GSDP','Interest Rate', 'Real Growth', 'Inflation', 'Primary Deficit'], 
              labels={'value':'', 'variable':'', 'Year':''}, 
              line_shape='spline', template='plotly_white', 
              width=800, height=400, title= "Bihar")
fig.update_yaxes(tick0=-5, dtick=15)
fig.update_xaxes(tick0=1980, dtick=2)
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1991,
            y0=-40,
            x1=1991,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=1996,
            y0=-40,
            x1=1996,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2004,
            y0=-40,
            x1=2004,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=2013,
            y0=-40,
            x1=2013,
            y1=80,
            line=dict(
                color="Grey",
                width=2
            )
))
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1,
    xanchor="center",
    x=0.5
))
fig.show()






