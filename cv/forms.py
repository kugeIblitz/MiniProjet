from django import forms
from django.forms import ModelForm
from cv.models import Skills, Portfolio,Experience



# Experience form
class ExperienceForm(ModelForm):
	class Meta:
		model = Experience
		fields = ('exp_name', 'description')
		labels = {
			'exp_name': '',
			'description': '',
					
		}
		widgets = {
			'exp_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Experience Name'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'description'}),
			
		}

# Skills form
class SkillsForm(ModelForm):
	class Meta:
		model = Skills
		fields = ('category', 'skill_name')
		labels = {
			'category': '',
			'skill_name': '',
					
		}
		widgets = {
			'category': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Skill category'}),
			'skill_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'skill name'}),
			
		}
# Certificate form
class CertificateForm(forms.ModelForm):
	
	
	class Meta:
		model = Portfolio
		fields = ('image', 'link','number')
		
			
		
