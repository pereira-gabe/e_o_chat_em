let contador = parseInt(document.getElementById("contadorGPT").innerText) || 0;

function aumentar(){
    contador++;
    document.getElementById("contadorGPT").innerText = contador;
}
