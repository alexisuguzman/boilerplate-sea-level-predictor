import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Fill in years up to 2050
    start_year = df['Year'].max()
    end_year = 2050

    new_rows = []
    for year in range(start_year, end_year + 1):
        if year not in df['Year'].values:
            new_rows.append({'Year': year, 'CSIRO Adjusted Sea Level': 0})
            print("added year")

    new_rows_df = pd.DataFrame(new_rows)

    df = pd.concat([df, new_rows_df], ignore_index=True)
    df = df.sort_values(by='Year')



    plt.plot(df['Year'], ([line.slope]*df['Year'] + line.intercept), color='orange' )
    
    
    # Create second line of best fit
    # Mask from 2000 to last year before predicting (2013)
    df_from_2000_to_start_year = df[(df['Year'] >= 2000) & (df['Year'] <= start_year)]
    second_line = linregress(df_from_2000_to_start_year['Year'], df_from_2000_to_start_year['CSIRO Adjusted Sea Level'])
    df_from_2000_to_2050 = df[(df['Year'] >= 2000) & (df['Year'] <= 2050)]


    plt.plot(df_from_2000_to_2050['Year'], ([second_line.slope]*df_from_2000_to_2050['Year'] + second_line.intercept), color='red')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
