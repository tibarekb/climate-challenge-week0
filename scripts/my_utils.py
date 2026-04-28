import matplotlib.pyplot as plt
import pandas as pd


def plot_temperature(df, date_col, temp_col,
					 title:str,
					 ylabel:str,
					 figsize=(24, 8),
					 annotate=True, ax=None):
	"""Plot temperature time series from a dataframe.

	Parameters
	- df: pandas.DataFrame containing the data
	- date_col: name of the date column (will be converted to datetime if needed)
	- temp_col: name of the temperature column
	- title: plot title
	- ylabel: y-axis label
	- figsize: tuple for figure size
	- rotate_xticks: degrees to rotate x ticks
	- annotate: whether to mark min/max points
	- ax: optional Matplotlib Axes to plot on

	Returns
	- ax: Matplotlib Axes with the plot
	"""
	if ax is None:
		fig, ax = plt.subplots(figsize=figsize)
	else:
		fig = ax.figure

	# Work on a copy if we need to convert date types
	df_plot = df.copy()
	if not pd.api.types.is_datetime64_any_dtype(df_plot[date_col]):
		df_plot[date_col] = pd.to_datetime(df_plot[date_col])

	ax.plot(df_plot[date_col], df_plot[temp_col])
	ax.set_ylabel(ylabel)
	ax.set_xlabel('Date')
	ax.set_title(title)
	plt.setp(ax.get_xticklabels(), rotation=45)

	if annotate and not df_plot.empty:
		highest_idx = df_plot[temp_col].idxmax()
		lowest_idx = df_plot[temp_col].idxmin()
		ax.scatter(df_plot.loc[highest_idx, date_col], df_plot.loc[highest_idx, temp_col],
				   color='red', marker='o', s=100, label='Max Temp')
		ax.scatter(df_plot.loc[lowest_idx, date_col], df_plot.loc[lowest_idx, temp_col],
				   color='blue', marker='o', s=100, label='Min Temp')
		ax.legend()

	return ax
