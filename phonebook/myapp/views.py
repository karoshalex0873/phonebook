from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import User
from django.db.models import Q

def show(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    if query:
        all_list = User.objects.filter(
            Q(First_Name__icontains=query) | 
            Q(Last_Name__icontains=query) |
            Q(Email__icontains=query)
        ).order_by('First_Name')  # Filter records based on the query
    else:
        all_list = User.objects.all().order_by('First_Name')  # 

    return render(request, 'show.html', {'users': all_list, 'search_query': query})


def display(request):
    if request.method == 'POST':
        myusers = User(
            First_Name=request.POST['first_name'],
            Last_Name=request.POST['last_name'],
            Phone=request.POST['phone_number'],
            Email=request.POST['email']
        )
        myusers.save()
        return redirect('show')  
    else:
        return render(request, 'index.html')


def delete(request, id):
    del_user = get_object_or_404(User, id=id)
    del_user.delete()
    return redirect('show')

def Spe_User(request):
    spec_users = get_object_or_404(User, First_Name='Alex')
    all_list = User.objects.all()
    return render(request, 'show.html', {'onlyuser': spec_users, 'users': all_list}) 

def edit_user(request ,user_id):
    user=get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.First_Name = request.POST['first_name']
        user.Last_Name = request.POST['last_name']
        user.Phone = request.POST['phone_number']
        user.Email = request.POST['email']
        user.save()
        return redirect('show')
    return render(request, 'index.html', {'user': user})