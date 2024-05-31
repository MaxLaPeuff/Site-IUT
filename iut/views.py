from django.shortcuts import render,redirect
from .models import CreateBlog, Memoire,Personnel,Contact
from .forms import BlogForm
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.
def home(request):
    # Récupérer les trois derniers articles de blog
    recent_posts = CreateBlog.objects.order_by('-date_created')[:3]

    # Transmettre les articles de blog au modèle de template
    context = {'recent_posts': recent_posts}
    return render(request, 'iut/index.html', context)



def about (request):
    return render(request, 'iut/about.html')

def administration(request):
    personnels = Personnel.objects.all()
    return render(request, 'iut/administration.html', {'personnels': personnels})


class List(ListView):
    template_name = 'iut/blog.html'
    queryset = CreateBlog.objects.all()
    paginate_by = 2

def detailView(request,slug):
    post=CreateBlog.objects.get(slug=slug)
    comments=post.comments.all()
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post=post
            form.save()
            return redirect('detailView',slug=post.slug)
    else:
        form=BlogForm
    content={
        'article':post,
        'comments':comments,
        'form':form,
    }
    return render(request,'iut/update.html',content)



def memoire_list(request):
    query = request.GET.get('q')
    if query:
        memoires = Memoire.objects.filter(
            Q(student_name__icontains=query) |
            Q(filiere__icontains=query) |
            Q(theme__icontains=query)
        )
    else:
        memoires = Memoire.objects.all()
    return render(request, 'iut/memoire_list.html', {'memoires': memoires})

def personnel(request):
    personnels = Personnel.objects.all()
    return render(request, 'iut/administration.html', {'personnels': personnels})

def contacter(request):
    contact=Contact.objects.all()
    
    if request.method=='POST' :
        nom=request.POST.get('nom')
        prenom=request.POST.get('prenom')
        email=request.POST.get('email')
        tel=request.POST.get('tel')
        objet=request.POST.get('objet')
        message=request.POST.get('message')
        
        newContact= Contact.objects.create(nom=nom,prenom=prenom,email=email,tel=tel,objet=objet,message=message)
        newContact.save()
        
    return render(request,'iut/index.html')