from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='description',
            field=models.CharField(
                blank=True,
                default='',
                help_text='1–2 речення про банк',
                max_length=120,
                verbose_name='Короткий опис',
            ),
        ),
    ]
