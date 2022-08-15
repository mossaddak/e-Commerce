from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import login, logout, authenticate

from notification.models import Notification
from .forms import (
    UserRegistrations,
    LoginForm,
    UserProfileUpdateForm,
    ProfilePictureUpdateForm,
    BannerUploadForm,
    
    
    )
from django.views.decorators.cache import never_cache
from django.contrib import messages
from .decorators import(
    not_logged_in_required
)
from django.contrib.auth.decorators import login_required
from .models import(
    User,
    Follow,
    Address
) 



# Create your views here.
@never_cache
@not_logged_in_required
def login_user(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data.get('username'),
                password=login_form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect("/")

            else:
                messages.warning(request, "You've given wron information, try again!")
                return redirect("login_user")

    context = {
        "login_form": login_form
    }
    return render(request, 'login.html', context)

# logout user
@never_cache
def logout_user(request):
    logout(request)
    return redirect("/")



@never_cache
def singup(request):
    form = UserRegistrations()
    if request.method == "POST":
        form = UserRegistrations(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            messages.success(request, "Registrations Successfully done!")
            return redirect("login_user")
        else:
            print(form.errors)
            
    context ={
        "form":form
    }
    return render(request,'singup.html', context)



def forgot_password(request):
    context ={

    }
    return render(request,'forgot.html', context)


from django.db.models import Count
@login_required(login_url='login_user')  
def user_profile(request):
    account = get_object_or_404(User, pk=request.user.pk)

    form = UserProfileUpdateForm(instance=account)
    counter = User.objects.annotate( number_of_reviews=Count('merchandise_product_related_name__productREVIEWrelatedNAME'))

    UserAddress = request.user.AddresRelatedName.all() 

    


    if request.method == "POST":
        if request.user.pk != account.pk:
            redirect("/")
        form = UserProfileUpdateForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile has been updated.")
            return redirect("user_profile")
        else:
            print(form.errors)

    context = {
        "account":account,
        "form":form,
        "counter":counter,
        "UserAddress":UserAddress
    }

    return render(request, 'profile.html', context)



#profile picturw picture
@login_required(login_url='login_user')  
def change_profile_picture(request):
    if request.method == "POST":
        form = ProfilePictureUpdateForm(request.POST, request.FILES)
        if form.is_valid():

            image = request.FILES['profile_image']
            user = get_object_or_404(User, pk=request.user.pk)

            if request.user.pk != user.pk:
                return redirect("user_profile")

            user.profile_image = image
            user.save()
            messages.success(request,"Profile picture update success!")

    return redirect('user_profile')


@login_required(login_url='login')  
def change_banner(request):
    if request.method == "POST":
        form = BannerUploadForm(request.POST, request.FILES)
        if form.is_valid():

            image = request.FILES['banner_input']
            user = get_object_or_404(User, pk=request.user.pk)

            if request.user.pk != user.pk:
                return redirect("my_products")

            user.StoreBanner = image
            user.save()
            messages.success(request,"Banner is updated!")
        else:
            print(form.errors)

    return redirect('my_products')



def Store(request, username):
    store = get_object_or_404(User, username = username)
    followers = store.followers.all()
    following = False
    muted = None


    if request.user.is_authenticated:
        if request.user.id == store.id:
            return redirect("my_products")

        followers = store.followers.filter(followed_by__id = request.user.id)

        if followers.exists():
            following = True

    if following:
        queryset = followers.first()
        if queryset.muted:
            muted = True 
        else:
            muted = False


    context = {
        "store":store,
        "following":following,
        "muted":muted
    }
    return render(request, "store.html", context)


@login_required(login_url="login")
def follow_or_unfollow_user(request, user_id):
    followed = get_object_or_404(User, id = user_id)
    followed_by = get_object_or_404(User, id = request.user.id)

    follow, created = Follow.objects.get_or_create(followed = followed, followed_by = followed_by)

    if created:
        followed.followers.add(follow)
        messages.success(request,f"You started following { followed.username }")
        
    else:
        followed.followers.remove(follow)
        follow.delete()
        messages.success(request,f"You unfollowed { followed.username }. Don't worry, { followed.username } won't know about it.")

    return redirect("Store", username = followed.username)


#notifications
@login_required(login_url="login_user")
def user_notifications(request):
    notifications = Notification.objects.filter(
        user = request.user,
        is_seen = False
    )
    for notification in notifications:
        notification.is_seen = True
        notification.save()
    return render(request, 'notifications.html')


#add address
def Adress(request):

    if request.method == "POST" and request.user.is_authenticated:
        
        Address.objects.create(
            User = request.user,
            Home = request.POST.get('home'),
            Area = request.POST.get('area'), 
            PostOffice = request.POST.get('PostOffice'),
            Upzilla = request.POST.get('upzilla'),
            Zilla = request.POST.get('zilla'), 
        )

        messages.success(request,"Your addrss is added.")
        return redirect('user_profile')

#delete address
def DeleteAddress(request, id):
    address = get_object_or_404(Address, pk=id)
    address.delete()
    messages.success(request,"Your addrss is deleted.")
    return redirect('user_profile')

#edit address

def EditAddress(request, id):
    UpdateAddress = get_object_or_404(Address, pk=id)
    AddressAdder = UpdateAddress.User.id

    if request.method == "POST":

        if AddressAdder == request.user.id:
            UpdateAddress.Home = request.POST.get('home')
            UpdateAddress.Area = request.POST.get('area')
            UpdateAddress.PostOffice = request.POST.get('PostOffice')
            UpdateAddress.Upzilla = request.POST.get('upzilla')
            UpdateAddress.Zilla = request.POST.get('zilla')
            
            UpdateAddress.save()
            messages.success(request,"Your addrss is updated.")
    return redirect('user_profile')









