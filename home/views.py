from django.shortcuts import render
from django.views.generic import TemplateView
from writing.models import notes

    
class note_view(TemplateView):
    template_name = "note.html"
    def get(self, request, id): 
        note = notes.objects.get(id=id)
        description = formatDescription(note.description)
        args = {
            "title": note.title,
            "description": description,
            "date": note.date,
        }
        return render(request, self.template_name, args)

class home_view(TemplateView):
    template_name = "home.html"
    def post(self, request):
        args = {}
        return render(request, self.template_name, args)

class titles_view(TemplateView):
    template_name = "titles.html"
    def get(self, request, parent):
        allNotes = notes.objects.all()
        allNotes = getTitlesWithParent(parent)
        args = {
            "allNotes": allNotes
        }
        return render(request, self.template_name, args)

class parent_view(TemplateView):
    template_name = "parent.html"
    def get(self, request):
        parents = getAllParents()
        args = {
            "parents": parents,
        }
        return render(request, self.template_name, args)


   
        
class default_view(TemplateView):
    template_name = "default.html"
    def get(self, request):
        args = {}
        return render(request, self.template_name, args)

def getAllDescriptions():
    allNotes = notes.objects.all()
    notesDescription = []
    for note in allNotes:
        notesDescription.append(note.title)
        description = note.description
        notesDescription.append(description)
    return notesDescription  


def getAllParents():
    allNotes = notes.objects.all()
    allParents = []
    for note in allNotes:
        noteParent = note.parent
        if not allParents.__contains__(noteParent):
            allParents.append(noteParent)
    return allParents

def getTitlesWithParent(parent):
    titles = []
    allNotes = notes.objects.all()
    for note in allNotes:
        noteParent = note.parent
        if noteParent == parent:
            titles.append(note)
    return titles

def formatDescription(description):
    formattedDescription = ""
    tabCommand = "*"
    tab = "     "
    for ch in description:
        if ch == tabCommand:
            formattedDescription += tab
        else:
            formattedDescription += ch

    return formattedDescription


