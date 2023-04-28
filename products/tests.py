from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

# Test Models 
from .models import Product , Brand , Category

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        new_brand = Brand.objects.create()
        new_category = Category.objects.create()
        Product.objects.create(
            name='product1', 
            sku=3123,
            brand = new_brand , 
            price = 100 , 
            desc = ' test desc' , 
            flag = 'New' , 
            category = new_category , 
            image = SimpleUploadedFile(name='test_image.jpg', content=open('/Users/macbook/Downloads/sgd-1.jpg', 'rb').read(), content_type='image/jpeg') , 
            quantity = 5 , 
            )
        
    def test_product_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'Name')
        
        
    def test_first_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)
        

    # Test Views        
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
