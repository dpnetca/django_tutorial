from django.shortcuts import render, HttpResponse
from .forms import GetNameForm, GetAnimalForm
from .models import Organization, Executive, Manager, Employee


def index(request):
    return render(request, "simpleforms/index.html")


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = GetNameForm(request.POST)
        # check wether form is valid
        if form.is_valid():
            # Process Form here
            # use form.cleaned_data
            fn = form.cleaned_data["first_name"]
            ln = form.cleaned_data["last_name"]
            return HttpResponse(f"ValidForm for {fn} {ln}")
    # if not post (ie if get) create a new blank form
    else:
        form = GetNameForm()
    # present html form page
    return render(request, "simpleforms/names.html", {"form": form})


def get_animal(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = GetAnimalForm(request.POST)
        # check wether form is valid
        if form.is_valid():
            # Process Form here
            # use form.cleaned_data
            species = form.cleaned_data["species"]
            breed = form.cleaned_data["breed"]
            return HttpResponse(f"ValidForm for {species} - {breed}")
    # if not post (ie if get) create a new blank form
    else:
        form = GetAnimalForm()
    # present html form page
    return render(request, "simpleforms/animals.html", {"form": form})


def view_org(request):
    orgs = Organization.objects.all()
    execs = Executive.objects.all()
    mgrs = Manager.objects.all()
    empls = Employee.objects.all()
    context = {"orgs": orgs, "execs": execs, "mgrs": mgrs, "empls": empls}
    return render(request, "simpleforms/view_org.html", context)
