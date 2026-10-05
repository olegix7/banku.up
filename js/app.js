// Touch feedback при кліку на картку (мобільні пристрої)
document.querySelectorAll('.bank-card').forEach(card => {
  card.addEventListener('click', () => {
    card.style.transform = 'scale(0.97)';
    setTimeout(() => { card.style.transform = ''; }, 150);
  });
});
