document.querySelector('.currency-mask').addEventListener('input', (e) => {
  document.querySelector('#id_cost').value = document.querySelector('.currency-mask').value.replace(/[^0-9]/g, "")

})

IMask(
  document.querySelector('.currency-mask'),
  {
    mask: '₸ num',
    blocks: {
      num: {
        // nested masks are available!
        mask: Number,
        thousandsSeparator: '.'
      }
    }
  }
)

var files
const inputCostMasked = document.querySelector('form .currency-mask');
let cost;
let isProblemCost = true;
inputCostMasked.addEventListener('input', (event) => {
    cost = +inputCostMasked.value.replaceAll('.', '').replaceAll('₸', '');
    if (cost >= 10 && cost < 1_000_000) {
        document.querySelector('.helptext').style.display = 'none';
        isProblemCost = false;
    } else {
        document.querySelector('.helptext').style.display = 'block';
        isProblemCost = true;
    }
});

document.querySelector('form button[type="submit"]').addEventListener('click', (event) => {
  // var userSupplierInput = document.querySelector('.supply_input').value;
  // var allSuppliers = document.querySelectorAll('.supplier_hint_list.forInp');
  // var allSupplierList = Array.from(allSuppliers).map(each => each.textContent);
  // if (allSupplierList.includes(userSupplierInput)) {
  //     document.querySelector('.helptext').style.display = 'none';
      cost = +inputCostMasked.value.replaceAll('.', '').replaceAll('₸', '');
      if (!(cost >= 10 && cost < 1_000_000)) {
          event.preventDefault();
          document.querySelector('.helptext').style.display = 'block';
          window.scrollTo(0, 0);
      } else {
          document.querySelector('form').submit();
      }
  
});


const previewImages = (el) => {
  files = el.files
  console.log(el.files)
  document.querySelector('.imagePreview').innerHTML = ''
  for (var i = 0; i < el.files.length; i++) {
    // console.log(file)
    document.querySelector('.imagePreview').innerHTML += `  <a href=${URL.createObjectURL(el.files[i])}><img id="blah" src=${URL.createObjectURL(el.files[i])} alt="your image" width="100"/></a>`

  }


}
const length_slice = (el) => {
  if (el.value.length >= 2) {
    el.value = el.value.slice(0, 3);
  }
}

