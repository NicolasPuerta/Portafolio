Formulario = document.querySelector(".formulario");
nombre = document.querySelector("#nombre");
email = document.querySelector("#email");
mensaje = document.querySelector("#mensaje");
btn = document.querySelector("#btnEnviar");

console.log('Holas');
btn.addEventListener("click", (event) => {
  event.preventDefault();
  if (nombre.value === "" || email.value === "" || mensaje.value === "") {
    alert("Todos los campos deben estar diligenciados, gracias");
    return;
  }
  Formulario.submit();
});

