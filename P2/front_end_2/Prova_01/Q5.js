function calcularAreaPerimetroCirculo() {
    let raio = parseFloat(prompt("Informe o raio do círculo:"));
  
    if (isNaN(raio) || raio <= 0) {
      alert("Por favor, digite um valor válido e maior que zero para o raio.");
      return;
    }
  
    let area = Math.PI * Math.pow(raio, 2);
    let perimetro = 2 * Math.PI * raio;
  
    alert(
      `Com raio = ${raio}:\nÁrea do círculo: ${area.toFixed(2)}\nPerímetro (circunferência): ${perimetro.toFixed(2)}`
    );
  }
  
  calcularAreaPerimetroCirculo();
  