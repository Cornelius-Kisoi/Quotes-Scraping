from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render, redirect
from .scraper_service import scrape_quotes
from .models import Quote
from collections import Counter
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return redirect('/api/login/')

# Account creation
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check passwords match
        if password != confirm_password:
            return render(request, 'signup.html', {"error": "Passwords do not match"})
        
        # Check if user exists
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {"error": "Username already exists"})
        
        # Create user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created successfully!")
        return redirect('/api/login/')
    
    return render(request, 'signup.html')


@login_required
def run_scraper(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not allowed to scrape")

    result = scrape_quotes()
    return JsonResponse({"message": f"Scraped {result} quotes"})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/api/dashboard/')
        else:
            return render(request, 'login.html', {"error": "Invalid credentials"})

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('/api/login/')

def get_quotes(request):
    data = list(Quote.objects.values())
    return JsonResponse(data, safe=False)

@login_required
def dashboard(request):
    query = request.GET.get('q')

    quotes = Quote.objects.all()

    if query:
        quotes = quotes.filter(author__icontains=query)

    # Total quotes
    total_quotes = quotes.count()

    # Count tags and authors
    all_tags = []
    authors = []
    for q in quotes:
        tags = q.tags.split(",")
        all_tags.extend(tags)
        authors.append(q.author)

    tag_counts = Counter(all_tags).most_common(5)
    author_counts = Counter(authors).most_common(5)

    # tags = [tag for tag, count in tag_counts]
    # counts = [count for tag, count in tag_counts]

    context = {
        "total_quotes": total_quotes,
        "top_tags": tag_counts,
        # "tags_json": json.dumps(tags),
        # "counts_json": json.dumps(counts)
        "tags_json": json.dumps([t for t, _ in tag_counts]),
        "counts_json": json.dumps([c for _, c in tag_counts]),

        "authors_json": json.dumps([a for a, _ in author_counts]),
        "author_counts_json": json.dumps([c for _, c in author_counts ])
    }

    return render(request, "dashboard.html", context)