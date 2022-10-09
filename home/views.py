import json
import os

import requests
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.shortcuts import render, redirect

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
        for value in topics:
            value = value.strip()
            if value != "":
                sub = Subscription(userid=user_id, category=value)
                try:
                    sub.save()
                except IntegrityError:
                    continue
        return redirect('sentiments')
    return render(request, 'subscribe_topics.html', {"topics": topics})


@login_required
def get_sentiment(request):
    first_15_subs = Subscription.objects.filter(userid=request.user.id).order_by('-id').all()[:15]
    topics = [item.category for item in first_15_subs]
    filtered_response = []
    if request.method == 'POST':
        if "topic" not in request.POST:
            messages.error(request, "Food Post failed! Please enter all details.")
            return redirect('sentiments')
        topic = request.POST["topic"]
        vibe = request.POST["vibe"]

        url = os.getenv("API_URL") + topic
        headers = {'auth': os.getenv("AUTH_TOKEN")}
        body = {}

        response = requests.post(url, json=body, headers=headers)
        json_response = json.loads(json.JSONDecoder().decode(response.text))
        json_response = [{'text': 'Tweet', 'sentiment': 'Sentiment'}] + json_response
        for item in json_response:
            if item["sentiment"] == vibe or vibe == "ALL":
                filtered_response.append(item)

    return render(request, 'get_sentiment.html', {"topics": topics, "results": filtered_response})
