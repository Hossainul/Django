document.addEventListener('DOMContentLoaded', function () {
    const toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function (toastEl) {
      new bootstrap.Toast(toastEl).show();
    });
  });




  // for increasing and decreasing car quantity

  function increment(button) {
    const input = button.parentElement.querySelector('input.quantity-input');
    input.stepUp();
  }

  function decrement(button) {
    const input = button.parentElement.querySelector('input.quantity-input');
    if (parseInt(input.value) > 1) {
      input.stepDown();
    }
  }