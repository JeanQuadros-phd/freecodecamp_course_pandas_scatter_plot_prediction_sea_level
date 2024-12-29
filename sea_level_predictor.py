import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data', alpha=0.6)

    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)  # Extending to 2050
    y1 = [slope1 * year + intercept1 for year in x1]
    plt.plot(x1, y1, color='red', label='Best Fit: All Data')

    # Create second line of best fit (from year 2000 onwards)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    y2 = [slope2 * year + intercept2 for year in x2]
    plt.plot(x2, y2, color='green', label='Best Fit: From 2000')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
