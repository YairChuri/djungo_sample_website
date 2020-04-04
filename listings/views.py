from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listings': paged_listing
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    print(request.path)
    return render(request, 'listings/listing.html')
    
def search(request):
    return render(request, 'listings/search.html')