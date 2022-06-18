from multiprocessing import context
from django.shortcuts import render, redirect
from dojo_ninja_app.models import dojos, ninjas

def index(request):
    context = {
        "dojos": dojos.objects.all(),
    }
    return render(request, "index.html",context)
def createDojo(request):
    if request.method == "POST":
        dojos.objects.create(
        name = request.POST["name"],
        city = request.POST["city"],
        state = request.POST["state"]
        )
        print(f"An new dojo created with id {dojos.id}")   
    return redirect("/")

def createNinja(request):
    if request.method == "POST":
        dojo_selected = dojos.objects.get(id=request.POST["dojo_id"])
        ninjas.objects.create( 
            dojo_id=dojo_selected,
            first_name = request.POST["first_name"],
            last_name = request.POST["last_name"]
        )
        print(f"An new ninja created with id {ninjas.id}")   
    return redirect("/")