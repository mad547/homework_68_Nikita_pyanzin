function handleCalculate(event) {
    event.preventDefault();

    const url = this.dataset.url;
    const a = parseFloat(document.getElementById('numA').value);
    const b = parseFloat(document.getElementById('numB').value);
    const resultBox = document.getElementById('result');

    if (isNaN(a) || isNaN(b)) {
        resultBox.textContent = 'Введите оба числа!';
        resultBox.className = 'result-box error';
        return;
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({A: a, B: b})
    })
        .then(response => response.json())
        .then(data => {
            if (data.answer !== undefined) {
                resultBox.textContent = `Ответ: ${data.answer}`;
                resultBox.className = 'result-box success';
            } else {
                resultBox.textContent = `Ошибка: ${data.error}`;
                resultBox.className = 'result-box error';
            }
        })
        .catch(() => {
            resultBox.textContent = 'Ошибка соединения';
            resultBox.className = 'result-box error';
        });
}
document.querySelectorAll('.calc-btn').forEach(btn => {
    btn.addEventListener('click', handleCalculate);
});