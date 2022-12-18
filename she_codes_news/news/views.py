from django.views import generic
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin    Added by Ben

from .models import NewsStory
from .forms import StoryForm

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    # queryset = NewsStory.objects.all().order_by("-pub_date")
    # context_object_name = 'all_stories' #added this instead of context in def get_context_data

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by("-pub_date")[:4]
        context['all_stories'] = NewsStory.objects.all().order_by("-pub_date")
        return context
    
class StoryView(generic.DetailView):
    model = NewsStory
    template_name ="news/story.html"
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)