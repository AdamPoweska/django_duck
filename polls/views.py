# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Question
from .forms import ducks_form, ducks_rating, user_description


def home_view(request):
    form = ducks_form()
    context = {
        'form_duck': form,
    }
    return render(request, "detail.html", context)

def home_rating(request):
    form = ducks_rating()
    context = {
        'form_rating': form,
    }
    return render(request, "detail.html", context)

def text_input_view(request):
    if request.method == 'POST':
        form = user_description(request.POST)
        user_text = form.cleaned_data['user_input']
        return render(request, 'results.html', {'form': form, 'user_text': user_text})
    else:
        form = user_description()
        return render(request, 'result.html', {'form': form, 'user_text': ''})
    

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Dodawanie formularzy do kontekstu:
        context['form_duck'] = ducks_form()
        context['form_rating'] = ducks_rating()
        context['from_input'] = user_description()
        return context


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, 'polls/index.html', context)


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions(not including those set to be published in the future)."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


def results(request, pk):
    question = get_object_or_404(Question, pk=pk)
    
    if request.method == 'POST':
        # Pobieranie danych z formularzy
        duck_description = request.POST.get('user_input', '')  
        duck_choice = request.POST.get('ducks_field', '')  
        duck_rating = request.POST.get('ducks_rating', '')  
        
        # Aktualizacja danych w bazie
        if duck_description:
            if question.duck_descriptions:
                question.duck_descriptions += f"\n{duck_description}"
            else:
                question.duck_descriptions = duck_description

        if duck_choice:
            if question.favourite_ducks:
                question.favourite_ducks += f"\n{duck_choice}"
            else:
                question.favourite_ducks = duck_choice

        if duck_rating:
            if question.duck_ratings:
                question.duck_ratings += f"\n{duck_rating}"
            else:
                question.duck_ratings = duck_rating

        question.save()

        # Przekazanie danych do szablonu
        return render(request, 'polls/results.html', {
            'question': question,
            'duck_description': duck_description,
            'duck_choice': duck_choice,
            'duck_rating': duck_rating,
        })

    return render(request, 'polls/results.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        question = self.get_object()
        context['results_text'] = "Wyniki głosowania: {}".format(question.results_text)
        return context
