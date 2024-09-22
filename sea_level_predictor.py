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
    # antes de linegress são definidos seus COEFICIENTES
    # slope = inclinação
    # intercept = onde intercepta
    # r_value = coeficiente de correlação
    # p_value = p-value
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Linha dever ir até o ANO 2050
    years_extended = pd.Series([i for i in range(df['Year'].min(), 2051)])
    # Cria o gráfico com a serie de dados, coeficientes e linha de regressão
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best Fit Line 1')

    # Create second line of best fit
    # ANO 2000 até ANO MAIS RECENTE
    # Guarda ano mais recente
    recent_df = df[df['Year'] >= 2000]
    # linregress CRIA UMA LIHA
    # antes de linegress são definidos seus COEFICIENTES
    # slope = inclinação
    # intercept = onde intercepta
    # r_value = coeficiente de correlação
    # p_value = p-value
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    # Linha dever ir do ANO 2000 até o ANO 2050
    years_recent_extended = pd.Series([i for i in range(2000, 2051)])
    # Cria o gráfico com a serie de dados, coeficientes e linha de regressão
    plt.plot(years_recent_extended, intercept_recent + slope_recent * years_recent_extended, 'g', label='Best Fit Line 2')

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