from django.shortcuts import render
from .models import Product
from django.db.models import Avg
# Create your views here.

# def calculate_averages(self):
#         # Calculate and update average values for Product model
#         Product.objects.update(
#             average_price=Avg('price'),
#             average_ratings=Avg('product_rating'),
#             average_review_count=Avg('review_count')
#         )
        
def home(request):
    return render(request,'base.html')
    
 
