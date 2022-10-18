import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()



from faker import Faker
import random
from products.models import Product , Brand , Category


def seed_brand(n):  # 20
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpeg','5.png','6.jpg']
    
    for  _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0,5)]}"
        Brand.objects.create(
            name = name , 
            image = image
        )
    print(f"Seed {n} Brnads ")


def seed_category(n): # 20
    fake = Faker()
    images = ['1.jpg','2.jpg','3.jpg','4.jpeg','5.png','6.jpg']
    
    for  _ in range(n):
        name = fake.name()
        image = f"Category/{images[random.randint(0,5)]}"
        Category.objects.create(
            name = name , 
            image = image
        )
    print(f"Seed {n} Category ")


def seed_products(n):
    fake = Faker()
    
    flag_type = ['New','Feature']
    images = ['1.jpg','2.jpg','3.jpeg','4.jpg','5.jpg','6.jpg']
    
    for _ in range(n):
        name = fake.name()
        sku=random.randint(1,100000)
        brand = Brand.objects.get(id=random.randint(1,20))
        price = round(random.uniform(20.99,99.99),2)
        desc = fake.text(max_nb_chars=1000)
        flag = flag_type[random.randint(0,1)]
        category = Category.objects.get(id=random.randint(1,20))
        image = f"Products/{images[random.randint(0,5)]}"
        
        Product.objects.create(
            name=name,
            sku=sku,
            brand = brand,
            price = price , 
            desc = desc , 
            flag = flag , 
            category = category,
            image = image 
        )
    print(f"Seed {n} Product ")




# seed_brand(20)
# seed_category(20)
seed_products(1000)