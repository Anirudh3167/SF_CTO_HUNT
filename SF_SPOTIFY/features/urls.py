from django.urls import path
from .views import *

app_name = "Features"

urlpatterns = [
    path('',Home,name="Home"),
    path('about/',About,name="About"),
    path('under-development/',UnderDevelopment,name="UnderDevelopment"),
    path('feature-<str:id>',Feature,name="Feature"),
    path('feature-<str:id>/about',FeatureAbout,name="FeatureAbout"),
    path('feature-<str:id>/analysis',FeatureAnalysis,name="FeatureAnalysis"),
]