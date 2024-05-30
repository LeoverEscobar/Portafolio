from django.shortcuts import render
from .models import Contacto

# Librerias para  enviar correo
from django.core.mail import EmailMessage 
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def contacto(request):
    if request.method == "POST":
        tname = request.POST["name"]
        temail = request.POST["email"]
        tphone = request.POST["phone"]
        tmessage = request.POST["message"]
        obj_contact = Contacto(name=tname,email=temail,phone=tphone,message=tmessage)
        obj_contact.save()
        #return HttpResponse("El registro fue ingresado")
        #return render(request,"pages/gracias.html",)
    

        # Inicio de codigo para enviar correo
        template_contact = render_to_string('pages/contacts_proof.html',{
        'name': tname,
        'email': temail,
        'phone': tphone,
        'message': tmessage
        })

        email = EmailMessage(
        tname,
        template_contact,
        settings.EMAIL_HOST_USER,
        ['laeg2002@gmail.com']
        )

        email.fail_silently = False
        email.send()
        # messages.success(request, 'Se envio el Correo')
        # ? duda para el profe si cambio el render por redirect me aparece un error
        return render(request, '../templates/pages/inicio.html')
    return render(request, 'pages/contacto.html')
