from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.BigIntegerField(null=True, blank=True)

    address = models.CharField(max_length=100, blank=True, null=True)

    order_products=models.ManyToManyField('Product', blank=True,related_name='order')

    alternative_mobile = models.BigIntegerField(
        null=True, blank=True)

    userImage = models.ImageField(upload_to='photos/user/')

    cart_products = models.ManyToManyField('Product', blank=True,related_name='cart')

   



    def __str__(self):
        return self.user.first_name


class Product(models.Model):
  
  

    name = models.CharField(max_length=100)

    category=models.ForeignKey('Product_Category',on_delete=models.CASCADE,null=True)

   

    description = models.TextField()

    price = models.IntegerField()

    off_price = models.IntegerField()

    offer = models.BooleanField()

    most_popular = models.BooleanField()

    fantastic = models.BooleanField()

    stock=models.IntegerField(null=True)

    mainImage = models.ImageField(
        null=True, blank=True, upload_to=f'products/')

    firstImage = models.ImageField(
        null=True, blank=True, upload_to=f'products/')

    secondImage = models.ImageField(
        null=True, blank=True, upload_to=f'products/')

    thirdImage = models.ImageField(
        null=True, blank=True, upload_to=f'products/')

    color = models.CharField(max_length=50)
    


    varients=models.ManyToManyField('Product', blank=True,related_name='color_varients')

    alsoBuy=models.ManyToManyField('Product', blank=True,related_name='similar_varients')

    def __str__(self):
        return self.name




    
        
  

class Product_Category(models.Model):
    MOBILES = 'MOBILE'
    HEADPHONES = 'HEADPHONE'
    WATCHES = 'WATCH'

    PRODUCT_CATEGORIES = [
        (MOBILES, 'MOBILE'),
        (HEADPHONES, 'HEADPHONE'),
        (WATCHES, 'WATCH')

    ]

    name=models.CharField(max_length=50,choices=PRODUCT_CATEGORIES,null=False)

    offer=models.BooleanField(null=True)
    subCategory=models.ManyToManyField('Product_Category',blank=True)

    def __str__(self):
        return self.name

    

class Product_Review(models.Model):

   
    writer=models.ForeignKey('Profile',on_delete=models.CASCADE,null=True),
    
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True,blank=True)

    title = models.CharField(max_length=30)
    stars = models.IntegerField()
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    class Meta:
        ordering = ('date_published',)


class Showcase_Images(models.Model):
    mainShowcase1=models.ImageField('posters/showcase/')
    mainShowcase2=models.ImageField('posters/showcase/')
    mainShowcase3=models.ImageField('posters/showcase/')
    mainShowcase4=models.ImageField('posters/showcase/')

    