const labels = document.getElementsByTagName("label");

labels[0].textContent = "Текст ответа";
labels[1].textContent = "Выберите контакт";
labels[0].setAttribute("id", "label_1");



textarea[1].placeholder = "Введите текст ответа";



var select = document.querySelector("#id_contact");
var contacts = document.querySelectorAll("[id^='contact_']");

select.addEventListener("change", function(event) {
    var selected = event.target.value;

    for (var i = 0; i < contacts.length; i++) {
    if (contacts[i].getAttribute("id") === "contact_" + selected) {
        contacts[i].style.display = "block";
    } else {
        contacts[i].style.display = "none";
    }
}
});

