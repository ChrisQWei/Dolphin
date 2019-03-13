from django import forms
from Register.models import user_info


class regist_form(forms.Form):
    id_card = forms.CharField(max_length=26)
    user_name = forms.CharField()
    phone_number = forms.IntegerField()
    def clean_titile(self):
        id_card = self.cleaned_data['id_card']
        if user_info.objects.filter(id_card=id_card).exists():
            raise forms.ValidationError('已存在相同身份证号')
        return id_card