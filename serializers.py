from rest_framework import serializers
from backend import models


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Product_Category
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Product_Review
        fields = "__all__"


class ProductRelationSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    

    class Meta:

        model = models.Product
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    varients =ProductRelationSerializer(many=True)
    alsoBuy = ProductRelationSerializer(many=True)
    category = ProductCategorySerializer()
    

    class Meta:

        model = models.Product
        fields = "__all__"


class ShowcaseSerializer(serializers.ModelSerializer):
    class Meta:

        model = models.Showcase_Images
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = "__all__"


