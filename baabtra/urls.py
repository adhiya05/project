from django.urls import path
from . import views


urlpatterns=[
    path('home',views.baabtrahome,name='home'),
    path('page2',views.page2,name='page'),
    path('aboutus',views.aboutus,name='about'),
    path('placement',views.placement,name='placement'),
    path('css1',views.css,name='css'),
    path('css2',views.css2,name='css2'),
    path('grid',views.grid,name='grid'),
    path('grid2',views.grid2,name='grid2'),
    path('grid3',views.grid3,name='grid3'),
     path('bootstrap',views.bootstrap,name='bootstrap'),
     path('baabtra2',views.baabtra2,name='baabtra2'),
    
    
    
]