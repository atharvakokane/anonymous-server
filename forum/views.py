from django.shortcuts import render, redirect
from .models import Post, User

def choose_username(request):
    if request.method == 'POST':
        # Save the username in the session
        username = request.POST.get('username')
        if username:
            request.session['username'] = username  # Save username in session
            # You can also create a User entry in the database if you want
            user, created = User.objects.get_or_create(username=username)
            return redirect('forum:index')  # Redirect to the forum after choosing username
    return render(request, 'forum/choose_username.html')

def index(request):
    if 'username' not in request.session:
        return redirect('forum:choose_username')  # If no username in session, redirect to username page

    posts = Post.objects.all().order_by('-timestamp')
    return render(request, 'forum/index.html', {'posts': posts})

def submit_post(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            username = request.session.get('username')
            user = User.objects.get(username=username)  # Get the User object based on the username in session
            # Create a new post associated with the user
            post = Post(content=content, user=user)
            post.save()
        return redirect('forum:index')
