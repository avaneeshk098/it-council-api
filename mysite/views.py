from django.http import HttpResponse
from django.shortcuts import render
import sheet_api
import json

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def backend(request):
    return render(request, "backend.html")


def backend_(request):
    data = []
    body = json.loads(request.body)
    data.append(body.get("name", "NAN"))
    data.append(body.get("class", "NAN"))
    data.append(body.get("section", "NAN"))
    data.append(body.get("dps_admission_number", "NAN"))
    data.append(body.get("phone", "NAN"))
    data.append(body.get("discord", "NAN"))

    sheet_api.sheet.insert_row(data, 1)

    """name = request.POST.get("name", "NAN").
    class_ = request.POST.get("class", "NAN")
    section = request.POST.get("section", "NAN")
    addmission_no = request.POST.get("section", "NAN")
    discord_id = request.POST.get("section", "NAN")
    phone_number = request.POST.get("section", "NAN")"""

    return HttpResponse("sent")
