from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin    Added by Ben

from .models import NewsStory, Category
from .forms import StoryForm
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    # queryset = NewsStory.objects.all().order_by("-pub_date")
    context_object_name = 'all_stories' #added this instead of context in def get_context_data

    def get_queryset(self):
        '''Return all news stories.'''
        cat_id = self.request.GET.get("cat")
        if cat_id:
            return NewsStory.objects.filter(category=cat_id)
        else:
            return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        context['categories'] = Category.objects.all()
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

class UpdatePostView(generic.UpdateView):
    model = NewsStory
    template_name = "news/updatePost.html"
    fields = ['title', 'pub_date', 'category', 'content', 'image']
    # success_url = reverse_lazy('news:index') - this is a static return

    #More dynmaic, returns user to story page being edited
    def get_success_url(self) -> str:
        return reverse_lazy('news:story', kwargs={"pk":self.kwargs['pk']})

    #Ensures only authors can edit story. Otherwiae, you could import and use LoginRequiredmixin (e.g.StoryDeleteView(LoginRequiredMixin, generic.DeleteView))
    def get_queryset(self):     
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs

class DeletePostView(generic.DeleteView):
    model = NewsStory
    template_name = "news/delete_post.html"
    success_url = reverse_lazy('news:index')
    context_object_name = "story"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(author=self.request.user)
        return qs

@login_required
def like(request, pk):
# when given a pk for a newsstory, add like; if exists, remove user from tally
    news_story = get_object_or_404(NewsStory, pk=pk)
    # user = request.user
    if news_story.favourited_by.filter(username=request.user.username).exists():
        news_story.favourited_by.remove(request.user)
    else:
        news_story.favourited_by.add(request.user)
    return redirect('news:story', pk=news_story.id)

    # return redirect(reverse_lazy('news:story', kwargs={'pk: pk'}))