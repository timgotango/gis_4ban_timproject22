from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription

@method_decorator(login_required, 'get')    # 저 아래 get 방식에 login_required 적용하겠다~
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):    # get 요청이 들어왔을 때 어떻게 처리해줄지!
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])
        subscription = Subscription.objects.filter(user=user,
                                                   project=project)
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': kwargs['project_pk']})    # 구독

class SubscriptionListView(ListView):
    model = Article                                     # 모델은 Article!
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 20

    def get_queryset(self):
        # subscription 안에 있는 project만 list 형태로 가져올 것이다~
        project_list = Subscription.objects.filter(user=self.request.user).values_list('project')
        # project 안의 article들을 모두 가져올 것이다~
        article_list = Article.objects.filter(project__in=project_list)
        return article_list