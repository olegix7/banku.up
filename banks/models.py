from django.db import models


class Bank(models.Model):
    name = models.CharField('Назва банку', max_length=100)
    url = models.URLField('Посилання', max_length=300)
    description = models.CharField(
        'Короткий опис',
        max_length=120,
        blank=True,
        default='',
        help_text='1–2 речення про банк'
    )
    promo_text = models.TextField(
        'Текст акції',
        blank=True,
        default='',
        help_text='Повний текст акції — відображається на окремій сторінці банку'
    )
    icon = models.CharField(
        'Іконка (emoji або CSS-клас)',
        max_length=10,
        default='🏦',
        help_text='Вставте emoji, наприклад 🟢 або 🖤'
    )
    order = models.PositiveSmallIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активний', default=True)

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    @property
    def display_url(self):
        """Повертає домен без протоколу для відображення."""
        url = self.url.replace('https://', '').replace('http://', '')
        return url.rstrip('/')
