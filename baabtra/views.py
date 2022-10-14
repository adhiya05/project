from django.shortcuts import render

# Create your views here.

def baabtrahome(request):
    return render(request,'baabtra/baabtrahome.html')

def page2(request):
    return render(request,'baabtra/page2.html')

def aboutus(request):
    return render(request,'baabtra/aboutus.html')
    
def placement(request):
    return render(request,'baabtra/placement.html')

def css(request):
    return render(request,'baabtra/css.html')

def css2(request):
    return render(request,'baabtra/css2.html') 

def grid(request):
    return render(request,'baabtra/grid.html')

def grid2(request):
    return render(request,'baabtra/grid2.html')

def grid3(request):
    return render(request,'baabtra/grid3.html')

def bootstrap(request):
    return render(request,'baabtra/bootstrap.html') 

def baabtra2(request):
    return render(request,'baabtra/baabtra2.html') 
            
            
            
        
    