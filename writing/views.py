from django.shortcuts import render, redirect
from writing.forms import ProductForm
from django.views.generic import TemplateView
from writing.models import notes
from datetime import datetime

# Create your views here.
class create_view(TemplateView):
    template_name = 'create.html'
    def get(self, request):
       form = ProductForm()
       args = {'form': form}
       return render(request, self.template_name, args)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['description']
            args = {'form': form, 'text': text, "hasDuplicate": False}

            if type(text) != str:
                args.update({"text": makeErrorReadable(text)})
                return render(request, self.template_name, args)

            if hasDuplicate(text):
                args.update({"hasDuplicate": True})
                #await... for the method to say yes or no idk how to do this...
                return render(request, self.template_name, args)
                
                
            form.save()
            return redirect('http://127.0.0.1:8000/page_created', args)
            return render(request, self.template_name, args)
            
class page_created(TemplateView):
    template_name = "pageSaved.html"
    def get(self, request, *args):
        args = {}
        return render(request, self.template_name, args)
        
def makeErrorReadable(error):
    legibleError = ""
    unimportantCh = ["[", "]","''"]
    for ch in error:
        if not ch == unimportantCh.__contains__(ch):
            legibleError += ch
    return legibleError


def hasDuplicate(note):
    allNotes = notes.objects.all()
    for a in allNotes:
        if a.description == note:
            return True

    return False
