from django import forms


class MultipleListForm(forms.Form):
    lists_num = forms.IntegerField(max_value=100, required=False)
    file = forms.FileField(allow_empty_file=True, required=False)


class ConcreteListForm(forms.Form):
    elements = forms.CharField(label='Elements', widget=forms.Textarea, required=False)
    file = forms.FileField(allow_empty_file=True, required=False)
