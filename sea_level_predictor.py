import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    # Year = X axis
    # CSIRO Adjusted Sea Level = Y axis
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    # linregress CRIA UMA LIHA
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Linha dever ir até o ANO 2050
    years_extended = pd.Series(range(df['Year'].min(), 2051))
    # Cria o gráfico com a serie de dados, coeficientes e linha de regressão
    # y = ab + c
    plt.plot(years_extended, result.intercept + result.slope * years_extended, 'r', label='Best Fit Line 1')


    # Create second line of best fit
    # ANO 2000 até ANO MAIS RECENTE
    # Guarda ano mais recente
    recent_df = df[df['Year'] >= 2000]
    # linregress CRIA UMA LIHA
    result = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    # Linha dever ir do ANO 2000 até o ANO 2050
    years_recent_extended = pd.Series(range(2000, 2051))
    # Cria o gráfico com a serie de dados, coeficientes e linha de regressão
    # y = ab + c
    plt.plot(years_recent_extended, result.intercept + result.slope * years_recent_extended, 'g', label='Best Fit Line 2')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    #plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    # gca = get current axis
    # gca outro nome para gráfico
    # retorna o gráfico
    return plt.gca()