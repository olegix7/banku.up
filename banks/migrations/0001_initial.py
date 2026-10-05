from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва банку')),
                ('url', models.URLField(max_length=300, verbose_name='Посилання')),
                ('icon', models.CharField(
                    default='🏦',
                    help_text='Вставте emoji, наприклад 🟢 або 🖤',
                    max_length=10,
                    verbose_name='Іконка (emoji або CSS-клас)'
                )),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активний')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
                'ordering': ['order', 'name'],
            },
        ),
    ]
