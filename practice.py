#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:40:46 2020

@author: alanalvarez
"""

import pandas as pd
import math
import matplotlib.pyplot as plt

def start():

    df = read_csv()
    op = '0'
    
    while op != '14':
        print('> Selecciona una opcion (1 - 13):', end='')
        op = input()
            
        if op == '1':
            funcion_1(df)
        elif op == '2':
            funcion_2(df)
        elif op == '3':
            funcion_3(df)
        elif op == '4':
            funcion_4(df)
        elif op == '5':
            funcion_5(df)
        elif op == '6':
            funcion_6(df)
        elif op == '7':
            funcion_7(df)
        elif op == '8':
            funcion_8(df)
        elif op == '9':
            funcion_9(df)
        elif op == '10':
            funcion_10(df)
        elif op == '11':
            funcion_11(df)
        elif op == '12':
            funcion_12(df)
        elif op == '13':
            funcion_13(df)
        elif op == '14':
            return
        else:
            print('\n * Opción Inválida * \n')

def read_csv():
    w_d = '/Users/alanalvarez/Documents/DICIS/2020_1/Materias/DM/code/practica_individual/'
    i_f = 'survey_results_public.csv'
    df = pd.read_csv(w_d + i_f)
    return df

    # Quitar NaN y valores nullos
def remove_nan(df, column):
    df_filter = (df[column].notnull()) & (df[column] != '') 
    return df_filter

def find_vals(df, column):
    filter_nan = remove_nan(df, column)

    data = df[filter_nan][column].str.split(';')
    aux = []
    for element in data:
        for e in element:
            if e not in aux:
                aux.append(e)
    return aux

def correlation(lista1, lista2):
    x = sum(lista1)/len(lista1)
    y = sum(lista2)/len(lista2)
    
    suma1 = 0
    suma2 = 0
    suma3 = 0
    
    for i in range(0, len(lista1)):
        suma1 += (lista1[i]-x)*(lista2[i]-y)
        suma2 += (lista1[i]-x)**2
        suma3 += (lista2[i]-y)**2
        
    #raiz = (suma2*suma3)**(1/2)
    suma2 = math.sqrt(suma2)
    suma3 = math.sqrt(suma3)
    raiz = suma2 * suma3
    correlacion = suma1/raiz
    
    return correlacion

def funcion_1(df):
    print('Five-number summary, boxplot, mean, and standard deviation for the annual salary per gender')
    filter_nan = remove_nan(df, 'ConvertedComp')
    for gen in find_vals(df, 'Gender'):
        filter = (filter_nan) & (df['Gender'].str.contains(gen))
        print('\n\nResumen para '+gen+': ')
        print(df[filter]['ConvertedComp'].describe())
        df[filter].boxplot(column = 'ConvertedComp', sym='')
        plt.show()

def funcion_2(df):
    print('Five-number summary, the boxplot, the mean, and the standard deviation for the annual salary per ethnicity')
    filter_nan = remove_nan(df, 'ConvertedComp')
    for et in find_vals(df, 'Ethnicity'):
        filter = (filter_nan) & (df['Ethnicity'].str.contains(et))
        print('\n\nResumen para '+et+': ')
        print(df[filter]['ConvertedComp'].describe())
        df[filter].boxplot(column = 'ConvertedComp')
        plt.show()

def funcion_3(df):
    print('Five-number summary, the boxplot, the mean, and the standard deviation for the annual salary per developer type.')
    filter_nan = remove_nan(df, 'ConvertedComp')
    for devs in find_vals(df, 'DevType'):
        filter = (filter_nan ) & (df['DevType'].str.contains(devs))
        print('\n\nResumen para '+devs+': ')
        print(df[filter]['ConvertedComp'].describe().apply(lambda x: format(x, 'f')))
        df[filter].boxplot(column = 'ConvertedComp')
        plt.show()

def funcion_4(df):
    print('Median, mean and standard deviation of the annual salary per country')
    filter_nan =  remove_nan(df, 'ConvertedComp')
    for country in find_vals(df, 'Country'):
        filter = (filter_nan) & (df['Country'].str.contains(country))
        print('\n\nResumen para '+country+': ')
        print(df[filter]['ConvertedComp'].describe()[['50%','mean','std']])
        
def funcion_5(df):
    print('Bar plot with the frequencies of responses for each developer type')
    filter_nan = remove_nan(df, 'DevType')
    dev_types = find_vals(df, 'DevType')
    count = []
    for dev in dev_types:
        filter = (filter_nan) & (df['DevType'].str.contains(dev))
        n = df[filter]['DevType'].count()
        count.append(n)
    analisis = pd.DataFrame({'DevType':dev_types, 'n':count})
    analisis.plot.bar(x='DevType', y='n')
    plt.show()

def funcion_6(df):
    print('Plot histograms with 10 bins for the years of experience with coding per gender')
    filter_2 = (remove_nan(df, 'YearsCode')) & ( df['YearsCode'] != 'Less than 1 year' ) & ( df['YearsCode'] != 'More than 50 years' )
    for gen in find_vals(df, 'Gender'):
        print('Género: ' +  gen)
        filter = (filter_2) & (df['Gender'].str.contains(gen))
        df[filter]['YearsCode'].apply(pd.to_numeric).sort_values().hist(bins=10, xrot=90)
        plt.show()

def funcion_7(df):
    print('Plot histograms with 10 bins for the average number of working hours per week, per developer type.')
    filter_nan = remove_nan(df, 'WorkWeekHrs')
    for dev in find_vals(df, 'DevType'):
        print('Tipo de desarrollador: ' +  dev)
        filter = (filter_nan) & (df['DevType'].str.contains(dev))
        filter = (filter) & (df['WorkWeekHrs'] <= 168)
        df[filter]['WorkWeekHrs'].sort_values().hist(bins=10, xrot=90)
        plt.show()
    
def funcion_8(df):
    print('Plot histograms with 10 bins for the age per gender.')
    filter_nan = remove_nan(df, 'Age')
    for gen in find_vals(df, 'Gender'):
        print('Género: '+gen)
        filter = (filter_nan) & (df['Gender'].str.contains(gen))
        df[filter]['Age'].sort_values().hist(bins=10, xrot=90)
        plt.show()

def funcion_9(df):
    print('median, mean and standard deviation of the age per programming language')
    filter_nan = remove_nan(df, 'Age')
    p_lan = find_vals(df, 'LanguageWorkedWith')
    p_lan[p_lan.index('C++')] = 'C+'
    p_lan[p_lan.index('Other(s):')] = 'Other'
    for lan in p_lan:
        filter = (filter_nan) & (df['LanguageWorkedWith'].str.contains(lan))
        print('\n\nResumen para '+lan+': ')
        print(df[filter]['Age'].describe())
    
def funcion_10(df):
    print('Correlation between years of experience and annual salary.')
    filter_nan = (remove_nan(df, 'ConvertedComp')) & (remove_nan(df, 'YearsCode'))
    filter = (filter_nan) & ( df['YearsCode'] != 'Less than 1 year' ) & ( df['YearsCode'] != 'More than 50 years' )
    data = df[filter][['YearsCode','ConvertedComp']]
    data = data.apply(pd.to_numeric)
    print(data.corr())

def funcion_11(df):
    print('Correlation between the age and the annual salary')
    filter = (remove_nan(df, 'ConvertedComp')) & (remove_nan(df, 'Age'))
    data = df[filter][['Age','ConvertedComp']]
    print(data.corr())
    
def funcion_12(df):
    print('Correlation between educational level and annual salary.')
    
    d = {'I never completed any formal education': 1, 'Primary/elementary school': 2, 'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 3,  'Some college/university study without earning a degree': 4, 'Bachelor’s degree (BA, BS, B.Eng., etc.)': 5, 'Professional degree (JD, MD, etc.)': 6, 'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 7, 'Other doctoral degree (Ph.D, Ed.D., etc.)': 8, 'Associate degree':9}
    
    filter = (remove_nan(df, 'EdLevel')) & (remove_nan(df, 'ConvertedComp'))
    ed_level =  df[filter]['EdLevel'].tolist()
    salary = df[filter]['ConvertedComp'].tolist()

    for idx in range(len(ed_level)):
        ed_level[idx] = d[ed_level[idx]]
    
    print(correlation(ed_level, salary))


def funcion_13(df):
    langs = find_vals(df, 'LanguageWorkedWith')
    langs[langs.index('C++')] = 'C+'
    langs[langs.index('Other(s):')] = 'Other'
    
    filter_nan = remove_nan(df, 'LanguageWorkedWith')
    count = []
    for lang in langs:
        filter = (filter_nan) & (df['LanguageWorkedWith'].str.contains(lang))
        n = df[filter]['LanguageWorkedWith'].count()
        count.append(n)

    analisis = pd.DataFrame({'Language':langs, 'n':count})
    analisis.plot.bar(x='Language', y='n')
    plt.show()

start()
































     