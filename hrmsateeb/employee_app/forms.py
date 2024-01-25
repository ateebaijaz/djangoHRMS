import io
from django import forms
from .models import AttandenceTable
import csv


class AttandenceForm(forms.Form):
    document = forms.FileField(
        label='Choose a file'
    )
    # def process(self):
    #     f = io.TextIOWrapper(self.cleaned_data['document'].file)
    #     r = csv.DictReader(f)
    #     for i in r:
    #         AttandenceTable.objects.create(employee=['user_id'],
    #         date=['date'],
    #         attendence=['attendence'])
    #         print(i)


