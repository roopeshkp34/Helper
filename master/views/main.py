from django.shortcuts import render
import pandas as pd

from django.http.response import JsonResponse
from django.db.models import Q
from master.models import Kuri

# Create your views here.


def index(request):
    objects = Kuri.objects.all().order_by('refer_id')
    return render(request, "index.html", {"objects": objects})

def save(request):
    try:
        file = request.FILES.get("file")
        if file:
            df = pd.read_excel(file)
            df = df.fillna("")
            for set in df.itertuples():
                print(set)
                Kuri.objects.create(refer_id=set.number, first_name=set.first_name.upper(), last_name=set.last_name.upper(), details=set.details.upper(), amount=set.amount)
        else:
            number = request.POST["number"]
            first_name = request.POST["first_name"]
            last_name = request.POST.get("last_name")
            details = request.POST.get("details")
            amount = request.POST.get("amount")
            Kuri.objects.create(refer_id=number, first_name=first_name.upper(), last_name=last_name.upper(), details=details.upper(), amount=amount)
            
        return JsonResponse(
                {"message": "Created Successfully", "status": "success"}
            )
    except Exception as e:
        return JsonResponse(
                {"message": str(e), "status": "failed"}
            )
    
def search_user(request):
    search_term = request.GET.get("search_term")
    users = Kuri.objects.filter(Q(first_name__contains=search_term) | Q(last_name__contains=search_term) | Q(details__contains=search_term)).order_by("id")
    return JsonResponse({"status": "success", "data": list(users.values())})