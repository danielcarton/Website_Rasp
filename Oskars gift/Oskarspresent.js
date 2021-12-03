var selectElem = document.getElementById('pdfs');

selectElem.onchange = function() {
  window.location = selectElem[selectElem.selectedIndex].value;
};