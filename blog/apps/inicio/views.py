#encoding:utf-8
from django.shortcuts import render, render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, context
from django.contrib.auth.forms import User
from .forms import *#aki estoy importando todos mis formularios de mi achivo form.py
from .models import *##aki estoy importando todos mis models de mi achivo models.py
# Create your views here.
from django.views.generic import TemplateView, FormView,ListView,CreateView
from django.core.urlresolvers import reverse_lazy
import datetime

import StringIO
from xhtml2pdf import pisa
from django.template.loader import render_to_string
from django.db.models import Q
# Create your views here.
def inicio(request):
	usuarios=User.objects.filter(is_staff=True)
	productos=Producto.objects.filter(estado=True,En_oferta=False).order_by('-id')
	pro_en_ofertas=Producto.objects.filter(estado=True, En_oferta=True).order_by('-id')
	dic={
		'usuarios':usuarios,
		'productos':productos,
		'pro_en_ofertas':pro_en_ofertas
	}
	return render(request,'inicio/inicio.html',dic,context_instance=RequestContext(request))

def loguin(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado/')
	if request.method=='POST':
		print "has escho POST"
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['name']
			print usuario
			clave=request.POST['password']
			print clave
			acceso=authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active and acceso.is_superuser and acceso.is_staff:
					login(request,acceso)
					return HttpResponse('/privado/')
				else:
					if acceso.is_active and acceso.is_staff:
						login(request,acceso)
						return HttpResponse('/privado/')
					else:
						if acceso.is_active:
							login(request,acceso)
							return HttpResponse('/privado/')
			else:
				return HttpResponse("Error, datos incorrectos intente nuevamente Gracias.")
				#return HttpResponse("Tu Cuenta de Usuario no esta activo consulte con el Administrador del Sistema")
		else:
			return HttpResponse("Error, datos incorrectos intente nuevamente Gracias.")
	else:
		formulario=AuthenticationForm()
		forms = UserFormAlumno()
	return render(request,'inicio/loguin.html',{'forms':forms},context_instance=RequestContext(request))
@login_required(login_url='/')
def privado(request):
	now = datetime.datetime.now()
	usuarios=User.objects.filter(is_staff=True)
	if request.user.is_staff and request.user.is_active and request.user.is_superuser:
		return render(request,'administrador/admin.html',{'now':now},context_instance=RequestContext(request))
	else:
		#user.is_staff decimoe q el administrador le dio el permiso para subsustema secretria
		if request.user.is_active and request.user.is_staff:
			return render(request,'administrador/admin.html',{'now':now},context_instance=RequestContext(request))
		else:
			if request.user.is_active:
				return render(request,'inicio/inicio.html',{'now':now,'usuarios':usuarios},context_instance=RequestContext(request))
			else:
				return HttpResponse("Error")

@login_required(login_url='/')
def salir(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/')
def editar_perfil(request):
	if request.method=='POST':
		user_form=UserForms(request.POST,instance=request.user)
		perfil_form=formPerfiles(request.POST,instance=request.user.perfil)
		if user_form.is_valid() and perfil_form.is_valid():
			user_form.save()
			perfil_form.save()
			return HttpResponse("Actualizaste tu perfil correctamente.")
	else:
		user_form=UserForms(instance=request.user)
		perfil_form=formPerfiles(instance=request.user.perfil)
	return render_to_response('inicio/datosPerfil.html',{'user_form':user_form,'perfil_form':perfil_form},context_instance=RequestContext(request))
class nuevoUser(FormView):
	template_name = 'inicio/nuevo.html'
	form_class=UserForm
	success_url = reverse_lazy('listaUsuarios')
	def form_valid(self,form):
		user=form.save()
		perfil=Perfiles()
		perfil.usuario = user
		perfil.materno=form.cleaned_data['materno']
		perfil.ci=form.cleaned_data['ci']
		perfil.telefono=form.cleaned_data['telefono']
		perfil.save()
		return super(nuevoUser, self).form_valid(form)

class nuevoDirector(FormView):
	template_name = 'administrador/nuevoDirector.html'
	form_class=UserFormDirector
	success_url = reverse_lazy('verDitectores')
	def form_valid(self,form):
		user=form.save()
		perfil=Directores()
		perfil.usuario = user
		perfil.materno=form.cleaned_data['materno']
		perfil.ci=form.cleaned_data['ci']
		perfil.telefono=form.cleaned_data['telefono']
		perfil.save()
		return super(nuevoDirector, self).form_valid(form)
######
class nuevoAlumno(FormView):
	template_name = 'administrador/nuevoAlumno.html'
	form_class=UserFormAlumno
	success_url = reverse_lazy('verAlumno')
	def form_valid(self,form):
		user=form.save()
		perfil=Alumnos()
		perfil.usuario = user
		perfil.telefono=form.cleaned_data['telefono']
		perfil.save()
		return super(nuevoAlumno, self).form_valid(form)

from django.core.mail import send_mail
def regisrarseUser(request):
	if request.method == 'POST':
		forms = UserFormAlumno(request.POST)
		if forms.is_valid():
			user = forms.save()
			datos = Alumnos()
			datos.usuario = user
			datos.telefono = int(request.POST['telefono'])
			datos.save()
			user.save()
			acceso=authenticate(username=request.POST['username'],password=request.POST['password2'])
			if acceso.is_active and not acceso.is_staff:
				login(request,acceso)
				asunto = "Bienvenido: %s"%(request.POST['first_name'].capitalize())
				mensaje = "Estamos felises por averte registrado en nuestro sitio Web ahora ya eres uno más de nuestros usuarios online, esperamos tenerte bien informado con todas nuestras actividades no te lo pierdas opten más información ingresando al sitio web: https://shrouded-journey-73490.herokuapp.com/ con tu respetiva cuenta o bien revisando tu correo electrónico deves en cuando. Saludos"
				#mail = EmailMessage(subject='Ejemplo de prueba', body='Este es un ejemplo de prueba de correo', from_email='sistemasuatf12345@gmail.com.com', to=['sistemasuatf12345@gmail.com.com'])
				#mail.send()
				send_mail(asunto, 
				mensaje, 
				'"origen"parabrisas.chelo@gmail.com',
				[request.POST['email']])
				return HttpResponse('/')
		else:
			return HttpResponse('Error, por favor verifique sus datos nuevamente Gracias.')
			#return HttpResponse("Bien venido %s, este al tanto de nuestra novedades...!!!"%(user.first_name))
@login_required(login_url='/')
def verDitectores(request):
	users=User.objects.all().order_by("-id")
	perfil=Directores.objects.all().order_by("-id")
	t_user=Directores.objects.all().count()
	return render_to_response("administrador/DatosDirectores.html",{'users':users,'perfil':perfil,'t_user':t_user},context_instance=RequestContext(request))
def verAlumno(request):
	users=User.objects.all().order_by("-id")
	perfil=Alumnos.objects.all().order_by("-id")
	t_user=Alumnos.objects.all().count()
	return render_to_response("administrador/verAlumno.html",{'users':users,'perfil':perfil,'t_user':t_user},context_instance=RequestContext(request))
def DatosUsuario(request):
	users=User.objects.all().order_by("-id")
	perfil=Perfiles.objects.all().order_by("-id")
	t_user=Perfiles.objects.all().count()
	return render_to_response("inicio/DatosUsuario.html",{'users':users,'perfil':perfil,'t_user':t_user},context_instance=RequestContext(request))
def verificacion(request):
	use=request.GET['use']
	try:
		us=User.objects.get(username=use)
		return HttpResponse("El Nombre de Usuario ya exsiste Intente con otro Nombre.")
	except User.DoesNotExist:
		return HttpResponse()

def docentes(request):
	return render(request, 'inicio/docentes.html')

def generar_pdf(html):
	resultado=StringIO.StringIO()
	pdf=pisa.pisaDocument(StringIO.StringIO(html.encode("UTF:8")),resultado)
	if not pdf.err:
		return HttpResponse(resultado.getvalue(),'application/pdf')
	return HttpResponse("Error al generar el reporte")
def informeReport(request):
	html=render_to_string('inicio/informeReport.html',context_instance=RequestContext(request))
	return generar_pdf(html)
@login_required(login_url='/')
def perfilUser(request):
	user = User.objects.get(id=request.user.id)
	
	dic={
		'user':user

	}
	return render(request,'inicio/perfilUser.html',dic,context_instance=RequestContext(request))
@login_required(login_url='/')
def bienvenida(request):
	user = request.user
	print user
	return HttpResponse("Hola %s,Estamos felises por registrarte en nuestro sitio Web ahora ya eres uno más de nuestros usuarios online, esperamos tenerte bien informado con todas nuestras actividades no te lo pierdas opten más información ingresando al sitio web: https://shrouded-journey-73490.herokuapp.com/ con tu respetiva cuenta y bien revisando tu correo electrónico."%(user))
def personal(request):
	personal = User.objects.filter(is_superuser=True, is_staff=True)
	print personal
	return render(request,'inicio/personal.html',{'personal':personal},context_instance=RequestContext(request))
from django.conf import settings
@login_required(login_url='/')
def mensajes(request):
	if request.method == 'POST':
		asunto = request.POST['asunto']
		mensaje = request.POST['mensaje']
		clientes = User.objects.exclude(is_superuser=True,is_staff=True)
		for i in clientes:
			if len(i.email) > 0:
				print i.email
				send_mail(asunto, 
				mensaje, 
				settings.EMAIL_HOST_USER,
				[i.email])
		return HttpResponse("Tu mensaje de gmail a sido inviado correctamente.")
	return render(request,'inicio/mensajes.html')
def buscar(request):
    if request.method=="POST":
        texto=request.POST["q"]
        busqueda=(
            Q(first_name__icontains=texto) |
            Q(last_name__icontains=texto) |
            Q(username__icontains=texto)
        )
        resultados=User.objects.filter(busqueda, is_superuser=False).distinct()
        print "Clente:",resultados
        return render_to_response('inicio/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

    else:
        texto=request.GET["q"]
        busqueda=(
            Q(first_name__icontains=texto) |
            Q(last_name__icontains=texto) |
            Q(username__icontains=texto)
        )
        resultados=User.objects.filter(busqueda, is_superuser=False).distinct()
        return render_to_response('inicio/buscar.html',{'resultados':resultados},context_instance=RequestContext(request))

def newProducto(request):
	Usuario=Producto(usuario=request.user)
	if request.method=='POST':
		forms=FormsProducto(request.POST,request.FILES,instance=Usuario)
		if forms.is_valid():
			forms.save()
			return HttpResponse("Registro Exitoso.")
	else:
		forms=FormsProducto(instance=Usuario)
	return render_to_response('inicio/newProducto.html',{'forms':forms},context_instance=RequestContext(request))
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def verProducto(request):
	productos=Producto.objects.all().order_by('-id')
	c_total=Producto.objects.count()
	c_act=Producto.objects.filter(estado=True).count()
	c_des=Producto.objects.filter(estado=False).count()

	paginator=Paginator(productos,3)
	page = request.GET.get('page')
	try:
		contenido = paginator.page(page)
	except PageNotAnInteger:
		contenido = paginator.page(1)
	except EmptyPage:
		contenido = paginator.page(paginator.num_pages)

	dic={
		'c_total':c_total,
		'productos':productos,
		'c_act':c_act,
		'c_des':c_des,
		'contenido':contenido
	}
	return render_to_response('inicio/verProducto.html',dic,context_instance=RequestContext(request))

def Detalles(request, id):
	producto=Producto.objects.get(id=int(id))

	return render_to_response('inicio/Detalles.html',{'producto':producto},context_instance=RequestContext(request))

def EdirtarPro(request, id):
	dato=Producto.objects.get(id=int(id))
	print dato
	if request.method=='POST':
		forms=FormsProductoEdit(request.POST, request.FILES ,instance=dato)
		if forms.is_valid():
			forms.save()
			return HttpResponse("El registro se Actualizo correctamente.")
	else:
		forms=FormsProductoEdit(instance=dato)
	return render_to_response('inicio/EdirtarPro.html',{'forms':forms,'cod':int(id)}, context_instance=RequestContext(request))
def ofertas(request, id):
	if request.method=='POST':
		dato=request.POST['oferta']
		if dato=="on":
			Producto.objects.filter(id=int(id)).update(En_oferta=True)
			return HttpResponse('El Producto esta en Oferta')
	else:
		return HttpResponse('Selecciona una opción')
def dar_baja(request, id):
	if request.method=='POST':
		dato=request.POST['baja']
		if dato=="on":
			Producto.objects.filter(id=int(id)).update(estado=False)
			return HttpResponse('El Producto esta en baja')
	else:
		return HttpResponse('Selecciona una opción')
def like(request, id):
	dato=Producto.objects.get(id=int(id))
	dato=int(dato.gusto) + 1
	Producto.objects.filter(id=int(id)).update(gusto=dato)
	return HttpResponse('Gracias por indicar que le gusta el producto, puede pasar por nuestra tienda Av. Prado San Clemente esq. Camargo por la compra del producto le haremos un descuento. <a href="https://www.google.com.bo/maps/place/Tienda+de+Parabrisas+Chelo/@-19.570935,-65.7573429,17z/data=!4m12!1m6!3m5!1s0x93f94e094a849b4b:0x6daa8e36aac601bc!2sTienda+de+Parabrisas+Chelo!8m2!3d-19.570935!4d-65.7551542!3m4!1s0x93f94e094a849b4b:0x6daa8e36aac601bc!8m2!3d-19.570935!4d-65.7551542?hl=es" target="_black">Ver Mapa</a>')