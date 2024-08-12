const show_date_group = (arg) => {
  var element = document.querySelector(`.${arg}`)
  element.classList.toggle('show_group')
}
const calcButtonAll = document.querySelectorAll('#openModalButton');
const calcOptionsModal = document.getElementById('customModal');
const openCalcOptionsModal  = () => {
  calcOptionsModal.style.display = 'flex';
}

const closeCalcOptionsModal  = () => {
  calcOptionsModal.style.display = 'none';
}

calcButtonAll.forEach(each => {
  each.addEventListener('click', () => {
    openCalcOptionsModal()
    date = each.getAttribute('date')

    document.querySelectorAll('.custom-option')[1].disabled = (each.getAttribute('today') != each.getAttribute('date_f'))

  });
})
const getCalculations = (confirmed, date) => {
  return fetch(`/total_sum/confirmed=${confirmed}/date=${date}/extra=0`)
    .then(response => response.json())
    .then(data => {
      var dataFormatted
      if (confirmed) {
        dataFormatted = `Total: ${data['total']}; Банковский счёт: ${data['transfer']}; Cash: ${data['cash']}`
      }
      else {
        dataFormatted = `Total: ${data['total']}`
      }
      // console.log(data)
      alert(dataFormatted)
      return data
    });
}


async function asyncGetCalculations(confirmed, date) {
  try {

    await getCalculations(confirmed, date);

    closeCalcOptionsModal()
  } catch (error) {
    console.error('Произошла ошибка:', error);

    closeCalcOptionsModal()
  }
}
window.addEventListener("click", function (event) {
  if (event.target === calcOptionsModal) {
    calcOptionsModal.style.display = "none";
  }
});
document.querySelectorAll('.custom-option').forEach((each, num) => {
  each.addEventListener('click', () => {
  
    asyncGetCalculations(num,date)
  })

})
const redirectTo = (id) => {
  window.location.href = `supply/edit/${id}`
}