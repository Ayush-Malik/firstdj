from django.shortcuts import render
from django.http import HttpResponse

from new_app.models import Contact

# Create your views here.

def home_page(request):
    
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            dropdown = request.POST.get('dropdown')
            desc = request.POST.get('desc')
        
            contact = Contact(name = name , email = email , phone = phone , dropdown = dropdown , desc = desc )
            contact.save()

            context = { 'var_1' : "It's a joke man !!! " , 'var_2' : 'I know you are a idiot !!!' }

            
            return render(request , 'end_response.html' , context  )
        


        context = { 'variable' : '21 diin me paisa double' , 'var_1' :'Let me double your money!!!' , 'var_2' : 'Guarantee to dekho hm dete nhi , to aukat k hisaab se paisa lgana' }
        return render(request , 'home_page.html' , context)
        # return HttpResponse("Ye apun ka home page hai!!")