// === VERSÃO 1: Salário inicial fixo de R$ 1.000,00 ===
let salarioFixo = 1000;
let anoAtual = new Date().getFullYear();
let percentualFixo = 0.0015; // 0,15%

for (let ano = 1996; ano <= anoAtual; ano++) {
  salarioFixo += salarioFixo * percentualFixo;
  if (ano >= 1997) {
    percentualFixo *= 2;
  }
}

alert(`VERSÃO 1\nSalário inicial fixo: R$ 1000,00\nSalário atual em ${anoAtual}: R$ ${salarioFixo.toFixed(2)}`);


// === VERSÃO 2: Salário informado pelo usuário ===
let salarioInicial = parseFloat(prompt("Digite o salário inicial do funcionário (ex: 1000):"));

if (isNaN(salarioInicial) || salarioInicial <= 0) {
  alert("Por favor, insira um valor válido maior que zero.");
} else {
  let salario = salarioInicial;
  let percentual = 0.0015;

  for (let ano = 1996; ano <= anoAtual; ano++) {
    salario += salario * percentual;
    if (ano >= 1997) {
      percentual *= 2;
    }
  }

  alert(`VERSÃO 2\nSalário inicial informado: R$ ${salarioInicial.toFixed(2)}\nSalário atual em ${anoAtual}: R$ ${salario.toFixed(2)}`);
}
