# Generated by Django 2.2.6 on 2019-10-06 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_client_ultimo_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='ID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='clients'),
        ),
        migrations.AddField(
            model_name='client',
            name='doc_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ID'),
        ),
    ]
