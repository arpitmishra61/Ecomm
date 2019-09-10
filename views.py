from django.shortcuts import render
from backend import serializers

from backend import models
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,ListCreateAPIView


class AllProduct(ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        query = {}
        data = []

        for key in self.request.GET.keys():
            data.append(key)
        print(data)    

        if 'name' in data:
            for key, value in self.request.GET.items():
                if(key!='name'):
                 query["{}".format(key)]=value
                else:

                 query["category__{}__icontains".format(key)] = value
            print(query)     

            return models.Product.objects.filter(**query)

        elif 'product' in data:
            for key, value in self.request.GET.items():
                query["name__icontains"] = value
            print(query)
            return models.Product.objects.filter(**query)

        elif 'id' in data:
             for key, value in self.request.GET.items():
                query["category__{}__icontains".format(key)] = value
             print(query)
             return models.Product.objects.filter(**query)
        elif 'idp' in data:
             for key, value in self.request.GET.items():
                query["{}__icontains".format(key[0:2])] = value
             print(query)
             return models.Product.objects.filter(**query)
        else:

                
            return models.Product.objects.all()


class Filter(ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        query = {}
        data = []

        for key in self.request.GET.keys():
            data.append(key)
        
        for key, value in self.request.GET.items():
            query["{}".format(key)] = value

            print(query)
            return models.Product.objects.filter(**query)


class Category(ListAPIView):
    serializer_class = serializers.ProductCategorySerializer

    def get_queryset(self):
        query = {}
        for key, value in self.request.GET.items():
           query["{}__icontains".format(key)] = value

           products= models.Product.objects.filter(**query)
           if(products.length):
            return products
           else:
               [{msg:"Empty"}]


class Showcase(ListAPIView):

    queryset = models.Showcase_Images.objects.all()

   
    serializer_class = serializers.ShowcaseSerializer


class Reviews(ListAPIView):
    queryset = models.Product_Review.objects.all()
    print(queryset)
    serializer_class = serializers.ReviewSerializer





class CartProductsAPI(ListCreateAPIView):
    
    def get_queryset(self):
        query = {}
        
          
        print()
        profile=models.Profile.objects.get(id=self.kwargs['pk'])
        print(profile.cart_products.all())

        cartProducts=profile.cart_products.all()
        print(cartProducts)
        return cartProducts
        
       

    serializer_class = serializers.ProductRelationSerializer

    


