
# coding: utf-8

# Launch Jupyter with this to prevent error about data rate limit:
# 
# jupyter notebook --NotebookApp.iopub_data_rate_limit=10000000000
# 
# Source: https://github.com/jupyter/notebook/issues/2287

# In[5]:

########
# import packages

# Data handling
import pandas as pd
from pandas import Series, DataFrame, Panel
import numpy as np
import matplotlib.pyplot as plt
import requests
import matplotlib
matplotlib.style.use('ggplot')

# Interactivity
from IPython.display import display
from ipywidgets import interactive, Select, Output

# Plotting (Plot.ly offline mode)
import plotly as py
from plotly import graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=False)


# In[19]:

data = pd.read_csv("/Users/Shea/Desktop/Python Project/data from Vinay/world-bank.csv",encoding ='latin1',index_col = False)
data2 = data.drop(['Series Code', 'Country Code'], axis=1)


# In[20]:

data


# In[21]:

data2


# In[8]:

# load data
dev_data = pd.read_csv('/Users/Shea/Desktop/Python Project/Popular Indicators (3)/test_Data.csv')
dev_data


# In[ ]:

# make function for country-based data
# make plot w/ traces
# make function to combine both


# In[22]:

# make function for country-based data
def country_based_data(country_name,file,series):
    data2=file
    series_name=series
    infla_data1 = data2[data2["Series Name"] == series_name]
    country_data = infla_data1['Country Name'] == country_name
    infla_data1 = infla_data1[country_data]
    infla_data1 = infla_data1.drop(['Series Name', 'Country Name'], axis=1)
    row1 = infla_data1.iloc[0]
    row1 = row1.astype(float)
    row1.plot(kind='line', x='Year', y='Value')
    plt.title(country_name + " -" + series_name)
    plt.show()


# In[ ]:

import pandas as pd
import plotly.plotly as py

get_ipython().system('pip install ipython[notebook]')
from ipywidgets import widgets 
from IPython.display import display
from plotly.graph_objs import *
from plotly.widgets import GraphWidget


# In[28]:

def update_plot(update):
    a = dev_data['Country Name'] == update['new']
    b = dev_data[a]
    data = b.groupby(dev_data['year'])['Country Name']
    
    x = []
    y = []
    
    for i in range(len(data)):
        x.append(dev_data.index[i])
        y.append(dev_data[i])
        
        graph.restyle({
            'x':[x],
            'y':[y],
        })
        
        graph.relayout({'title': 'Percent change in deveopment indicators for {}'.format(update['new'])})
        
w = widgets.Dropdown(
    options = list(dev_data['Country Name'].unique()),
    description = 'Country Name')

w.observe(update_plot, names = "selected_label")

figure = go.Figure(data = data_trace, layout = layout)
iplot(figure)

# add traces???
graph.add_traces(Scatter(x=[1,2,3], y=[5, 4, 5], name='another sample'))

display(w)


# In[26]:

# make plot w/ traces
# Plotting (Plot.ly offline mode)
import plotly
from plotly import graph_objs as go
import pandas as pd
import plotly.plotly as py

from ipywidgets import widgets 
from IPython.display import display
from plotly.graph_objs import *
from plotly.widgets import GraphWidget
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=False)


# define x, y's, & year

Year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]




#traces

trace1 = go.Scatter(
    x = Year,
    y = 'GDP per capita (current US$)',
    name = "GDP per capita (current US$)",
    text = 'Country Name')
    
trace2 = go.Scatter(
    x = Year,
    y = 'Population growth (annual %)',
    name = "Population growth (annual %)",
    text = 'Country Name')
    
trace3 = go.Scatter(
    x = Year,
    y = 'Inflation, consumer prices (annual %)',
    name = "Inflation, consumer prices (annual %)",
    text = 'Country Name')

    
    
data_trace = [trace1, trace2, trace3]

# edit layout
layout = go.Layout(
        title = "Development Indicators (Country/Year)",
        xaxis = dict(title = 'Year'),
        yaxis = dict(title = 'Percent Change')     
  )

figure = go.Figure(data = data_trace, layout = layout)
iplot(figure)


# In[ ]:

key_metric = w.observe(update_plot, names = "selected_label")
if key_metric== "Inflation":
    series1= "Inflation, consumer prices (annual %)"
    e=country_based_data(country,data2,series1)
    series2= "Inflation, GDP deflator (annual %)"
    e=country_based_data(country,data2,series2)
elif key_metric=="GDP":
    series1= "GDP per capita (current US$)"
    e=country_based_data(country,data2,series1)
    series2= "GDP (current US$)"
    e=country_based_data(country,data2,series2)
    series3= "GDP growth (annual %)"
    e=country_based_data(country,data2,series3)
elif key_metric=="Population":
    #series1= "Population Total"
    #e=country_based_data(country,data2,series1)
    series2= "Population growth (annual %)"
    e=country_based_data(country,data2,series2)

