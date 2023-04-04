from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
from io import BytesIO
import pandas as pd
import seaborn as sns


# Create your views here.
def home(request):
    return render(request,'homepage.html')

def choose(request):
    return render(request,'index.html')


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
import io
import urllib, base64

def plot2(request):
    # barplot
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





import pandas as pd
import matplotlib.pyplot as plt
from django.shortcuts import render
from django.http import HttpResponse
import io
import urllib, base64



from django.http import HttpResponse

def plot3(request):
    # pie plot
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
    plt.pie(totals, labels=labels, colors=colors, autopct='%.0f%%', startangle=90, shadow=True)
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

def plot4(request):
    # violin plot
    plt.close()
    filename = 'worldometer_data.csv'
    data = pd.read_csv(filename)

    sns.violinplot(data=data, x="Continent", y="Covid_stage ",inner=None)
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.4,left=0.2)
    plt.rcParams['figure.autolayout'] = True
    # Save the plot to a BytesIO buffer
    from io import BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Convert the buffer to a base64-encoded string and pass it to the template
    import base64
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    context = {'image': image_base64}

    return render(request, 'plot4.html', context)
    