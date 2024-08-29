import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv")
# Set index to date column and parse dates
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data
lower_part = df["value"].quantile(0.025)  # flop 2,5%
upper_part = df["value"].quantile(0.975)  # top 2,5%
# filtering top and flop
df = df[(df["value"] >= lower_part) & (df["value"] <= upper_part)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df["value"], color="blue", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    # Save image and return fig (don't change this part)
    fig.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None

    # Draw bar plot

    # Save image and return fig (don't change this part)
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
