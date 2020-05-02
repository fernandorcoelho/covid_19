# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

data = pd.read_csv('brazil_covid19.csv')
#Convert elements in data['date'] to date format (with day first)
data['date'] = pd.to_datetime(data['date'],dayfirst=True)
#Sum all cases and deaths at the same region in the same day
data_region = data.groupby(['date','region']).sum().reset_index()
#Grid on plot
sns.set_style("whitegrid")

#g->Figure instance; ax = Object (or array), indicates plot positions; size of plot
fig,ax = plt.subplots(2,figsize=(10,12))

#DateFormatter = How date will be show; Next line put axis X in the way I define
#by DateFormatter; Next line I declare space between dates = 1 week
date_form = DateFormatter("%d/%m")
ax[0].xaxis.set_major_formatter(date_form)
ax[0].xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
#Plot
fig1 = sns.lineplot(data=data_region,x='date',y='cases',
                   hue='region',marker='o',ax=ax[0])
ax[0].set_title(u'Evolução dos casos de COVID-19 no Brasil')
#Definig legend title
legend1 = ax[0].legend()
legend1.texts[0].set_text(u"Região")
ax[0].set_xlabel('Datas')
ax[0].set_ylabel(u'Nº de Casos')
#first and last ticks on X axis
ax[0].set(xlim=['2020-01-30','2020-04-21'])

fig2 = sns.lineplot(data=data_region,x='date',y='deaths',
                   hue='region',marker='o',ax=ax[1])
ax[1].xaxis.set_major_formatter(date_form)
ax[1].xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax[1].set_title(u'Evolução das mortes por COVID-19 no Brasil')
legend2 = ax[1].legend()
legend2.texts[0].set_text(u"Região")
ax[1].set_xlabel('Datas')
ax[1].set_ylabel(u'Nº de Mortes')
ax[1].set(xlim=['2020-01-30','2020-04-21'])

#Here im rotating/aligning both X ticks and adjusting plots to not overlap 
plt.setp(ax[0].get_xticklabels(), rotation=45, ha="right")   # optional
plt.setp(ax[1].get_xticklabels(), rotation=45, ha="right")
fig.subplots_adjust(bottom=-0.2)