from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Person
from .forms import PersonForm
from datetime import date, timedelta


# Create your views here.
def person_list(request):
    persons = Person.objects.all()
    first_person = Person.objects.first() #a4  
    # persons = Person.objects.filter(id=first_person.id) #a4
    
    # thirty_years_ago = date.today() - timedelta(days=30*365)  a2
    # persons = Person.objects.filter(birth_date__lte=thirty_years_ago)  a2
    # persons = Person.objects.filter(age__gte=30) a1
    return render(request,'base.html',{'persons':persons})

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm()
    return render(request,'add_person.html',{'form':form})

def edit_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form = PersonForm(instance=person)
    return render(request, 'edit_person.html', {'form': form})    

def delete_person(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')
    return render(request, 'delete_person.html', {'person': person}) 


def retrieve_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
        return render(request, 'person_details.html', {'person': person})
    except Person.DoesNotExist:
        return HttpResponse("Person does not exist.")


             