# Michael Underwood, Michael Hutchings, Preston Fitzgerald, Elliot Pi, Lily Pettit, Noelle Burton

# import
from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
from django.shortcuts import render
from django.http import HttpResponse
from .models import missingPersons
# Create your views here.

# this is the landing page
def indexPageView(request) :
   mp = missingPersons.objects.all()

   context = {
        "mp" : mp
    }
   


   # industry standard
  
   return render(request,'basefolder/index.html',context)

# this is the about page
def aboutPageView(request) :
   chart = create_pie_chart
   
   context = {
   'chart' : chart
   }

   return render(request, 'basefolder/about.html', context)

def showPageView(request, id):

   student=missingPersons.objects.get(id=id)

   context = {
      "data" : student
   }

   return render(request,'basefolder/showMissing.html', context)



# Create your views here.


 




#This function creates a pie chart for the stats (used in the aboutPageView)
def create_pie_chart():
   labels = ['Tip', 'Training & ' + '\n' + 'Technical ' +'\n' + 'Assistance',  'High Risk',
             'General Info', 'Crisis', 'Referral']
   values = [29, 1, 28, 12, 19, 11]
   fig, ax =plt.subplots(figsize=(6, 6))
   wedges, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.0f%%', textprops={'fontsize': 12, 'color': 'white'})
   ax.axis('equal')

   for text in texts:
      text.set_color('black')

   figfile = io.BytesIO()
   plt.savefig(figfile, format='png')
   figfile.seek(0)
   figdata_png = base64.b64encode(figfile.getvalue()).decode('utf8')
   
   return  figdata_png