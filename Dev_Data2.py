
# coding: utf-8

# In[36]:

########
# import packages

# Data handling
import pandas as pd

# Interactivity
from IPython.display import display
from ipywidgets import interactive, Select, Output

# Plotting (Plot.ly offline mode)
import plotly
from plotly import graph_objs as go
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=False)


# In[44]:

########
# Parameters and data loading

# load some dataframes
dev_data = pd.read_csv('/Users/Shea/Desktop/Python Project/d7.csv')


# In[38]:

# rename column with year values 'Year'
dev_data2 = dev_data.rename(columns = {'Unnamed: 1':'Year'})


# In[48]:

######## 
# define observations & facets dataframes
OBS_DF = dev_data2
FCST_DF = dev_data2


# In[40]:

######## 
# Define variables for drop-downs - copy & paste from above
COUNTRIES = {'Afghanistan':1, 'Albania':2, 'Algeria':3, 'American Samoa':4, 'Andorra':5}

COUNTRY_NAMES = sorted(COUNTRIES.keys())

INDICATORS = ['GDP growth (annual %)', 'Population growth (annual %)', 'Inflation, GDP deflator (annual %)']

YEARS = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
       2011, 2012, 2013, 2014, 2015]


# In[49]:

# Widget for selecting a country
COUNTRIES_WIDGET = Select(
    options = COUNTRIES,
    description='Country',
    height='142px',
    width='250px'
)

display(COUNTRIES_WIDGET)


# In[50]:

# Widget for selecting an indicator
INDICATORS_WIDGET = Select(
    options = INDICATORS,
    description='Series',
    height='80px',
    width='250px'
)

display(INDICATORS_WIDGET)


# In[51]:

PLOT_OUTPUT = Output()
display(PLOT_OUTPUT)


# In[ ]:




# In[54]:

def update_plot_output(*args, **kwargs):
    Country = COUNTRIES_WIDGET.value
    Series = INDICATORS_WIDGET.value
    
    PLOT_OUTPUT.clear_output()
    with PLOT_OUTPUT:
        iplot_scatter(Country, Series)

COUNTRIES_WIDGET.observe(update_plot_output)
INDICATORS_WIDGET.observe(update_plot_output)

