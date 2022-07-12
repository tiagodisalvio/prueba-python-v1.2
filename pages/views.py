from urllib import request
from django.shortcuts import render

#para importar formulario
from pages.forms import NewPost
from pages.models import Post

#para poder ver el detalle de las vistas
from django.views.generic.detail import DetailView
# para editar una vista
from django.views.generic.edit import UpdateView
#para eliminar vista
from django.views.generic.edit import DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

#Vista del inicio
def pages(request):
    posts = Post.objects.all()#aca traigo todos los posts
    
    context = {"posts":posts}
    
    return render(request, 'pages/inicioPages.html',context)

#vista para crear fomulario
@login_required
def newPost(request):
    if request.method =='POST':
    
        myForm = NewPost(request.POST, files=request.FILES)
    
        if myForm.is_valid():
            
            info = myForm.cleaned_data
            
            newPost = Post (img=info['img'], place=info['place'], name=info['name'], title=info['title'], description=info['description'])
            newPost.save()
            
            posts = Post.objects.all()#aca traigo todos los posts
    
            context = {"posts":posts}
    
            return render(request, 'pages/inicioPages.html',context)
        
    else:
        myForm = NewPost()
        
    return render(request, "pages/newPost.html",{"myForm":myForm})

#para ver el detalle de cada post

class PostDetail(DetailView):
    
    model = Post
    template_name = "pages/postDetail.html"
    

#para eliminar una vista
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/pages/'
    template_name='pages/post_confirm_delete.html'
    
#para editar un post


@login_required
def postUpdate(request, post_id):#para editar el post
    post=Post.objects.get(id=post_id)
    if request.method == 'POST':
        
        myForm = NewPost(request.POST, files=request.FILES)#aca llegan todos los datos del html
    
        if myForm.is_valid():
            
            info = myForm.cleaned_data
            
            post.img=info['img']
            post.name=info['name']
            post.place=info['place']
            post.description=info['description']
            post.title=info['title']
                        
            post.save()
            
            return render(request, "pages/inicioPages.html")#volves al inicio
        
    else:
        #creo el formulario con datos que voy a cambiar osea traigo lo que ya tiene cargado el post
            myForm=NewPost(initial={'img':post.img, 'place': post.place , 'title': post.title, 'name': post.name, 'description': post.description})
            
    #voy al template para editarlo
    return render(request,"pages/editPost.html",{"myForm":myForm, "post_id":post_id})#hago que retorne de nuevo la lista de posts
