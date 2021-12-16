from django import forms

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['__all__']
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
