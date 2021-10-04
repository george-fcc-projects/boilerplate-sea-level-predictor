import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df)


    # Create scatter plot
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    # Create first line of best fit
    line1 = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.ylim(bottom=0, top=20)
    plt.xlim(right=2065)
    plt.plot(range(1880, 2051), line1.intercept + line1.slope * range(1880, 2051), 'r', label='fitted line')

    # Create second line of best fit
    df_line2 = df.loc[df['Year'] >= 2000]
    print(df_line2)
    line2 = linregress(x=df_line2['Year'], y=df_line2['CSIRO Adjusted Sea Level'])
    print(line2)
    plt.plot(range(2000, 2051), line2.intercept + line2.slope * range(2000, 2051), 'r', label='fitted line')

    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()