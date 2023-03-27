from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import os
import pandas as pd
import seaborn as sns


# Create your views here.
def home(request):
    return render(request,'homepage.html')

def choose(request):
    return render(request,'index.html')

def plot(request):
    # load dataset
    directory = os.path.dirname(os.path.abspath(__file__))
    filename = 'data/titanic.csv'
    file_path = os.path.join(directory, filename)
    data=pd.read_csv(file_path)

    # create plot
    fig, ax = plt.subplots()
    sns.barplot(x='who', y='fare', hue='class', data=data, palette='Blues', ax=ax)

    # save plot to a bytes buffer
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)

    # create HTTP response with image data
    response = HttpResponse(buffer, content_type='image/png')

    return response

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
import io
import urllib, base64

def plot2(request):
    plt.close()
    # Read the data from CSV file
    covid_data = pd.read_csv("country_wise_latest.csv")
    
    # Generate the plot using seaborn
    chart1 = sns.barplot(x='WHO Region', y='Confirmed', errorbar=None, data=covid_data)
    plt.title('Confirmed cases by WHO Region')
    plt.xlabel('WHO Region')
    plt.ylabel('Confirmed cases')
    plt.xticks(rotation=25)
    plt.subplots_adjust(bottom=0.4,left=0.2) # Adjust the position of x-axis labels

    # Convert the plot to PNG image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the PNG image to base64 string
    image_base64 = base64.b64encode(image_png)
    image_base64 = image_base64.decode('utf-8')
    
    # Pass the base64 string to the context
    context = {'image_base64_1': image_base64}
    
    # Render the template with context
    return render(request, 'plot2.html', context=context)



# import matplotlib.pyplot as plt
# plt.rcParams["figure.figsize"] = [8, 6] # Set the figure size
# import io
# import seaborn as sns
# from django.http import HttpResponse
# import pandas as pd

# def plot2(request):
#     # Read the data from CSV file
#     covid_data = pd.read_csv("country_wise_latest.csv")
    
#     # Generate the plot using seaborn
#     chart1 = sns.barplot(x='WHO Region', y='Confirmed', data=covid_data)
#     plt.title('Confirmed cases by WHO Region')
#     plt.xlabel('WHO Region')
#     plt.ylabel('Confirmed cases')
#     plt.subplots_adjust(bottom=0.4) # Adjust the position of x-axis labels
    
#     # Convert the plot to PNG image
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()

#     # Return the PNG image as HTTP response
#     return HttpResponse(image_png, content_type='image/png')



import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
import io
import urllib, base64

# def plot3(request):
#     # Read the data from CSV file
#     covid_data = pd.read_csv("country_wise_latest.csv")
    
#     # Calculate the total numbers for each category
#     total_confirmed = covid_data['Confirmed'].sum()
#     total_active = covid_data['Active'].sum()
#     total_recovered = covid_data['Recovered'].sum()
#     total_deaths = covid_data['Deaths'].sum()

#     # Create a list of total numbers and labels for the chart
#     totals = [total_active, total_recovered, total_deaths]
#     labels = ['Active', 'Recovered', 'Deaths']
#     colors = ['#3274A1', '#3A923A', '#C03D3E']
    
#     # Generate the pie chart using matplotlib
#     plt.pie(totals, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90, shadow=True)
#     plt.title('COVID-19 Total Cases')
    
#     # Convert the plot to PNG image
#     buffer = io.BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     buffer.close()

#     # Encode the PNG image to base64 string
#     image_base64 = base64.b64encode(image_png)
#     image_base64 = image_base64.decode('utf-8')
    
#     # Pass the base64 string to the context
#     context = {'image_base64_2': image_base64}
    
#     # Render the template with context
#     return render(request, 'plot3.html', context=context)


from django.http import HttpResponse

def plot3(request):
    plt.close()
    # Read the data from CSV file
    covid_data = pd.read_csv("country_wise_latest.csv")
    
    # Calculate the total numbers for each category
    # total_confirmed = covid_data['Confirmed'].sum()
    total_active = covid_data['Active'].sum()
    total_recovered = covid_data['Recovered'].sum()
    total_deaths = covid_data['Deaths'].sum()

    # Create a list of total numbers and labels for the chart
    totals = [total_active, total_recovered, total_deaths]
    labels = ['Active', 'Recovered', 'Deaths']
    colors = ['#3274A1', '#3A923A', '#C03D3E']
    
    # Generate the pie chart using matplotlib
    plt.pie(totals, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90, shadow=True)
    plt.title('COVID-19 Total Cases')
    
    # Convert the plot to PNG image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode the PNG image to base64 string
    image_base64 = base64.b64encode(image_png)
    image_base64 = image_base64.decode('utf-8')
    
    # Pass the base64 string to the context
    context = {'image_base64': image_base64}
    
    # Render the template with context
    return render(request, 'plot3.html', context=context)



