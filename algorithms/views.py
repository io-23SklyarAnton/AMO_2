from django.shortcuts import render
from django.views.generic import FormView
from .forms import MultipleListForm, ConcreteListForm
from .services.algorithm_services import generate_lists_and_sort, get_sort_list_and_time


def home_view(request):
    return render(request, 'home.html', {'selector_id': 0})


class MultipleListsView(FormView):
    template_name = 'algorithms/multiple_algorithms_sort.html'
    form_class = MultipleListForm
    success_url = '#'

    def form_valid(self, form):
        sorted_lists = generate_lists_and_sort(form)
        self.request.session['sorted_lists'] = sorted_lists
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sorted_lists = self.request.session.get('sorted_lists')
        context['selector_id'] = 1
        context['sorted_lists'] = sorted_lists
        return context


class ConcreteListView(FormView):
    template_name = 'algorithms/concrete_list_sort.html'
    form_class = ConcreteListForm
    success_url = '#'

    def form_valid(self, form):
        sorted_list, execution_time = get_sort_list_and_time(form)
        self.request.session['sorted_list'] = sorted_list
        self.request.session['execution_time'] = execution_time
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sorted_list = self.request.session.get('sorted_list')
        execution_time = self.request.session.get('execution_time')
        context['selector_id'] = 2
        context['sorted_list'] = sorted_list
        context['execution_time'] = execution_time
        return context
