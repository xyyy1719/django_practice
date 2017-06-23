from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from books.models import Book, Publisher

# Create your views here.
def search(request):
    errors = []
    # 判断query里是否包含q
    if 'q' in request.GET:
        q = request.GET['q']
        # 没有输入直接点提交, 则q是空字符串
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:   
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    # errors为空时, 表示query中没有包含q, 意味着是初次打开/search/页面, 不用显示错误信息
    return render(request, 'search_form.html', {'errors': errors})

class PublisherList(ListView):
    model = Publisher
    context_object_name = 'my_favorite_publishers'
    template_name = 'publisher_list.html'

class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        context['book_list'] = Books.objects.all()
        return context


