from multiprocessing import context
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect,reverse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.http import HttpResponseRedirect


from .models import(
    Banner,
    Products,
    Category,
    ProductREVIEWS,
    ProductOrder,
    User,
    ShopingCart
)

from .forms import (
    add_product_info,
    update_product_info,
    UpdateFeedbackForm,
)

from user_profile.decorators import(
    not_logged_in_required
)
from django.contrib.auth.decorators import login_required





def home(request):

    

    #banners__________________________
    banners = Banner.objects.all()
    total_banners = banners.count()
    list = []
    
    for i in range(0,total_banners):
        list.append(i)

    #all products_____________________
    all_products = Products.objects.all()
    categories = Category.objects.all()







    context ={
        "banners":banners,
        "banner_range":list,
        "all_products":all_products,
        "categories": categories,
        #"TotalProductsFeedback":TotalProductsFeedback
    }
    return render(request,'home.html', context)


def category_items(request,category_id):
    category = get_object_or_404(Category, pk=category_id)
    category_products = category.categoty_related_name.all()


    page = request.GET.get('page', 1)
    paginator = Paginator(category_products, 30)
    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(1)
    except PageNotAnInteger:
        products = paginator.page(1)
        return redirect("/")


    context= {
        "category":category,
        "products":products,  
        "paginator":paginator

    }
    return render(request,'category_products.html', context)


def all_products(request):
    all_products = Products.objects.all()
    total_products = all_products.count()

    page = request.GET.get('page', 1)
    paginator = Paginator(all_products, 30)
    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(1)
    except PageNotAnInteger:
        products = paginator.page(1)
        return redirect("/")


    context= {
        "products":products,  
        "paginator":paginator,
        "total_products":total_products
    }
    return render(request,'all_products.html', context)



#quick view
def quick_view(request, quick_view_id):

    quick_view = get_object_or_404(Products, pk=quick_view_id)


    AllProductFeedback = quick_view.productREVIEWrelatedNAME.all()
    TotalProductsFeedback = AllProductFeedback.count()


    
    TotalRatings = 0
    AverageRating = 0

    AllOneStar = AllTwoStar = AllThreeStar = AllFourStar = AllFiveStar = 0
    OneStarAveragePercentage = TwoStarAveragePercentage = ThreeStarAveragePercentage = FourStarAveragePercentage = FiveStarAveragePercentage = 0

    if TotalProductsFeedback !=0 :
        AllOneStar = quick_view.productREVIEWrelatedNAME.filter(rating=1).count()
        AllTwoStar = quick_view.productREVIEWrelatedNAME.filter(rating=2).count()
        AllThreeStar = quick_view.productREVIEWrelatedNAME.filter(rating=3).count()
        AllFourStar = quick_view.productREVIEWrelatedNAME.filter(rating=4).count()
        AllFiveStar = quick_view.productREVIEWrelatedNAME.filter(rating=5).count()


        OneStarAveragePercentage = round((quick_view.productREVIEWrelatedNAME.filter(rating=1).count() / TotalProductsFeedback)*100,1)
        TwoStarAveragePercentage = round((quick_view.productREVIEWrelatedNAME.filter(rating=2).count() / TotalProductsFeedback)*100,1)
        ThreeStarAveragePercentage = round((quick_view.productREVIEWrelatedNAME.filter(rating=3).count() / TotalProductsFeedback)*100,1)
        FourStarAveragePercentage = round((quick_view.productREVIEWrelatedNAME.filter(rating=4).count() / TotalProductsFeedback)*100,1)
        FiveStarAveragePercentage = round((quick_view.productREVIEWrelatedNAME.filter(rating=5).count() / TotalProductsFeedback)*100,1)


    for ProductRating in AllProductFeedback:
        rating = ProductRating.rating # rating = field name of ProductREVIEWS model
        if rating:
            TotalRatings += rating
            AverageRating = round(TotalRatings/TotalProductsFeedback,1)


    user_has_bought_product = False
    if request.user.is_authenticated:
        products_bought_by_user = Products.objects.filter(ProductOrderRelatedName__User=request.user)
        
        if quick_view in products_bought_by_user:
            user_has_bought_product = True 
        else:
            user_has_bought_product = False 

    
    context = {
        "quick_view":quick_view,
        "TotalProductsFeedback":TotalProductsFeedback,
        "AllProductFeedback":AllProductFeedback,
        "AverageRating":AverageRating,
        "AllOneStar":AllOneStar,
        "AllTwoStar":AllTwoStar,
        "AllThreeStar":AllThreeStar,
        "AllFourStar":AllFourStar,
        "AllFiveStar":AllFiveStar,
        "OneStarAveragePercentage":OneStarAveragePercentage,
        "TwoStarAveragePercentage":TwoStarAveragePercentage,
        "ThreeStarAveragePercentage":ThreeStarAveragePercentage,
        "FourStarAveragePercentage":FourStarAveragePercentage,
        "FiveStarAveragePercentage":FiveStarAveragePercentage,
        "user_has_bought_product":user_has_bought_product
        

    }
        
    return render(request, 'quickVIEW_item.html', context)

    

#search product____________________________________________
def search_products(request):
    search_key = request.GET.get('search', None)
      

    search_products = Products.objects.filter(
        Q(product_title__icontains=search_key)|
        Q(product_desc__icontains=search_key)|
        Q(product_price__icontains=search_key)|
        Q(offer_price__icontains=search_key)|
        Q(total_stock__icontains=search_key)|
        Q(product_category__title__icontains=search_key)

    ).distinct()

    if search_products.count() !=0:

        context = {
            "search_products":search_products,
            "search_key":search_key,
        }
        return render(request, 'search.html', context)

    else:
        context = {
            "search_key":search_key,
        }
        return render(request, 'sorry.html', context)



#my products_____________________________________________
@login_required(login_url='login_user')  
def my_products(request):

    merchandise_product = request.user.merchandise_product_related_name.all()
    total_merchandise_product = merchandise_product.count

    page = request.GET.get('page', 1)
    paginator = Paginator(merchandise_product, 30)
    try:
        products = paginator.page(page)
    except EmptyPage:
        products = paginator.page(1)
    except PageNotAnInteger:
        products = paginator.page(1)
        return redirect("/")

    context = {
        "products":products,  
        "paginator":paginator,
        "total_merchandise_product":total_merchandise_product,
        "merchandise_product":merchandise_product
    }


    return render(request, "my_products.html", context)

    

#add product______________________________________________
@login_required(login_url='login_user')
def add_product(request):
    submitted = False
    if request.method == "POST":
        form = add_product_info(request.POST)
        form = add_product_info(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user

            if form.instance !='':
                form.save()
                messages.success(request,"Successfully product added.")
                return redirect("add_product")
        else:
            form = add_product_info()
            if 'submitted' in request.GET:
                submitted = True


    form = add_product_info
    context = {
        "form":form 
    }

    return render(request, "add_product.html", context)


#update product____________________________________________
def update_product(request,id):
    product = Products.objects.get(pk=id)
    form = update_product_info(request.POST or None, instance=product)
    
    if request.method == 'POST' and form.is_valid():
        form = update_product_info(request.POST, request.FILES, instance=product)
        form.save()
        print(form.errors)
        messages.success(request,"Successfully product information updated.")
        return redirect("my_products")

    context = {
        'product':product,
        "form":form
    }
    
    return render(request, "update_product.html", context)



#deldete product____________________________________
def delete_product(request,id):
    Products.objects.get(pk=id).delete()
    messages.success(request,"Successfully product deleted.")
    return redirect("my_products")



#add feedback_______________________________________ 
def feedBack(request,quick_view_id):
    quick_view = get_object_or_404(Products, pk=quick_view_id)

    if request.method == "POST" and request.user.is_authenticated:
        try:
            ProductREVIEWS.objects.create(
                user=request.user,
                product=quick_view,
                feedBACK=request.POST.get('feedBACK'),
                rating=request.POST.get('product_rating'), 
            )
            messages.success(request,"Thanks for your feedback.")
            return redirect('quick_view', quick_view_id)
        except:
            messages.warning(request,"You've already given feedback.")
            return redirect('quick_view', quick_view_id)

    else:
        messages.warning(request,"Sorry we can't take your feedback.")
        return redirect('quick_view', quick_view_id)



#update feedback_____________________________________
def UpdateFeedback(request, id):

    feedback = ProductREVIEWS.objects.get(pk=id)
    product_id = feedback.product.id
    reviewers = feedback.user

    if request.method == "POST":
        form = UpdateFeedbackForm(request.POST)

        if form.is_valid() and reviewers.id == request.user.id:
            
            feedBACK = request.POST.get('UpdateFeedBACK')
            UpdateRating = request.POST.get('UpdateRating')

            feedback.feedBACK = feedBACK
            feedback.rating = UpdateRating
            
            feedback.save()
            messages.success(request, "Feedback is updated")

    return redirect('quick_view', product_id)

    
#feedback delete
def DeleteFeedback(request,id):

    feedback = ProductREVIEWS.objects.get(pk=id)
    product_id = feedback.product.id

    feedback.delete()
    messages.success(request,"Successfully your feedback deleted.")
    return redirect(reverse('quick_view', args=[product_id]))


#order
def Order(request, quick_view_id):
    OrderProduct = get_object_or_404(Products, pk=quick_view_id)
    #  product_image

    if request.method == "POST" and request.user.is_authenticated:
   
        ProductOrder.objects.create(
            User=request.user,
            img = OrderProduct.product_image,
            CustomerName=request.POST.get('CustomerName'),
            Product=OrderProduct,
            ProductTitle=request.POST.get('product_title'),
            Price=request.POST.get('product_price'), 
            Shipping=request.POST.get('ShippingCost'),
            TotalPrice=request.POST.get('TotalCost'),
            Quantity=request.POST.get('product_quantity'),
            Email=request.POST.get('email'),
            Phone=request.POST.get('phone'),
            ThanaPostCode=request.POST.get('ThanaPostCode'), 
            FullAddress=request.POST.get('FulllAdress'), 
        )
        messages.success(request,"Thanks for your order.")
        return redirect('OrderList')
        

    context = {
        "OrderProduct":OrderProduct,
    }
    return render(request, "order_form.html", context)

#order list
def OrderList(request):
    UserAllOrder = request.user.UserOrderRelatedName.all()
    DeliveredOrder = request.user.UserOrderRelatedName.filter(OrderStatus='Delivered')
    CancelledOrder = request.user.UserOrderRelatedName.filter(OrderStatus='Canceled')
    context = {
        "UserAllOrder":UserAllOrder,
        "UserTotalOrder":UserAllOrder.count(),
        "DeliveredOrder":DeliveredOrder,
        "CancelledOrder":CancelledOrder,
    }
    return render(request, "order_list.html", context)


def OrderTracking(request):

    OrderId = request.GET.get('orderTracking')

    try:
        if request.method=="GET":
            TrackingOrder=ProductOrder.objects.get(pk=OrderId)
            context = {
                "TrackingOrder":TrackingOrder,
            }
            return render(request, 'order_tracking_info.html',context)

    except:
        messages.warning(request,"You you have given wrong order ID, please try again with right ID.")
        return redirect("OrderList")


#delete order
def DeleteOrder(request,id):
    order = ProductOrder.objects.get(pk=id)

    order.delete()
    messages.success(request,"Successfully your order deleted.")
    return redirect('OrderList')


#shopping cart
def ShoppinfCart(request,id):
    product = get_object_or_404(Products, pk=id)
    try:
        if request.user.is_authenticated:
            ShopingCart.objects.create(
                User = request.user,
                Product = product
            )
            messages.success(request,"Successfully your product added to the cart.")
        return redirect('quick_view', id)
    except:
        messages.warning(request,"You already added this product.")
        return redirect('quick_view', id)

def DeleteCartItem(request,id):
    CartItem = get_object_or_404(ShopingCart, pk=id)
    CartItem.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

        

    




        
        




    



