var boolValue = true

const togglePassword = () => {
  if (boolValue) {
    document.querySelector('.passwordBlock').innerHTML = `  <div class="mb-3">
        <label for="new_pass" class="form-label">Новый пароль</label>
        <div class="input-group">
          <input type="password" name="new_password" id="new_pass" class="form-control" required>
          <button type="button" class="bi bi-eye" id="toggle_new_pass">
          
          </button>
        </div>
      </div>
      <div class="mb-3">
      <label for="old_pass" class="form-label">Старый пароль</label>
      <div class="input-group">
        <input type="password" name="current_password" id="old_pass" class="form-control" required>
        <button type="button" class="bi bi-eye" id="toggle_old_pass">
    
        </button>
      </div>
    </div>`
    document.getElementById('toggle_new_pass').addEventListener('click', function () {
      togglePasswordVisibility('new_pass', 'toggle_new_pass');
    });

    document.getElementById('toggle_old_pass').addEventListener('click', function () {
      togglePasswordVisibility('old_pass', 'toggle_old_pass');
    });

    function togglePasswordVisibility(inputId, iconId) {
      var input = document.getElementById(inputId);
      var icon = document.getElementById(iconId);
      if (input.type === "password") {
        input.type = "text";
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
      } else {
        input.type = "password";
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
      }
    }
    boolValue = false
  }
  else {
    document.querySelector('.passwordBlock').innerHTML = ''
    boolValue = true
  }

}
function resetForm() {
  document.getElementById("profile_update").reset();
  window.location.reload()
}
var updateUserBool = false
var updateBtn = document.querySelector('.other_details .updateBtn')
const updateUserData = () => {
  document.querySelector('.custom-modal').style.display = 'flex'

}

const openSessionModal = () => {
  document.querySelector('.custom-modal-profile').style.display = 'flex'
}

const cancelForm = () => {
  document.querySelector('.custom-modal-profile').style.display = 'none'
}


window.addEventListener("click", function (event) {
  if (event.target === document.querySelector('.custom-modal')) {
    document.querySelector('.custom-modal').style.display = "none";
  }
});
const previewImage = (el) => {
  document.querySelector('.img_part img').src = URL.createObjectURL(el.files[0])
  document.querySelector('.form_image').submit()
  // URL.createObjectURL(el.files[i])

}
document.querySelector('.img_part img').addEventListener('click', function () {
  document.getElementById('id_image').click();
});


document.querySelector('.img_part img').addEventListener('contextmenu', function (event) {
  event.preventDefault();
  showContextMenu(event.clientX, event.clientY);
});

function showContextMenu(x, y) {
  var contextMenu = document.getElementById('context_menu');
  contextMenu.style.display = 'block';
  contextMenu.style.left = x + 'px';
  contextMenu.style.top = y + 'px';
}

function hideContextMenu() {
  var contextMenu = document.getElementById('context_menu');
  contextMenu.style.display = 'none';
}

document.getElementById('delete_option').addEventListener('click', function () {
  // Добавьте код для удаления фото, например, отправка AJAX-запроса на сервер
  hideContextMenu();
});

document.addEventListener('click', function (event) {
  if (event.button !== 2) {  // Проверяем, что клик был левой кнопкой мыши
    hideContextMenu();
  }
});
