# Import libraries
from datetime import datetime
from meteostat import Point, Daily, units
import seaborn as sns

# Set plot style
sns.set_theme()

# Set time period
start = datetime(2022, 1, 1)
end = datetime(2022, 12, 31)

# Create Points for each city
chicago = Point(41.916256, -87.647254)
seattle = Point(47.606209, -122.332071)
austin = Point(30.267153, -97.743061)
denver = Point(39.739236, -104.990251)
las_vegas = Point(36.169941, -115.13983)
vancouver = Point(49.282729, -123.120738)
london = Point(51.507351, -0.127758)
bozeman = Point(45.6795, -111.042222)

# Get daily data for each city in Fahrenheit
chicago_data = Daily(chicago, start, end)
chicago_data = chicago_data.convert(units.imperial)
chicago_data = chicago_data.fetch()

seattle_data = Daily(seattle, start, end)
seattle_data = seattle_data.convert(units.imperial)
seattle_data = seattle_data.fetch()

austin_data = Daily(austin, start, end)
austin_data = austin_data.convert(units.imperial)
austin_data = austin_data.fetch()

denver_data = Daily(denver, start, end)
denver_data = denver_data.convert(units.imperial)
denver_data = denver_data.fetch()

las_vegas_data = Daily(las_vegas, start, end)
las_vegas_data = las_vegas_data.convert(units.imperial)
las_vegas_data = las_vegas_data.fetch()

vancouver_data = Daily(vancouver, start, end)
vancouver_data = vancouver_data.convert(units.imperial)
vancouver_data = vancouver_data.fetch()

london_data = Daily(london, start, end)
london_data = london_data.convert(units.imperial)
london_data = london_data.fetch()

bozeman_data = Daily(bozeman, start, end)
bozeman_data = bozeman_data.convert(units.imperial)
bozeman_data = bozeman_data.fetch()

# Get monthly averages for each city
chicago_monthly_data = chicago_data.groupby(chicago_data.index.month).mean()
seattle_monthly_data = seattle_data.groupby(seattle_data.index.month).mean()
austin_monthly_data = austin_data.groupby(austin_data.index.month).mean()
denver_monthly_data = denver_data.groupby(denver_data.index.month).mean()
las_vegas_monthly_data = las_vegas_data.groupby(las_vegas_data.index.month).mean()
vancouver_monthly_data = vancouver_data.groupby(vancouver_data.index.month).mean()
london_monthly_data = london_data.groupby(london_data.index.month).mean()
bozeman_monthly_data = bozeman_data.groupby(bozeman_data.index.month).mean()

# Plot relplots where the x-axis is the index and the y-axis is the tavg column
chicago_plot = sns.relplot(data=chicago_data, x=chicago_data.index, y="tavg", kind="line", aspect=2)
seattle_plot = sns.relplot(data=seattle_data, x=seattle_data.index, y="tavg", kind="line", aspect=2)
austin_plot = sns.relplot(data=austin_data, x=austin_data.index, y="tavg", kind="line", aspect=2)
denver_plot = sns.relplot(data=denver_data, x=denver_data.index, y="tavg", kind="line", aspect=2)
las_vegas_plot = sns.relplot(data=las_vegas_data, x=las_vegas_data.index, y="tavg", kind="line", aspect=2)
vancouver_plot = sns.relplot(data=vancouver_data, x=vancouver_data.index, y="tavg", kind="line", aspect=2)
london_plot = sns.relplot(data=london_data, x=london_data.index, y="tavg", kind="line", aspect=2)
bozeman_plot = sns.relplot(data=bozeman_data, x=bozeman_data.index, y="tavg", kind="line", aspect=2)

'''
Plot bar charts for monthly averages for each city where the x-axis is the index and the y-axis is the tavg column
The y-axis is set to 0 to 100 to make the plots easier to compare
'''
chicago_monthly_plot = sns.barplot(data=chicago_monthly_data, x=chicago_monthly_data.index, y="tavg")
chicago_monthly_plot.set(ylim=(0, 100))
seattle_monthly_plot = sns.barplot(data=seattle_monthly_data, x=seattle_monthly_data.index, y="tavg")
seattle_monthly_plot.set(ylim=(0, 100))
austin_monthly_plot = sns.barplot(data=austin_monthly_data, x=austin_monthly_data.index, y="tavg")
austin_monthly_plot.set(ylim=(0, 100))
denver_monthly_plot = sns.barplot(data=denver_monthly_data, x=denver_monthly_data.index, y="tavg")
denver_monthly_plot.set(ylim=(0, 100))
las_vegas_monthly_plot = sns.barplot(data=las_vegas_monthly_data, x=las_vegas_monthly_data.index, y="tavg")
las_vegas_monthly_plot.set(ylim=(0, 100))
vancouver_monthly_plot = sns.barplot(data=vancouver_monthly_data, x=vancouver_monthly_data.index, y="tavg")
vancouver_monthly_plot.set(ylim=(0, 100))
london_monthly_plot = sns.barplot(data=london_monthly_data, x=london_monthly_data.index, y="tavg")
london_monthly_plot.set(ylim=(0, 100))
bozeman_monthly_plot = sns.barplot(data=bozeman_monthly_data, x=bozeman_monthly_data.index, y="tavg")
bozeman_monthly_plot.set(ylim=(0, 100))

# Set titles and axis labels for each plot
chicago_plot.set(title="Average Daily Temperature in Chicago", xlabel="Date", ylabel="Temperature (F)")
seattle_plot.set(title="Average Daily Temperature in Seattle", xlabel="Date", ylabel="Temperature (F)")
austin_plot.set(title="Average Daily Temperature in Austin", xlabel="Date", ylabel="Temperature (F)")
denver_plot.set(title="Average Daily Temperature in Denver", xlabel="Date", ylabel="Temperature (F)")
las_vegas_plot.set(title="Average Daily Temperature in Las Vegas", xlabel="Date", ylabel="Temperature (F)")
vancouver_plot.set(title="Average Daily Temperature in Vancouver", xlabel="Date", ylabel="Temperature (F)")
london_plot.set(title="Average Daily Temperature in London", xlabel="Date", ylabel="Temperature (F)")
bozeman_plot.set(title="Average Daily Temperature in Bozeman", xlabel="Date", ylabel="Temperature (F)")

chicago_monthly_plot.set(title="Average Monthly Temperature in Chicago", xlabel="Month", ylabel="Temperature (F)")
seattle_monthly_plot.set(title="Average Monthly Temperature in Seattle", xlabel="Month", ylabel="Temperature (F)")
austin_monthly_plot.set(title="Average Monthly Temperature in Austin", xlabel="Month", ylabel="Temperature (F)")
denver_monthly_plot.set(title="Average Monthly Temperature in Denver", xlabel="Month", ylabel="Temperature (F)")
las_vegas_monthly_plot.set(title="Average Monthly Temperature in Las Vegas", xlabel="Month", ylabel="Temperature (F)")
vancouver_monthly_plot.set(title="Average Monthly Temperature in Vancouver", xlabel="Month", ylabel="Temperature (F)")
london_monthly_plot.set(title="Average Monthly Temperature in London", xlabel="Month", ylabel="Temperature (F)")
bozeman_monthly_plot.set(title="Average Monthly Temperature in Bozeman", xlabel="Month", ylabel="Temperature (F)")

# Map the months to their abbreviated names
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
chicago_monthly_plot.set_xticklabels(month_names)
seattle_monthly_plot.set_xticklabels(month_names)
austin_monthly_plot.set_xticklabels(month_names)
denver_monthly_plot.set_xticklabels(month_names)
las_vegas_monthly_plot.set_xticklabels(month_names)
vancouver_monthly_plot.set_xticklabels(month_names)
london_monthly_plot.set_xticklabels(month_names)
bozeman_monthly_plot.set_xticklabels(month_names)

# Save each plot to the folder 'plots'
chicago_plot.savefig("plots/chicago.png")
seattle_plot.savefig("plots/seattle.png")
austin_plot.savefig("plots/austin.png")
denver_plot.savefig("plots/denver.png")
las_vegas_plot.savefig("plots/las_vegas.png")
vancouver_plot.savefig("plots/vancouver.png")
london_plot.savefig("plots/london.png")
bozeman_plot.savefig("plots/bozeman.png")

chicago_monthly_plot.figure.savefig("plots/chicago_monthly.png")
seattle_monthly_plot.figure.savefig("plots/seattle_monthly.png")
austin_monthly_plot.figure.savefig("plots/austin_monthly.png")
denver_monthly_plot.figure.savefig("plots/denver_monthly.png")
las_vegas_monthly_plot.figure.savefig("plots/las_vegas_monthly.png")
vancouver_monthly_plot.figure.savefig("plots/vancouver_monthly.png")
london_monthly_plot.figure.savefig("plots/london_monthly.png")
bozeman_monthly_plot.figure.savefig("plots/bozeman_monthly.png")
