from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView

class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name ="login.html"
    
    def get_success_url(self):
        return reverse_lazy('new_collection') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    


class SignUpView(CreateView):
  template_name = 'signup.html'
  success_url = reverse_lazy('login')
  form_class = UserRegisterForm

