

// const inputElement = document.getElementById('client_input');
// const hintList = document.querySelectorAll('.clients_hint_list.forInp[style="display: block;"]');
// const hintListContainer = document.querySelector('.clients_hint_list_all')
// const helptext = document.querySelector('.alert.alert-warning')
// const extraInfo = document.querySelector('.extra-info')
// let selectedIndex = -1;

// var isFirst = true
// const show_hints = (inp) => {
//     isFirst = true
//     var search_value = inp.value.trim().toLowerCase()
//     var all_hints = hintList
//     // var all_hints = hintList

//     hintListContainer.style.display = 'block'
//     if (search_value) {
//         all_hints.forEach(each => {
//             if (each.innerText.toLowerCase().search(search_value) == -1) {
//                 each.style.display = 'none'
//                 each.classList.remove('selected')
//                 console.log(0)
//                  helptext.style.display = 'block'
//                  extraInfo.style.display = 'flex'
//             }
//             else {
//                 each.style.display = 'block'


//             }
//             if (document.querySelector('.selected')) {
//                 document.querySelector('.selected').classList.remove('selected')
//             }
//             if (document.querySelectorAll('.clients_hint_list.forInp[style="display: block;"]')[0]) {
//                 document.querySelectorAll('.clients_hint_list.forInp[style="display: block;"]')[0].classList.add('selected')
//             }
//             selectedIndex = 0
//         })

//     }
//     else {
//         all_hints.forEach(each => {
//             each.style.display = 'block'
//         })
//         document.querySelectorAll('.selected').forEach(each => {
//             each.classList.remove('selected')
//         })
//         selectedIndex = -1
//          helptext.style.display = 'none'
//          extraInfo.style.display = 'none'

//     }

// }
// hintList.forEach(hint => {
//     hint.addEventListener('click', () => {
//         // alert()
//         document.querySelector('#client_input').value = hint.innerText
//        helptext.style.display = 'none'
//        extraInfo.style.display = 'none'
//         try {
//             document.querySelector('.selected').classList.remove('selected')
//         }
//         catch {

//         }
//         hint.classList.add('selected')
//         // alert()
//         hintListContainer.style.display = 'none'
//         hintList.forEach(hint => {
//             hint.style.display = 'none'

//         })

//     })

// })

// document.querySelector('.input_with_hints input').addEventListener('focus', () => {
//     hintListContainer.style.display = 'block'
// })


// inputElement.addEventListener('keydown', function (event) {
//     if (hintList.length === 0) {
//         return;
//     }

//     switch (event.key) {
//         case 'ArrowUp':
//             event.preventDefault();
//             moveSelection(-1);
//             break;
//         case 'ArrowDown':
//             event.preventDefault();
//             moveSelection(1);
//             break;
        
//         case 'Enter':
//             event.preventDefault();
//             selectHint(selectedIndex);
//         // alert()  
//     }
// });

// function moveSelection(step) {

//     const maxIndex = document.querySelectorAll('.clients_hint_list.forInp[style="display: block;"]').length;
//     selectedIndex = Math.max(-1, Math.min(maxIndex, selectedIndex + step));
//     hintList.forEach((hint, index) => {
//         hint.classList.remove('selected');
//     });

//     if (selectedIndex >= 0) {
//         if (selectedIndex == maxIndex) {
//             selectedIndex = 0
//         }


//     }
//     if (selectedIndex == -1) {
//         selectedIndex = maxIndex - 1
//     }
//     // inputEl  ement.value = document.querySelectorAll('.supplier_hint_list.forInp[style="display: block;"]')[selectedIndex].innerText
//     document.querySelectorAll('.clients_hint_list.forInp[style="display: block;"]')[selectedIndex].classList.add('selected');

//     document.querySelector('.input_with_hints input').value = document.querySelectorAll('.clients_hint_list.forInp[style="display: block;"]')[selectedIndex].innerHTML
// }

// function selectHint(index) {

//     inputElement.value = document.querySelector('.selected').textContent;
//    helptext.style.display = 'none'
//    extraInfo.style.display = 'none'
//     selectedIndex = -1;
//     document.querySelector('.clients_hint_list_all').style.display = 'none'
// }





// const length_slice = (el) => {
//     if (el.value.length >= 2) {
//         el.value = el.value.slice(0, 3);
//     }
// }



// window.addEventListener("click", function (event) {

//     if(!event.target.classList.contains('input_with_hints')){
//         hintListContainer.style.display = 'none'
//     }
//   });


//     IMask(
//         document.querySelector('.tel_number'),
//     {
//         mask: '+7(000)000-00-00'  ,
//       blocks: {
//         num: {
//           // nested masks are available!
//           mask: Number,
//           thousandsSeparator: '.'
//         }
//       }
//     }
//   )
document.addEventListener('DOMContentLoaded', () => {
    new SearchHints(
        '#client_input', 
        '.clients_hint_list.forInp',
        '.clients_hint_list_all',
        '.alert.alert-warning',
        '.extra-info',
        // '.create_debt_btn',
        null,
    );

    IMask(
        document.querySelector('.tel_number'),
        {
            mask: '+7(000)000-00-00',
            blocks: {
                num: {
                    mask: Number,
                    thousandsSeparator: '.'
                }
            }
        }
    );
});
