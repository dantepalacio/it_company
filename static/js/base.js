let modal = document.getElementById("request_form");
let html = document.getElementsByTagName("html")[0];
let btn = document.getElementById("request_btn");
let close = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
    html.style.overflow = "hidden";
    html.style.marginRight = 17 + "px";
}

close.onclick = function() {
    modal.style.display = "none";
    html.style.overflow = "auto";
    html.style.marginRight = "";
}

window.onclick = function(e) {
    if (e.target == modal) {
        modal.style.display = "none";
        html.style.overflow = "auto";
        html.style.marginRight = "";
    }
}


document.addEventListener("DOMContentLoaded", function (event) {
    // Найти элемент с сообщением
    let message = document.getElementById("message_success");
    if (message) {
      // Скрыть сообщение через 5 секунд
      setTimeout(function () {
        message.style.display = "none";
      }, 5000);
    }
  });


let input = document.getElementsByTagName("input");
let textarea = document.getElementsByTagName("textarea");
console.log(textarea);
input[1].placeholder = "Атын енгізіңіз";
input[2].placeholder = "Тегі енгізіңіз";
input[3].placeholder = "Поштаны енгізіңіз";
textarea[0].placeholder = "Хабарламаңызды енгізіңіз"