from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from customers.models import TenantUser


class TenantUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirmação de senha', widget=forms.PasswordInput)

    class Meta:
        model = TenantUser
        fields = ('email', 'client',)

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não são iguais.")
        return password2

    def save(self, commit=True):
        user = super(TenantUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class TenantUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label="Password",
                                         help_text="Não há nenhuma maneira de ver a senha do usuário, "
                                                   "mas você pode alterar a senha "
                                                   "usando <a href=\"../password/\">este formulário</a>.")

    class Meta:
        model = TenantUser
        fields = (
            'email', 'password', 'user_permissions', 'is_active', 'is_superuser'
        )

    def clean_password(self):
        return self.initial["password"]
