from .models            import Post
from django             import forms




class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			'titulo_post',
			'contenido',
			'categoria',]
		labels = {
			'titulo_post': 'Titulo',
			'contenido': 'Contenido',
			'categoria': 'Categoria',
		}
		widgets = {
			'titulo_post': forms.TextInput(attrs={'class':'form_control'}),
			'contenido': forms.Textarea(attrs={'class':'form_control', 'rows':5, 'placeholder':'Ingrese contenido del  post.'}),
			'categoria': forms.Select(),
		}