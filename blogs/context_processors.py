
from .models import category
from Assignments.models import sociallink

def get_categories(request):
    categories = category.objects.all()
    return dict(categories=categories)

def get_sociallinks(request):
    # platform = platform.objects.all()
    social_links = sociallink.objects.all()
    return dict(social_links=social_links)
