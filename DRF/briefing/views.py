from django.shortcuts import render, redirect

def briefing_page(request):
    return render(request, "briefing/briefing_page.html", {})