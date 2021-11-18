from django.shortcuts import render


def get_topics(request):
    """ A view to return the main forum page """
    return render(request, 'forum/forum.html')