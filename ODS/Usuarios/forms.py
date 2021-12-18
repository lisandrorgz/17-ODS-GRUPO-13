from django import forms
from .models import Post, Usuario

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'author',
			'titulo_post',
			'contenido',
			'categoria',]
		labels = {
			'author': 'Nombre de Usuario',
			'titulo_post': 'Titulo',
			'contenido': 'Contenido',
			'categoria': 'Categoria',
		}
		widgets = {
			'author': forms.TextInput(attrs={'class':'form_control'}),
			'titulo_post': forms.TextInput(attrs={'class':'form_control'}),
			'contenido': forms.TextInput(attrs={'class':'form_control'}),
			'categoria': forms.CheckboxSelectMultiple(),
		}

class UsuarioForm(forms.ModelForm):

	class Meta:
		model = Usuario
		fields = ['first_name', 'last_name', 'email','username', 'password']
		# labels = {'author': 'Nombre de Usuario', 'titulo_post': 'Titulo','contenido': 'Contenido', 'categoria': 'Categoria'}
		# widgets = {'author': forms.TextInput(attrs={'class':'form_control'}),'titulo_post': forms.TextInput(attrs={'class':'form_control'}), 'contenido': forms.TextInput(attrs={'class':'form_control'}),'categoria': forms.CheckboxSelectMultiple()}
