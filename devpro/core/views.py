import json

from django.http import JsonResponse
from django.core.paginator import Paginator

from devpro.core.models import Author

DEFALT_PAGE_SIZE = 25


def authors(request):
    page_number = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', DEFALT_PAGE_SIZE)
    q = request.GET.get('q')

    queryset = Author.objects.all()
    if q:
        queryset = queryset.filter(name__icontains=q)
    paginator = Paginator(queryset, per_page=page_size)
    page = paginator.get_page(page_number)

    # return HttpResponse(json.dumps(authors), content_type='application/json')
    return JsonResponse({
        'data': [a.to_dict() for a in page.object_list],
        'count': paginator.count,
        'current_page': page_number,
        'num_pages': paginator.num_pages
    })
