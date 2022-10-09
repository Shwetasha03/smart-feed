from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# from home.forms import TopicsForm
from django.db.utils import IntegrityError

from home.models import Subscription


@login_required
def subscribe_topics(request):
    topics = []
    if request.method == 'POST':
        entered_topics = request.POST.getlist('topics')
        selected_topics_checkbox = request.POST.getlist('checks[]')
        user_id = request.user.id
        topics = entered_topics + selected_topics_checkbox
        print(topics)
        for value in topics:
            value = value.strip()
            if value != "":
                sub = Subscription(userid=user_id, category=value)
                try:
                    sub.save()
                except IntegrityError:
                    continue
        return render(request, 'get_sentiment/')
    return render(request, 'subscribe_topics.html', {"topics": topics})


def get_sentiment(request):
    topics = ['Sports', 'Harry Potter']
    return render(request, 'get_sentiment.html', {"topics": topics})

