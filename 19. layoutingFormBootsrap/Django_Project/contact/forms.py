from django import forms
from django.forms.fields import EmailField

# create your views here


class ContactForm(forms.Form):

    # mengambil attrs di bottstrap form
    nama_lengkap  = forms.CharField(
        label = 'Nama Lengkap',
        max_length= 20,
        widget= forms.TimeInput(
            # attrs ini adalah atribute yang berisi dictionary
            attrs={
                'class':'form-control',
                'placeholder':'masukan nama lengkap anda',
            }
        )
    )
    jenis_kelamin = forms.ChoiceField(
        widget = forms.RadioSelect(
            attrs={
                'class':'form-check-input',
            }
        ),
        choices = [
            ('P','pria'),
            ('W','wanita'),
        ]
    )
    tanggal_lahir = forms.DateField(
        widget = forms.SelectDateWidget(
                    attrs = {
                        'class':'form-control col-sm-2',
                    },
                     years=range(1945,2020,1),
                 )
    )
    Email   = forms.EmailField(
        widget = forms.TimeInput(
            attrs= {
                'class':'form-control',
                'placeholder':'isi dengan email anda',
            }
        )
    )
    alamat  = forms.CharField(
        widget=forms.Textarea(
            attrs = {
                'class':'form-control',
                'placeholder':'isi alamat lengkap',
            }
        )
        
        )
    agree   = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                'class':'form-check-input',
            }
        )

    )