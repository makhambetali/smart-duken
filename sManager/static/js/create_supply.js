document.addEventListener('DOMContentLoaded', () => {
    new SearchHints(
        '#supply_input', 
        '.supplier_hint_list.forInp',
        '.supplier_hint_list_all',
        '.helptext',
        null,
        '.create_supply_btn',
    );

    IMask(
        document.querySelector('.currency-mask'),
        {
            mask: '₸ num',
            blocks: {
                num: {
                    mask: Number,
                    thousandsSeparator: '.'
                }
            }
        }
    );
    
    var date = new Date();
    date.setDate(date.getDate() + 1);
    var nextDate = date.toISOString().substring(0, 10);
    document.querySelector('#id_date').value = nextDate;

    const inputCostMasked = document.querySelector('form .currency-mask');
    let cost;
    let isProblemCost = true;
    inputCostMasked.addEventListener('input', (event) => {
        cost = +inputCostMasked.value.replaceAll('.', '').replaceAll('₸', '');
        if (cost >= 10 && cost < 1_000_000) {
            document.querySelectorAll('.helptext')[1].style.display = 'none';
            isProblemCost = false;
        } else {
            document.querySelectorAll('.helptext')[1].style.display = 'block';
            isProblemCost = true;
        }
    });

    inputCostMasked.addEventListener('keydown', function (event) {
        if (event.key === '.' || event.key === ',' || event.key === '-') {
            event.preventDefault();
        }
    });

    document.querySelector('form button[type="submit"]').addEventListener('click', (event) => {
        var userSupplierInput = document.querySelector('.supply_input').value;
        var allSuppliers = document.querySelectorAll('.supplier_hint_list.forInp');
        var allSupplierList = Array.from(allSuppliers).map(each => each.textContent);
        if (allSupplierList.includes(userSupplierInput)) {
            document.querySelector('.helptext').style.display = 'none';
            if (isProblemCost) {
                event.preventDefault();
                window.scrollTo(0, 0);
            } else {
                document.querySelector('form').submit();
            }
        } else {
            event.preventDefault();
            document.querySelector('.helptext').style.display = 'block';
            // hintListContainer.style.display = 'block';
            window.scrollTo(0, 0);
        }
    });
});

const length_slice = (el) => {
    if (el.value.length >= 2) {
      el.value = el.value.slice(0, 3);
    }
  }
  