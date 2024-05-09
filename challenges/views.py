from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Test january",
    "february": "Test February",
    "march": "Test March",
    "april": "Test April",
    "may": "Test May",
    "june": "Test June",
    "july": "Test July",
    "august": "Test August",
    "september": "Test September",
    "october": "Test October",
    "november": "Test November",
    "december": "Test December",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        "months": months
    })


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if month < 1:
        return HttpResponseNotFound("Not Valid")
    if month > len(months):
        return HttpResponseNotFound("Not Valid")
    redirect_month = months[month-1]
    redirect_url = reverse("month-challenge", args=redirect_month)
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    try:
        challenges = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            "text": challenges
        })
    except:
        response = render_to_string("404.html")
        return HttpResponseNotFound(response)
