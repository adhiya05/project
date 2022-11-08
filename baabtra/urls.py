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
     path('js',views.js,name='js'),
     path('doc',views.doc,name='doc'),
    path('doc2',views.doc2,name='doc2'),
    path('array',views.array,name='array'),
    path('task',views.task,name='task'),
    path('jquery',views.jquery,name='jquery'),
     path('queryadd',views.queryadd,name='queryadd'),
     path('jquery2',views.jquery2,name='jquery2'),
    path('traverse',views.traverse,name='traverse'),
    path('signup',views.signup,name='signup'),
    path('test_css',views.test_css,name='test_css'),
    path('life',views.life,name='life'),
    path('pictures',views.pictures,name='pictures'),

  

   
   

    
    
    
]