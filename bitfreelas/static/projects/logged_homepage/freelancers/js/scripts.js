document.querySelector('input[type="search"]').addEventListener('input', function (event) {
    let filter = event.target.value.toLowerCase();
    let cards = document.querySelectorAll('.card');

    cards.forEach(function (card) {
        let cardTitle = card.querySelector('.card-title').textContent.toLowerCase();

        if (cardTitle.indexOf(filter) > -1) {
            card.style.display = '';
        } else {
            card.style.display = 'none';
        }
    });
});
