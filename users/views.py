from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import UserRegisterForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/sign_up.html'
    success_url = reverse_lazy('sign_up')
