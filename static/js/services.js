function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab-btn");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  

// Получаем все кнопки вкладок и все таблицы
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

// Добавляем обработчик события для каждой кнопки
tabBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    // Получаем значение data-set для текущей кнопки
    const set = btn.getAttribute('data-set');
    
    // Скрываем все таблицы
    tabContents.forEach(tab => {
      tab.classList.remove('active');
    });
    
    // Показываем только ту таблицу, у которой значение data-set соответствует выбранному значению set_services
    const selectedTab = document.getElementById(`tab-${set}`);
    selectedTab.classList.add('active');
  });
});
