from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label = "User Name : ",initial="Nasim", help_text="please use your name")
    email = forms.EmailField(label= "Email")
    age = forms.IntegerField()
    balance = forms.DecimalField()
    weight = forms.FloatField()
    birth = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))
    check = forms.BooleanField()
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type' : 'datetime-local'}))
    CHOICES = [('S', 'Small'),('M','Medium'),('L', 'Large')]
    T_shirt = forms.ChoiceField(choices=CHOICES,label="T-Shirt Size :", widget=forms.RadioSelect)
    MEAL = [('B', 'Beef'), ('M','Mutton'),('C','chicken')]
    Menu = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)
    file = forms.FileField()
    img = forms.ImageField()

    
class studentCheck(forms.Form):
     
     def money(val):
          if val >= 200:
            raise forms.ValidationError("YEah Baby")
          
     Name = forms.CharField(
        label="Enter your name:",
        initial="mofiz",
        validators=[validators.MaxLengthValidator(10, message="Enter a valid name !")]
    )
     Email = forms.CharField(label="Enter your Email: ", 
                             validators=[validators.EmailValidator(message="enter a valid email")])
     Age =forms.IntegerField(validators=[validators.MaxValueValidator(20,message="Enter a age limit lower than 20")])
     Money = forms.IntegerField(validators=[money])

    
    # custom check 
    # def clean(self):
    #     cleaned_data = super().clean
    #     valname = self.cleaned_data['Name']
    #     valemail = self.cleaned_data['Email']

    #     if len(valname) < 10:
    #         raise forms.ValidationError('Name must be at least 10 characters')
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('You Email is not valid !!')