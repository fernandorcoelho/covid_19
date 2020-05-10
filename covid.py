# Loading libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import seaborn as sns
import kaggle
# Handle date time conversions between pandas and matplotlib
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Authenticate API, Download and Unzip the CSV file from Kaggle
kaggle.api.authenticate()
kaggle.api.dataset_download_files('unanimad/corona-virus-brazil',
                                  'C:/Users/Usuario/Desktop/Nando/data_projects/covid_19/covid_download',
                                  unzip = True)

# Load the CSV file to df
file_path = 'covid_download/brazil_covid19.csv'
df = pd.read_csv(file_path)

## NOTE: ON THIS PROJECT WE ARE DEALING WITH ACCUMULATED NUMBER OF CASES
## AND DEATHS

# ---- PLOT NUMBER OF CASES -----
# Set the date column in date format
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
# Sum the states cases and deaths grouping by date
df_group_region = df.groupby(['date', 'region']).sum().reset_index()
# Defining the figure size and fig, ax
fig, ax = plt.subplots(3, figsize=(16, 14))
# Defining x and y
x_date = df_group_region['date']
y_cases = df_group_region['cases']
# Making a Lineplot using Seaborn
df_plot_cases = sns.lineplot(x_date, y_cases, hue='region',
                             data=df_group_region, marker="o", ax=ax[0])

# Define the date format
date_form = DateFormatter("%d/%m")
ax[0].xaxis.set_major_formatter(date_form)
# Ensure a major tick for each week using (interval=1)
ax[0].xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# Defining the plot title
title_casos = ("EVOLUÇÃO DE CASOS CONFIRMADOS DE COVID-19 NO BRASIL EM 2020")
ax[0].set_title(title_casos, fontsize=16)
# Set title and labels for axes and hue legend
legend_cases = ax[0].legend()
legend_cases.texts[0].set_text("Região")
ax[0].set_xlabel('Datas')
ax[0].set_ylabel('Nº de Casos', fontsize=14)
# Specifying the start and end of x
ax[0].set(xlim=['2020-01-30', '2020-04-25'])
# Setting the dates of x axis in diagonal
fig.autofmt_xdate()


# ---- PLOT NUMBER OF DEATHS -----
# Defining x and y
# x_dates already defined
y_deaths = df_group_region['deaths']
# Making a Lineplot using Seaborn
df_plot_cases = sns.lineplot(x_date, y_deaths, hue='region',
                             data=df_group_region, marker="o", ax=ax[1])

# Define the date format
date_form = DateFormatter("%d/%m")
ax[1].xaxis.set_major_formatter(date_form)
# Ensure a major tick for each week using (interval=1)
ax[1].xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# Defining the plot title
title_mortes = ("EVOLUÇÃO DE MORTES CAUSADA PELO COVID-19 NO BRASIL EM 2020")
ax[1].set_title(title_mortes, fontsize=16)
# Set title and labels for axes and hue legend
legend_cases = ax[1].legend()
legend_cases.texts[0].set_text("Região")
ax[1].set_xlabel('Datas')
ax[1].set_ylabel('Nº de Mortes', fontsize=14)
# Specifying the start and end of x_dates
ax[1].set(xlim=['2020-01-30', '2020-04-25'])
# Setting the dates of x axis in diagonal
fig.autofmt_xdate()


# ---- PLOT LETHALITY RATE -----
# Defining x and y
# x_dates already defined
# Handling with divisions by zero deaths
df_no_0cases = df_group_region.query('deaths > 0')
df_no_0cases['lethality rate (%)'] = (df_no_0cases['deaths']/df_no_0cases['cases'])*100
y_lethality_rate = df_no_0cases['lethality rate (%)']

# Making a Lineplot using Seaborn
df_plot_cases = sns.lineplot(x_date, y_lethality_rate, hue='region',
                             data=df_group_region, marker="o", ax=ax[2])

# Define the date format
date_form = DateFormatter("%d/%m")
ax[2].xaxis.set_major_formatter(date_form)
# Ensure a major tick for each week using (interval=1)
ax[2].xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
# Defining the plot title
title_mortes = ("EVOLUÇÃO DA TAXA DE LETALIDADE (%) POR COVID-19 NO BRASIL EM 2020")
ax[2].set_title(title_mortes, fontsize=16)
# Set title and labels for axes and hue legend
legend_cases = ax[2].legend()
legend_cases.texts[0].set_text("Região")
ax[2].set_xlabel('Datas')
ax[2].set_ylabel('Taxa de mortalidade (%)', fontsize=14)
# Specifying the start and end of x_dates
ax[2].set(xlim=['2020-01-30', '2020-04-25'])
# Setting the dates of x axis in diagonal
fig.autofmt_xdate()


# Displaying the grid on all the three plots
ax[0].grid()
ax[1].grid()
ax[2].grid()
