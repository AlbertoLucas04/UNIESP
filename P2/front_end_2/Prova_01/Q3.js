let n = parseInt(prompt("Quantos números você deseja informar?"));

if (isNaN(n) || n <= 0) {
  alert("Por favor, informe um número válido maior que zero.");
} else {
  let soma = 0;
  let menor = null;
  let maior = null;

  for (let i = 1; i <= n; i++) {
    let numero = parseFloat(prompt(`Digite o ${i}º número:`));

    if (isNaN(numero)) {
      alert("Valor inválido! Digite um número.");
      i--;
      continue;
    }

    soma += numero;

    if (menor === null || numero < menor) {
      menor = numero;
    }

    if (maior === null || numero > maior) {
      maior = numero;
    }
  }

  alert(`Menor valor: ${menor}\nMaior valor: ${maior}\nSoma dos valores: ${soma}`);
}
