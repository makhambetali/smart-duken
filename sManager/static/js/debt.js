
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
