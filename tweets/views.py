from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.utils.http import is_safe_url
from django.conf import settings
from .models import Tweet
from .forms import TweetForm
import random 
# Create your views here.

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

def home_view(request, *args, **kwargs):
    return render(request, template_name="pages/home.html", context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    print("is ajax",request.is_ajax())
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(),status=201) #created items
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect("/")
        form = TweetForm()
        if form.errors:
            if request.is_ajax():
                return JsonResponse(form.errors, status=400)
    return render(request, "components/forms.html", context={"form":form})

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    # tweet_lists = [{"id":x.id, "content":x.content, "likes":random.randint(0,23)} for x in qs]
    tweet_lists = [x.serialize() for x in qs]
    data = {
        "response":tweet_lists
    } 
    return JsonResponse(data)
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args,kwargs)
    """
    REST API VIEW
    Consume by Javascript 
    return JSON data
    """
    data ={}
    status=200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['id'] = obj.id
        data["content"] = obj.content  
    except:
        # raise Http404(f"TWEET WITH {tweet_id} ID NOT FOUND")
        data['message'] = "NOT FOUND" 
        status=404
    return JsonResponse(data, status=400)
    # return HttpResponse(f"<h1>{tweet_id} - {obj.content}</h1>")

