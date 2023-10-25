from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from tcp_gaming import settings
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from .token import generatorToken

# Create your views here.
def index(request):
    return render(request, "login/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur existe déjà")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Cet email existe déjà")
        elif not username.isalnum():
            messages.error(request, "Le nom d'utilisateur doit être alphanumérique")
        elif password != password1:
            messages.error(request, "Les mots de passe ne correspondent pas")
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.username = username
            my_user.is_active = False
            my_user.save()
            messages.success(request, "Votre compte a été créé avec succès")
            login(request, my_user)

            # Envoi d'un mail de bienvenue
            subject = "Bienvenue sur TCP Gaming"
            welcome_messages = "Bonjour " + my_user.username + ",\n\nNous vous souhaitons la bienvenue sur TCP Gaming !\n\nCordialement,\nL'équipe TCP Gaming"
            from_email = settings.EMAIL_HOST_USER
            to_list = [my_user.email]
            send_mail(subject, welcome_messages, from_email, to_list, fail_silently=False)

            # Envoi d'un mail de confirmation
            current_site = get_current_site(request)
            email_subject = "Activez votre compte"
            messageConfirm = render_to_string("emailconfirm.html", {
                'user': my_user.username,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
                'token': generatorToken.make_token(my_user),
            })

            email_message = EmailMessage(
                email_subject,
                messageConfirm,
                settings.EMAIL_HOST_USER,
                [my_user.email],
            )

            email_message.fail_silently = False
            email_message.send()
            return redirect("login-index")
        
    return render(request, "login/register.html")


def connect(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "login/index.html", {'username': user.username})
            else:
                messages.error(request, "Votre compte n'est pas encore activé. Vérifiez votre e-mail pour le lien de confirmation.")
                return redirect("login-index")
        else:
            messages.error(request, "Identifiants incorrects")
            return redirect("login-index")

    return render(request, "login/connect.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès")
    return redirect("login-index")


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode('utf-8')
        my_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generatorToken.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        login(request, my_user)
        messages.success(request, "Votre compte a été activé avec succès")
        return redirect("login-index")
    else:
        messages.error(request, "Le lien d'activation est invalide")
        return redirect("login-index")