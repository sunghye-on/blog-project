from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import Blogpost
# Create your views here.
def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list,3)
    page1 = request.GET.get('page')
    posts = paginator.get_page(page1)
    return render(request, 'home.html',{'blog':blogs, 'posts':posts})
     
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog , pk = blog_id)
    
    
    return render(request,'detail.html',{'det':blog_detail})


def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']     
    blog.date = timezone.datetime.now()
    blog.save() 
    return redirect('/blog/'+str(blog.id))

def getpage(request):
    num = request.GET['pagenum']
    # if(num<1 or num > posts.paginator.num_pages):
       # return redirect('home')
    # else:
    return redirect('/?page='+num)
        
def blogpost(request):
    if request.method == "POST":
        forms = Blogpost(request.POST)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.date = timezone.now()
            post.save()
            return redirect('home')
    else:
        forms = Blogpost()
        return render(request,'new.html',{'form':forms})
        
