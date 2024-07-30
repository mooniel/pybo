from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from ..models import Question

def index(request):
    print("access index")
    page = request.GET.get('page', '1')  # 페이지
    question_list = Question.objects.order_by('-issued_date')
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    print(page_obj)
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def completed(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_completed.html', context)