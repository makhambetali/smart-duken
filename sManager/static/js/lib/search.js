class SearchHints {
    constructor(inputSelector, hintListSelector, hintListContainerSelector, helpTextSelector, extraInfoSelector, submitButtonSelector) {
        this.inputSelector = inputSelector;
        this.hintListSelector = hintListSelector;
        this.hintListContainerSelector = hintListContainerSelector;
        this.helpTextSelector = helpTextSelector;
        this.extraInfoSelector = extraInfoSelector;
        this.submitButtonSelector = submitButtonSelector;

        this.inputElement = document.querySelector(inputSelector);
        this.hintList = document.querySelectorAll(hintListSelector);
        this.hintListContainer = document.querySelector(hintListContainerSelector);
        this.helpText = document.querySelector(helpTextSelector);
        this.extraInfo = document.querySelector(extraInfoSelector);
        this.submitButton = document.querySelector(submitButtonSelector);
        this.selectedIndex = -1;

        this.init();
    }

    init() {
        this.inputElement.addEventListener('input', () => this.showHints());
        this.inputElement.addEventListener('keydown', (event) => this.handleKeyDown(event));
        this.inputElement.addEventListener('focus', () => this.hintListContainer.style.display = 'block');
        this.hintList.forEach(hint => {
            hint.addEventListener('click', () => this.selectHint(hint));
        });
        window.addEventListener('click', (event) => {
            if (!event.target.closest(this.inputSelector)) {
                this.hintListContainer.style.display = 'none';
            }
        });
        this.name_array = []
        this.hintList.forEach(each => {
            this.name_array.push(each.innerText.trim().toLowerCase())
        })
        this.name_obj = {
            true:'block',
            false: 'none'
        }
        console.log(this.name_array)
    }

    showHints() {
        const searchValue = this.inputElement.value.trim().toLowerCase();
        let hasMatch = false;
        this.hintList.forEach(each => {
            if (each.innerText.toLowerCase().includes(searchValue)) {
                each.style.display = 'block';
                hasMatch = true;
            } else {
                each.style.display = 'none';
            }
            each.classList.remove('selected');
        });
       
        if(this.submitButton){
            this.submitButton.disabled = !this.name_array.includes(searchValue)
        }
        this.helpText.style.display = this.name_obj[!this.name_array.includes(searchValue)]
        if (searchValue && !hasMatch) {
           
            if (this.extraInfo) this.extraInfo.style.display = 'flex';
        } else {
            if (this.extraInfo) this.extraInfo.style.display = 'none';
        }
        this.hintListContainer.style.display = 'block';
        const visibleHints = this.hintListContainer.querySelectorAll(this.hintListSelector + '[style="display: block;"]');
        if (visibleHints.length > 0) {
            visibleHints[0].classList.add('selected');
            this.selectedIndex = 0;
        } else {
            this.selectedIndex = -1;
        }
        
    }

    handleKeyDown(event) {
        if (this.hintList.length === 0) {
            return;
        }
        switch (event.key) {
            case 'ArrowUp':
                event.preventDefault();
                this.moveSelection(-1);
                break;
            case 'ArrowDown':
                event.preventDefault();
                this.moveSelection(1);
                break;
            case 'Enter':
                event.preventDefault();
                this.selectHint(this.hintListContainer.querySelector('.selected'));
                break;
        }
    }

    moveSelection(step) {
        const visibleHints = this.hintListContainer.querySelectorAll(this.hintListSelector + '[style="display: block;"]');
        const maxIndex = visibleHints.length - 1;
        if (visibleHints.length === 0) return;

        this.selectedIndex = Math.max(0, Math.min(maxIndex, this.selectedIndex + step));
        visibleHints.forEach(hint => hint.classList.remove('selected'));
        visibleHints[this.selectedIndex].classList.add('selected');
        this.inputElement.value = visibleHints[this.selectedIndex].innerText;
    }

    selectHint(hint) {
        if (hint) {
            this.inputElement.value = hint.innerText;
            this.helpText.style.display = 'none';
            if (this.extraInfo) this.extraInfo.style.display = 'none';
            this.selectedIndex = -1;
            this.hintListContainer.style.display = 'none';
            if(this.submitButton)
            {
                this.submitButton.disabled = false; // Enable the submit button when a hint is selected
            }
        }
    }
}
