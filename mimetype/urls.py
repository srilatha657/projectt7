from django.urls import path
from .views import HtmlView,XmlView,ExcelView
urlpatterns=[
     path('html/',HtmlView.as_view()),
     path('xml/',XmlView.as_view()),
     path('excel/',ExcelView.as_view()),
]




