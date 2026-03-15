from django.shortcuts import render

# Create your views here.
def galleryPage(request):
    return render(request, "gallery_page.html")
