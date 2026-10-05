from django.shortcuts import render, get_object_or_404
from .models import Bank


def index(request):
    banks = Bank.objects.filter(is_active=True)
    return render(request, 'banks/index.html', {'banks': banks})


def bank_detail(request, pk):
    bank = get_object_or_404(Bank, pk=pk, is_active=True)
    # Розбиваємо promo_text на абзаци по \n для зручного відображення
    promo_paragraphs = [p.strip() for p in bank.promo_text.split('\n') if p.strip()]
    return render(request, 'banks/detail.html', {
        'bank': bank,
        'promo_paragraphs': promo_paragraphs,
    })
