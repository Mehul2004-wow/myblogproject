from django import forms
# Create your models here.
class contactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField(label="Email")
    subject = forms.CharField(required=False)
    comment = forms.CharField(max_length=1000)

class RegistrationForm(forms.Form):
    name = forms.CharField()
    user_name = forms.CharField(required=True)
    mobile_no = forms.IntegerField()
    password = forms.CharField()
    re_password = forms.CharField()

class Login(forms.Form):
    User_name = forms.CharField(label="User Name")
    Password = forms.CharField(widget=forms.PasswordInput)

class PostForm(forms.Form):
    id = forms.IntegerField(label="ID")
    title = forms.CharField(max_length=200, label="Title")
    slug = forms.SlugField(max_length=200, label="Slug")
    content = forms.CharField(widget=forms.Textarea(), label="Content")
    author = forms.CharField(max_length=100, label="Author")
    IS_PUBLISHED_CHOICES = [(True, 'Yes'), (False, 'No')]
    is_published = forms.ChoiceField(choices=IS_PUBLISHED_CHOICES,widget=forms.RadioSelect)

class CategoryForm(forms.Form):
    Id = forms.IntegerField()
    Name = forms.CharField()
    Description = forms.CharField()


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=5)
    feedback = forms.CharField(widget=forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters.")
        return name
    
    def clean(self):
        cleaned_data = super().clean()
        rating = cleaned_data.get("rating")
        feedback = cleaned_data.get("feedback")

        if rating and feedback:
            if rating < 3 and len(feedback) < 20:
                raise forms.ValidationError("Please provide detailed feedback.")