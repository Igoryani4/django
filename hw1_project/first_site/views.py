# import logging
# from django.http import HttpResponse


# logger = logging.getLogger(__name__)
  

# def index(request):
#     logger.info('home page access')
#     return HttpResponse("Главная")
 

# def about(request):
#     logger.info('about page access')
#     return HttpResponse("О сайте")


# def contact(request):
#     logger.info('contacts page access')
#     return HttpResponse("Контакты")

import logging
from django.http import HttpResponse
from django.shortcuts import render


logger = logging.getLogger(__name__)

  
def index(request):
    logger.info('home page access')
    return render(request, 'index.html')
    # return HttpResponse("<h2>Главная</h2>")
 
def about_us(request):
    logger.info('about page access')
    return render(request, 'about.html')
    # return HttpResponse("<h2>О сайте</h2>")
 
def contact(request):
    logger.info('about page access')
    return render(request, 'contacts.html')
    # return HttpResponse("<h2>Контакты</h2>")