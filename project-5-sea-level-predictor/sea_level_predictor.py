import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df.head())

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='blue', s=10)

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = range(1880, 2051)
    y = slope*x + intercept
    plt.plot(x, y, 'r', label='fit: 1880-2050')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x = range(2000, 2051)
    y = slope*x + intercept
    plt.plot(x, y, 'g', label='fit: 2000-2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()