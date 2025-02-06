from .models import Collection, Rec
from .forms import RecForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView
from django.urls import reverse_lazy
import requests
from bs4 import BeautifulSoup
from django.shortcuts import get_object_or_404

class NewCollectionView(CreateView):
    model = Collection
    fields = ["name"]
    template_name = "new_collection.html"

    def form_valid(self, form):
        form = form.save(commit=False)
        form.user = self.request.user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('new_collection')
    
class RecListView(ListView, FormView):
    model = Rec
    form_class = RecForm
    template_name = "rec_list.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Rec.objects.filter(collection=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):

        collection_pk = self.kwargs['pk']
        collection = get_object_or_404(Collection, pk=collection_pk)
        self.model.objects.create(
                    collection = collection,
                    title = form.data["title"],
                    author = form.data["author"],
                    word_count = form.data["word_count"],
                    summary = form.data["summary"],
                    url = form.data["url"],
                    notes = form.data["notes"]
                )
        """
        AO3 doesn't allow web scraping 
        try:
            get_url = requests.get(url)
            print(get_url.status_code)
            if int(get_url.status_code) == 200:
                fic_data = self.scrap_fic(get_url)

                collection_pk = self.kwargs['pk']
                get_collection = get_object_or_404(Collection, pk=collection_pk)

                self.model.objects.create(
                    collection = get_collection,
                    title = fic_data["title"],
                    author = fic_data["author"],
                    word_count = int(fic_data["word_count"]),
                    summary = fic_data["summary"],
                    url = url,
                    notes = notes
                )
                return super().form_valid(form)
        except:
            super().form_valid(form)"""
        return super().form_valid(form)

    def get_success_url(self):
        collection = int(self.kwargs["pk"])
        print(collection)
        return reverse_lazy("rec_list", args=[collection])
    
    def scrap_fic(self, get_url):
        
        souped_page = BeautifulSoup(get_url.content, 'html.parser')
        preface = souped_page.find("div", {"class": "preface"})
        title = preface.find("h2").get_text()
        author = preface.find("h3").get_text()
        
        summary_module = souped_page.find("div", {"class": "summary"})
        summary = summary_module.find("p").get_text()

        word_count = souped_page.find("dd", {"class": "words"}).get_text()

        return dict({
            "title": title.strip(),
            "author": author.strip(),
            "summary": summary,
            "word_count": word_count.replace(",", "")
        })