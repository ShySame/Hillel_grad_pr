from authorization.forms import RegisterForm

from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

User = get_user_model()


class RegisterFormView(generic.CreateView):
    template_name = 'registration/registr.html'
    form_class = RegisterForm

    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterFormView, self).form_valid(form)


class UserEditView(LoginRequiredMixin, generic.UpdateView):
    model = User
    fields = ["username", "first_name", "last_name", "email"]
    template_name = 'registration/user_edit.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        user = self.request.user
        return user


class UserView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = 'registration/user.html'
