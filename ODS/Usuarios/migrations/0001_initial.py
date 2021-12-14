# Generated by Django 3.2.9 on 2021-12-14 20:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_post', models.CharField(help_text='Maximo 20 caracteres por titulo de Post', max_length=20)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True, verbose_name='FECHA,HORA')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': "Post's",
                'db_table': 'Post',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(choices=[('1', 'FIN DE LA POBREZA'), ('2', 'HAMBRE CERO'), ('3', 'SALUD Y BIENESTAR'), ('4', 'EDUCADION DE CALIDAD'), ('5', 'IGUALDAD DE GENERO'), ('6', 'AGUA LIMPIA Y SANEAMIENTO'), ('7', 'ENERGIA'), ('8', 'CRECIMIENTO ECONOMICO'), ('9', 'AGUA'), ('10', 'REDUCCION DE DESIGUALDADES'), ('11', 'COMUNIDADES SOSTENIBLES'), ('12', 'PRODUCCION Y CONSUMO'), ('13', 'ACCION POR EL CLIMA'), ('14', 'VIDA SUBMARINA'), ('15', 'ECOSISTEMAS TERRESTRES'), ('16', 'PAZ, JUSTICIA'), ('17', 'ALIANZAS')], max_length=2)),
                ('id_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.post')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
            },
        ),
    ]
