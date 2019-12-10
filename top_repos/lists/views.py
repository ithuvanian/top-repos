from django.shortcuts import render

import requests
import datetime

from .models import Languages, RepoSummary

# Create your views here.


def index(request, lang):
    url = 'https://api.github.com/search/repositories?q=language:' + \
        lang + '&sort=stars'
    r = requests.get(url)
    response = r.json()
    repos = response['items']

    summaries = []
    for repo in repos:
        summary = RepoSummary()
        summary.name = str(repo['name'])
        summary.url = str(repo['svn_url'])
        summary.stars = str(repo['stargazers_count'])
        summary.description = str(repo['description'])
        summaries.append(summary)

    langname = str(lang)
    if langname == 'css':
        langname = langname.upper()
    else:
        langname = langname.title()

    context = {
        'language': langname,
        'imgpath': Languages.list[lang],
        'summaries': summaries,
        'now': datetime.datetime.now()
    }
    return render(request, 'lists/index.html', context)
