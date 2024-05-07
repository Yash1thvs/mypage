from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
        return HttpResponse(challenges)
    except:
        return HttpResponseNotFound("not supported")
