from django.shortcuts import render


# from home.forms import TopicsForm


def subscribe_topics(request):
    topics = []
    if request.method == 'POST':
        entered_topics = request.POST.getlist('topics')
        selected_topics_checkbox = request.POST.getlist('checks[]')
        print(entered_topics)
        print(selected_topics_checkbox)
        topic = entered_topics.extend(selected_topics_checkbox)
        return render(request, 'get_sentiment')
    return render(request, 'subscribe_topics.html', {"topics": topics})


def get_sentiment(request):
    topics = ['Sports', 'Harry Potter']
    return render(request, 'get_sentiment.html', {"topics": topics})

