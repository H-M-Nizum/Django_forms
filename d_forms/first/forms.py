from django import forms
from django.forms.widgets import NumberInput
import datetime

class PracticeForm(forms.Form):
    # CharField()
    name = forms.CharField()
    
    # CharField() with Textarea widget
    # multi-line input field to your form
    Message = forms.CharField(widget=forms.Textarea)
    
    
    # CharField() with Textarea widget attribute
    # default number of rows is 10
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    
    # EmailField() - default widget of EmailInput 
    # This field also uses the built-in Django validation EmailValidator that requires an @ symbol within the input for it to be considered valid.
    email = forms.EmailField()
    
    # BooleanField() - unclicked checkbox
    # Boolean data type of either True or False. The default is False
    Agree = forms.BooleanField()
    
    
    # DateField() - only accepts date formatted values such as 2020-07-30
    # The default widget is DateInput but it renders just like a CharField
    Birthday = forms.DateField()
    
    # DateField() with NumberInput widget attribute
    # If you are looking to add a calendar, import NumberInput at the top of the file then add the NumberInput widget with the attribute 'type' : 'date'.
    birth_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    # same as work
    Birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # DateField() with SelectDateWidget widget
    # SelectDateWidget which displays three drop-down menus for month, date, and year.
    CHOICES = ['1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001']
    birth = forms.DateField(widget=forms.SelectDateWidget(years=CHOICES))
    
    
    # DecimalField() - number value inputs
    value = forms.DecimalField()
    
    
    ###############################################
    ################### core Arguments ############
    ###############################################
    
    # 1. required (Boolean) - By default it's True . 
    # The required argument determines if the fields are required for form submission. It is a boolean (True or False only) and creates the asterisk mark next to the field.
    for_not_required = forms.CharField(required=False)
    
    # 2. max_length and min_length
    Max_length = forms.CharField(max_length=10)
    Min_length = forms.CharField(min_length=6)
    
    # 3. label (String)
    label = forms.CharField(label='New Custom Label Arguments uses')
    
    # 4. initial (String) for CharField()
    first_name = forms.CharField(initial='Rahim')
    
    # 5. initial (Boolean) for BooleanField()
    check = forms.BooleanField(initial=True)
    
    # 6. initial (Datetime) for DateField()
    # Import datetime at the top of the file. Then you can set the initial input as the current date by using the import datetime
    day = forms.DateField(initial=datetime.date.today)
    
    
    
    ####################################################
    ### ChoiceField, MultipleChoiceField, ModelChoiceField, and ModelMultipleChoiceField#######
    #####################################################
    
    LANGUAGE = [('p', 'Python'), ('c', 'C'), ('j', 'Java'), ('js', 'Javascript')]
    
    # 1. ChoiceField() and RadioSelect 
    choice_one = forms.ChoiceField(choices=LANGUAGE)
    
    choice_one_with_RadioSelect = forms.ChoiceField(widget=forms.RadioSelect, choices=LANGUAGE)
    
    
    # 2. MultipleChoiceField() and  CheckboxSelectMultiple
    choice_multiple = forms.MultipleChoiceField(choices=LANGUAGE)
    
    choice_multiple_with_CheckboxSelectMultiple = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=LANGUAGE)
     
     
   