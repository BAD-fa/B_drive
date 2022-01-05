from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout as lo
from django.views.generic import FormView

from .models import User, File
from .forms import SignIn, UploadForm


def home(request):
    return render(request, "home.html")


class Login(View):
    form = SignIn()
    ctx = {'form': form}

    def get(self, request):
        return render(request, 'drive/login.html', context=self.ctx)

    def post(self, request):
        form = SignIn(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect(reverse('drive:home'))
            else:
                self.ctx['message'] = "user doesn't exist"
                return render(request, 'drive/login.html', context=self.ctx)


@method_decorator(login_required, name='dispatch')
class Upload(FormView):
    template_name = 'drive/upload.html'
    form_class = UploadForm
    success_url = reverse('drive:show_files')

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('files')
        user = User.objects.get(email=request.user.email)
        if form.is_valid():
            size = 0
            for f in files:
                size += f.size
                name = form.cleaned_data.get('name', '')
                if name:
                    File.objects.create(name=name, file=f, user=user)

                else:
                    File.objects.create(name=f.name, file=f, user=user)
            user.uploaded_size += size
            user.save()
            return self.form_valid(form)

        else:
            return self.form_invalid(form)


@login_required
def show_files(request):
    if request.method == "GET":
        user = User.objects.get(email=request.user.email)
        user_files = user.files.all().values('name', 'file', 'date')
        ctx = {'files': user_files}
        return render(request, 'drive/files.html', context=ctx)


@login_required
def logout(request):
    lo(request)
    return redirect(reverse('drive:home'))
