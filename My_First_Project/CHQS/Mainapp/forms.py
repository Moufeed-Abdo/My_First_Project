from django import forms
from .models import Student, Memo
#-----------------------------------
class StudentForm(forms.ModelForm):

    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    address = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta():
        model = Student
        fields = ('name', 'age', 'address', 'email')
        # exclude = ('user.username', 'user.firstname', 'user.surname')
#-----------------------------------

class MemoForm(forms.ModelForm):

    # mem_stu_name = forms.CharField(max_length=50)
    mem_sora = forms.CharField(max_length=50)
    mem_from = forms.IntegerField()
    mem_to = forms.IntegerField()
    mem_date = forms.DateField()
    mem_quant = forms.IntegerField()
    mem_rmrk = forms.CharField(max_length=20)
    mem_finished = forms.CharField(max_length=50)

    class Meta():
        model = Memo
        fields = ('mem_stu_name','mem_sora', 'mem_from', 'mem_to', 'mem_date','mem_quant','mem_rmrk','mem_finished')
