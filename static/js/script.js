
// THIS IS THE TOGGLER FOR THE BREAK EVEN TEXTAREA
if (document.getElementById("id_be")){
  const breakEven = document.getElementById("id_be");
  const breakEvenTextarea = document.getElementById("id_Reason_For_be");

//  THIS WILL HIDE THE TEXTAREA UNTIL THE BE IS CHECKED
  window.addEventListener('load', ()=> {
    if (!breakEven.checked) {
      breakEvenTextarea.parentNode.style.display = 'none';
    }
  })

  breakEven.addEventListener('click', ()=> {
    if(breakEven.checked){
      breakEvenTextarea.parentNode.style.display = 'block';
    }else {
      breakEvenTextarea.parentNode.style.display = 'none';
    }
  })
}
