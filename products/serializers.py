
from rest_framework import serializers
from .models import Product , Category , Brand , Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['name','image']

class BrandSerializer(serializers.ModelSerializer):
    class Meta :
        model = Brand
        fields = ['name','image']






class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField()
    # brand = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField(method_name='price_with_tax_1')
 
    def price_with_tax_1(self,product:Product):
        return product.price*1.1
    
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
 
    def price_with_tax_1(self,product:Product):
        return product.price*1.1
    
    class Meta:
        model= Product
        fields = ['name' ,'brand','category','price_with_tax','reviews']