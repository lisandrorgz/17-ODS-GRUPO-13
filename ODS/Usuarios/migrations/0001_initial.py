# Generated by Django 3.2.9 on 2021-12-12 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(help_text='Maximo de caracteres permitidos (13)', max_length=30)),
                ('correo', models.CharField(default='EMAIL', max_length=150)),
                ('contraseña', models.CharField(max_length=150)),
                ('rol', models.CharField(blank=True, choices=[('A', 'ADMIN'), ('E', 'ESCRITOR')], max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('titulo_post', models.CharField(help_text='Maximo 20 caracteres por titulo de Post', max_length=20)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True, verbose_name='FECHA,HORA')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario')),
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