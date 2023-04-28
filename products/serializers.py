
from django.db.models.aggregates import Avg
from rest_framework import serializers
from .models import Product , Category , Brand , Review , ProductImages


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['name','image']

class BrandSerializer(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = ['name','image']






class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField(method_name='price_with_tax_1')
    avg_review = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField(method_name='get_reviews_count')
 
    def price_with_tax_1(self,product:Product):
        return product.price*1.1
    
    def get_avg_review(self,product:Product):
        avg =product.product_review.aggregate(myavg=Avg('rate'))
        avg_rate = avg['myavg']
        if avg_rate:
            avg_rate = round(avg_rate,2)
        else:
            avg_rate = 0
        return avg_rate    
    
    
    def get_reviews_count(self,product:Product):
        reviews = product.product_review.all().count()
        return reviews
    
    class Meta:
        model= Product
        fields = '__all__'
        
    



class BrandSerializerDetail(serializers.ModelSerializer):
    products = ProductSerializer(source='product_brand', many=True)
    class Meta :
        model = Brand
        fields = ['name','image','products']
        
        
class CategorySerializerDetail(serializers.ModelSerializer):
    products = ProductSerializer(source='product_category', many=True)
    class Meta :
        model = Category
        fields = ['name','image','products']
        
        

class ProductReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = ['user','review','rate','created_at']
        
        
class ProductSerializerDetail(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField(method_name='price_with_tax_1')
    reviews = ProductReviewSerializer(source='product_review', many=True)
    avg_review = serializers.SerializerMethodField()
    reviews_count = serializers.SerializerMethodField(method_name='get_reviews_count')   
    images = ProductImagesSerializer(source='product_image',many=True)  
     
    def price_with_tax_1(self,product:Product):
        return product.price*1.1
    
    def get_avg_review(self,product:Product):
        avg =product.product_review.aggregate(myavg=Avg('rate'))
        avg_rate = avg['myavg']
        if avg_rate:
            avg_rate = round(avg_rate,2)
        else:
            avg_rate = 0
        return avg_rate    

    def get_reviews_count(self,product:Product):
        reviews = product.product_review.all().count()
        return reviews
    

    class Meta:
        model= Product
        fields = ['name' ,'brand','category','price_with_tax','reviews','reviews_count','avg_review','images']