function del_escape () {
  x = document.getElementById('delShutter');
  x.parentNode.removeChild(x);

  x = document.getElementById('delInfo');
  x.parentNode.removeChild(x);
}

// http://www.quirksmode.org/js/selected.html
function getSel()
{
  if (window.getSelection)
	return window.getSelection();

  else if (document.getSelection)
  return document.getSelection();

  else if (document.selection)
  return document.selection.createRange().text;

  else return "";
}

function show_delicious () {
  del_icious = document.createElement('div');
  del_icious.setAttribute('id', 'delInfo');

  oTitle = document.createElement('div');
  oTitle.setAttribute('id', 'delTitle');
  oTitle.appendChild(document.createTextNode("mhjones links"));

  del_icious.appendChild(oTitle);

  oForm = document.createElement('form');
  oForm.setAttribute('id', 'delForm');
  oForm.setAttribute('method', 'post');
  oForm.setAttribute('action', "http://mhjones.org/read/save");

  oTable = document.createElement("table");

  oTR1 = document.createElement('tr');
  oTD1 = document.createElement('td');
  oTD1.appendChild(document.createTextNode('URL'));

  oTD2 = document.createElement('td');
  oTD2.setAttribute('colspan', '2');
  oInput = document.createElement('input');
  oInput.setAttribute('name', 'url');
  oInput.value = location.href;
  oInput.setAttribute('type', 'text');

  oInput2 = document.createElement('input');
  oInput2.setAttribute('name', 'key');
  oInput2.value = '${key}';
  oInput2.setAttribute('type', 'hidden');

  oTD2.appendChild(oInput);
  oTD2.appendChild(oInput2);

  oTR1.appendChild(oTD1);
  oTR1.appendChild(oTD2);

  oTR2 = document.createElement('tr');
  oTD1 = document.createElement('td');
  oTD1.appendChild(document.createTextNode('Description'));

  oTD2 = document.createElement('td');
  oTD2.setAttribute('colspan', '2');
  oInput = document.createElement('input');
  oInput.setAttribute('name', 'title');
  oInput.value = document.title;
  oInput.setAttribute('type', 'text');

  oTD2.appendChild(oInput);

  oTR2.appendChild(oTD1);
  oTR2.appendChild(oTD2);

  oTR5 = document.createElement('tr');
  oTD1 = document.createElement('td');
  oTD1.setAttribute('colspan', '3');
  oTD1.setAttribute('id', 'delCenter');
  oInput = document.createElement('input');
  oInput.setAttribute('id', 'delSubmit');
  oInput.setAttribute('type', 'submit');
  oInput.value = "Add";

  oButton = document.createElement('input');
  oButton.onclick = del_escape;
  oButton.setAttribute('type', 'button');
  oButton.value = "Cancel";

  oTD1.appendChild(oInput);
  oTD1.appendChild(oButton);

  oTR5.appendChild(oTD1);

  oTable.appendChild(oTR1);
  oTable.appendChild(oTR2);
  oTable.appendChild(oTR5);

  oForm.appendChild(oTable);

  del_icious.appendChild(oForm);

  shutter = document.createElement('div');
  shutter.id = "delShutter";

  style = document.createElement('link');
  style.href = "http://mhjones.org/read/bookmarklet/css";
  style.rel = "stylesheet";
  style.type = "text/css";

  document.getElementsByTagName('head')[0].appendChild(style);

  document.body.appendChild(shutter);
  document.body.appendChild(del_icious);

  shutter.onclick = del_escape;
}

show_delicious();
