from django.shortcuts import redirect, render
from django.views import View
from .models import Affairs
from .forms import AddForm
# Create your views here.


def index(request):
    return render(request, "index.html")

class AddView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = AddForm(request.GET)
            return render(request, 'add.html', {'form': form})
        else:
            return render(request, 'add.html')
    def post(self, request):
        form = AddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            user = request.user
            affair = Affairs(name=name, description=description, username=user)
            affair.save()
            return redirect('affairs')
        
def get_affairs(request):
    if request.user.is_authenticated:
        data = Affairs.objects.filter(username=request.user)
        return render(request, "affairs.html", {"data": data})
    else:
        return render(request, "affairs.html")

def delete(request, id):
    affair = Affairs.objects.get(id=id)
    affair.delete()
    return redirect("affairs")