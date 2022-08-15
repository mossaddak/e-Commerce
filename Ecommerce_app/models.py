from django.db import models
from user_profile.models import User
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db.models import Avg, Count


#banners________________
class Banner(models.Model):
    banner_img = models.ImageField(upload_to = "0_home_banner", null=True)
    banner_created_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.pk) + "(Data:" + str(self.banner_created_date) + ")"

#category______________
class Category(models.Model):
    title = models.CharField(blank=True, null=True, max_length = 100)

    def __str__(self):
        return str(self.title)

#available Color 
class Available_color(models.Model):
    title = models.CharField(blank=True, null=True, max_length=250)


 
#products______________
class Products(models.Model):
    user = models.ForeignKey(User, related_name="merchandise_product_related_name", on_delete=models.CASCADE, blank=True, null=True)
    product_title = models.CharField(blank=True, null=True, max_length = 250)
    brand = models.CharField(max_length=250, blank=True, null=True)
    product_desc = RichTextField(blank=True, null=True)
    moreINFO = models.TextField(blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)
    offer_price = models.IntegerField(blank=True, null=True)
    total_stock = models.IntegerField(blank=True, null=True)
    product_category = models.ForeignKey(Category, related_name="categoty_related_name", on_delete=models.CASCADE, blank=True, null=True)
    product_image = models.ImageField(blank=True, null=True, upload_to = "1_products_img")
    warranty = models.IntegerField(blank=True, null=True)
    gurantee = models.IntegerField(blank=True, null=True)
    available_color = models.ForeignKey(Available_color, related_name="available_color_related_name", on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return f'{self.pk}.{self.product_title}({self.user})'


    #average rating
    def AverageRating(self):
        reviews = ProductREVIEWS.objects.filter(product=self).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    #count total feedback
    def countReview(self):
        reviews = ProductREVIEWS.objects.filter(product=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

        

        #Annotated_output = Model.Objects.annotate(variable=aggregate_function(columnname))

    


#products reviews
class ProductREVIEWS(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='userREVIEW',on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='productREVIEWrelatedNAME',on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True, null=True)
    feedBACK = models.TextField(blank=True, null=True)
    createdDate = models.DateField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'product'),
                name='add_to_cart_once'
            ) 
        ]


    
    def __str__(self):
        return f'{self.pk}.{self.product}({self.user})'


#product order
class ProductOrder(models.Model):

    User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='UserOrderRelatedName',on_delete=models.CASCADE)
    CustomerName = models.CharField(max_length=250, blank=True, null=True)
    Product = models.ForeignKey(Products, related_name='ProductOrderRelatedName',on_delete=models.CASCADE)
    ProductTitle = models.CharField(max_length=250, blank=True, null=True)
    Price = models.IntegerField()
    Shipping = models.IntegerField(null=True)
    TotalPrice = models.IntegerField(null=True)
    Quantity = models.IntegerField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=250, blank=True, null=True)
    ThanaPostCode = models.CharField(max_length=250, blank=True, null=True)
    FullAddress = models.TextField(blank=True, null=True)
    createdDate = models.DateField(auto_now=True)
    img = models.ImageField(blank=True, null=True)
 

    ORDER_STATUS_CHOICES = [
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('On the way', 'On the way'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled')
        
    ]
    OrderStatus = models.CharField(max_length=30, choices=ORDER_STATUS_CHOICES, blank=True, null=True)

    def __str__(self):
        return f'{self.pk}.{self.User}({self.Product})'



class ShopingCart(models.Model):
    User = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='UserShoppingCartRelatedName',on_delete=models.CASCADE)
    Product = models.ForeignKey(Products, related_name='ShoppingCartRelatedName',on_delete=models.CASCADE)
    createdDate = models.DateField(auto_now=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('User', 'Product'),
                name='review_once'
            )   
        ]

    def __str__(self):
        return f'{self.pk}.{self.User}({self.Product})'



    


