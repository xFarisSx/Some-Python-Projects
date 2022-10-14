from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == 'clicked' :
                    item.complete = True
                    print("wow")
                else:
                    item.complete = False
                    
                item.save()
            
        elif response.POST.get("newItem"):
            if 25 > len(response.POST.get("new")) > 2:
                text = response.POST.get("new")
                ls.item_set.create(text= text, complete=False)
            else:
                print("invalid")
        for item in ls.item_set.all():
            if response.POST.get("delete"+str(item.id)) == 'delete' :
                item.delete()
                print("wow")
                    

        
    
    return render(response, "main/list.html", {"ls": ls})

def note(response, item):
    currentitem = Item.objects.get(id=item)
    if response.method == "POST":
        if response.POST.get("save"):
            text = response.POST.get("text")
            currentitem.note_set.create(text=text)
            return HttpResponseRedirect(f"/view/{currentitem.id}/note")
    if not currentitem.note_set.all():
        note = ''
    else:
        note = [*currentitem.note_set.all()][-1]
        

    return render(response, "main/note.html", {"item":currentitem, "note":note})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect(f"/view/{t.id}")
       
        
    else:
        form = CreateNewList()
    return render(response, 'main/create.html', {'form':form})

def view(response):
    return render(response, 'main/view.html',{})