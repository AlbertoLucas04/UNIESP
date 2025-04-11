let pares = 0;
let impares = 0;

for (let i = 1; i <= 10; i++) {
  let numero = parseInt(prompt(`Digite o ${i}º número inteiro:`));

  if (isNaN(numero)) {
    alert("Por favor, digite um número válido!");
    i--;
    continue;
  }

  if (numero % 2 === 0) {
    pares++;
  } else {
    impares++;
  }
}

alert(`Quantidade de números pares: ${pares}\nQuantidade de números ímpares: ${impares}`);
