document.addEventListener('DOMContentLoaded', () => {
    const likeButtons = document.querySelectorAll('.like-btn');

    likeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const url = btn.dataset.url;
            const countSpan = btn.querySelector('.likes-count');

            fetch(url, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                }
            })
            .then(response => response.json())
            .then(data => {
                countSpan.textContent = data.likes_count;
                if (data.liked) {
                    btn.classList.remove('btn-outline-danger');
                    btn.classList.add('btn-danger');
                }else {
                    btn.classList.remove('btn-danger');
                    btn.classList.add('btn-outline-danger');
                }
            });
        });
    });
});