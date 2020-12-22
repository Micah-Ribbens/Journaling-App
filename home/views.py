from django.shortcuts import render
from django.views.generic import TemplateView
from writing.models import notes

    
class home_view(TemplateView):
    template_name = "home.html"
    def get(self, request):
        allNotes = getAllDescriptions()
        args = {
            "allNotes": allNotes
            }
        return render(request, self.template_name, args)


def getAllDescriptions():
    allNotes = notes.objects.all()
    notesDescription = []
    timesGoneThrough = 0
    for note in allNotes:
        timesGoneThrough += 1
        notesDescription.append(f"Exercise {timesGoneThrough}")
        description = note.description
        notesDescription.append(description)
    return notesDescription  





