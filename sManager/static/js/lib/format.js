
window.addEventListener('load', function () {
  
  document.querySelectorAll('.currency-text').forEach(each => {
    each.innerHTML =  Intl.NumberFormat('de-DE', { style: 'currency', currency: 'KZT', maximumSignificantDigits: 10 }).format(each.innerHTML)
})


document.querySelectorAll('.moneyInput').forEach(each => {
  each.addEventListener('input', function (event) {
    let value = this.value;
    
    // Удаляем все символы, кроме цифр, + и -
    value = value.replace(/[^0-9+-]/g, '');
    
    // Проверяем, есть ли несколько + или - или они находятся не в начале
    const match = value.match(/^([+-]?)(\d*)$/);

if (match) {
value = match[1] + match[2]; // Сохраняем только валидную часть строки
} else {
value = value.slice(0, -1);  // Убираем последний введенный символ
}
    // Ограничиваем длину строки до 10 символов
    if (value.length > 7) {
        value = value.slice(0, 7);
    }

    this.value = value;
});
})
})
function formatCurrency(value) {
  return Intl.NumberFormat('de-DE', { style: 'currency', currency: 'KZT', maximumSignificantDigits: 3 }).format(value);
}

window.formatCurrency = formatCurrency;

const check_length = (btn_class_or_id, el_value) => {
  document.querySelector(btn_class_or_id).disabled = ['+','-', ''].includes(el_value.replace(/\D/g, '')) || +el_value.replace(/\D/g, '') < 1
  
}