from django import forms
from blog.models import Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  def __init__(self, *args, **kwargs): # Define the constructor
    super(CommentForm, self).__init__(*args, **kwargs) # Call the constructor of the parent class
    self.helper = FormHelper() # Instantiate self.helper as an instance of the FormHelper class
    self.helper.add_input(Submit('submit', 'Submit')) # Instantiate an instance of the Submit class and add the submit button to the input of the form

