from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse
from .models import encuestaSatisfaccion
from django.db.models import Count
# Create your views here.

class Contact(APIView):
    template_name = 'contact.html'
    
def get(self, request):
        
        industrias = encuestaSatisfaccion.objects.values('preguntal').annotate(total=Count('preguntal')).order_by('preguntal') 
        etiquetasPregunta1 = [industria['preguntal'] for industria in industrias]
        valoresPreguntal = [industria['total'] for industria in industrias]

#grafico circular para la pregunta 2

        tamanos_empresas = encuestaSatisfaccion.objects.values('pregunta2').annotate(total=Count('pregunta2'))
        etiquetasPregunta2 = [tamano['pregunta2'] for tamano in tamanos_empresas]
        valoresPregunta2 = [tamano['total'] for tamano in tamanos_empresas]

#grafico de anillo para la pregunta 4

        frecuencias = encuestaSatisfaccion.objects.values ('pregunta3').annotate(total=Count('pregunta3'))
        etiquetasPregunta3 = [frecuencia['pregunta3'] for frecuencia in frecuencias]
        valoresPregunta3 = [frecuencia['total'] for frecuencia in frecuencias ]

        return render(request, self.template_name,{'etiquetasPregunta1': etiquetasPregunta1,
                                           'valoresPregunta1': valoresPreguntal,
                                           'etiquetasPregunta2': etiquetasPregunta2,                                          
                                           'valoresPregunta2': valoresPregunta2,
                                           'etiquetasPregunta3': etiquetasPregunta3,
                                           'valoresPregunta3': valoresPregunta3})
def post(self,request):
        return render(request, self.template_name)
    
class Home(APIView):
    template_name = "index.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

class About(APIView):
    template_name = "about-us.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

class Blog(APIView):
    template_name = "blog.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

class Contact(APIView):
    template_name = "contact.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

class Elements(APIView):
    template_name = "elements.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

class Portfolio(APIView):
    template_name = "portfolio.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

class Services(APIView):
    template_name = "services.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

class Single(APIView):
    template_name = "single-blog.html"
    def post(self, request):
        return render(request,self.template_name)
    def get(self, request):
        return render(request,self.template_name)

def signup(request):
    if request.method =='GET':
        return render(request, 'signup.html',{
            'form' : UserCreationForm
        })
    else:
            try:
                user = User.objects.create_user(first_name=request.POST['first_name'], email=request.POST['email'], last_name=request.POST['last_name'], username=request.POST['username'], password=request.POST['password'])
                user.save()
                correo = request.POST['email']
                usuario = request.POST['username']
                contra = request.POST['password']
                return redirect('enviar_correo', correo=correo, usuario=usuario, contra=contra)
                                
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form' : UserCreationForm,
                    "mensaje" : 'Username already exist'
                })
                #return HttpResponse('Username already exist')
        #return HttpResponse('Password do not match')
def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('/')

def enviar_correo(request, correo, usuario, contra):
    subject = 'Bienvenida'
    from_email = 'axel.zarcort@gmail.com'
    recipient_list = [correo]

    # Renderiza la plantilla HTML con el contexto
    contexto = {'usuario': usuario,
                "contra": contra}
    contenido_correo = render_to_string('correo.html', contexto)

    # Envía el correo
    send_mail(subject, '', from_email, recipient_list, html_message=contenido_correo)
    
    return redirect('signin')


def grafica(request):
    registros = encuestaSatisfaccion.objects.all()
    return {'registros': registros}

def consulta1(request):
    # Realiza una consulta que cuente las filas con 'SI' en la columna pregunta1
    count = encuestaSatisfaccion.objects.filter(pregunta1="Si").count()
    return {'count_si': count}

def consulta2(request):
    # Realiza una consulta que cuente las filas con 'NO' en la columna pregunta1
    count2 = encuestaSatisfaccion.objects.filter(pregunta1="No").count()
    return {'count_no': count2}

def HomePage(request):
    grafica_data = grafica(request)
    tuvista_data = consulta1(request)
    tuvista_data2 = consulta2(request)
    
    # Combina los contextos de ambas vistas en un solo diccionario
    context = {**grafica_data, **tuvista_data, **tuvista_data2}
    return render(request, 'menu.html', context)

def Enc(request):
    
    grafica_data = grafica(request)
    tuvista_data = consulta1(request)
    tuvista_data2 = consulta2(request)
    
    # Combina los contextos de ambas vistas en un solo diccionario
    context = {**grafica_data, **tuvista_data, **tuvista_data2}
    return render (request, 'encuesta.html',context)