from django import forms
from django.contrib.auth.models import User
from .models import Blog,ContactUs

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude =['author']

    def __init__(self, *args, **kwargs):
            super(BlogForm, self).__init__(*args, **kwargs)

            self.fields['title'].widget.attrs['class'] = 'form-control'
            self.fields['title'].widget.attrs['placeholder'] = 'Title'
            self.fields['title'].label = ''

            self.fields['image'].widget.attrs['class'] = 'form-control'
            self.fields['image'].widget.attrs['placeholder'] = ''
            self.fields['image'].label = 'Image'

            self.fields['content'].widget.attrs['class'] = 'form-control'
            self.fields['content'].widget.attrs['placeholder'] = 'Content'
            self.fields['content'].label = ''

            self.fields['tags'].widget.attrs['class'] = 'form-control'
            self.fields['tags'].widget.attrs['placeholder'] = 'Tags'
            self.fields['tags'].label = ''
            self.fields['tags'].help_text = '<span class="form-text text-muted"><small> Separate between tags by comma (,) </small></span>'

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude =['user']

    def __init__(self, *args, **kwargs):
            super(ContactForm, self).__init__(*args, **kwargs)
            self.fields['message'].widget.attrs['class'] = 'form-control'
            self.fields['message'].widget.attrs['placeholder'] = 'Message'
            self.fields['message'].label = ''
            self.fields['subject'].widget.attrs['class'] = 'form-control'
            self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
            self.fields['subject'].label = ''


         


