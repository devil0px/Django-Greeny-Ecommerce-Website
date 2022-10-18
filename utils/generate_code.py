
import random

def generaste_code(length=8):
    numbers = '0123456789'
    return ''.join(random.choice(numbers) for _ in range(length))
