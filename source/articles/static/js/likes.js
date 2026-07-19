function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener('DOMContentLoaded', () => {
    const likeButtons = document.querySelectorAll('.like-btn');

    likeButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const url = btn.dataset.url;
            const countSpan = btn.querySelector('.likes-count');
            const icon = btn.querySelector('.like-icon');

            fetch(url, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': getCookie('csrftoken'),
                }
            })
            .then(response => response.json())
            .then(data => {
                countSpan.textContent = data.likes_count;
                if (data.liked) {
                    icon.textContent = '♥';
                    icon.style.color = '#dc3545';
                } else {
                    icon.textContent = '♡';
                    icon.style.color = '';
                }
            });
        });
    });
});