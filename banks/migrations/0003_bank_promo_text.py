from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_bank_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='promo_text',
            field=models.TextField(
                blank=True,
                default='',
                help_text='Повний текст акції — відображається на окремій сторінці банку',
                verbose_name='Текст акції',
            ),
        ),
    ]
