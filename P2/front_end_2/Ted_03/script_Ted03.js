let nomes = ["Ana", "João", "Maria", "Carlos", "Paula"];
console.log(nomes[2]);

nomes.push("Pedro");
nomes.unshift("Lucas");
console.log(nomes);

nomes.pop();
console.log(nomes);

let numeros = [2, 4, 6, 8];
let dobrados = numeros.map(num => num * 2);
console.log(dobrados);

let numerosFiltrados = [1, 3, 5, 7, 9].filter(num => num > 5);
console.log(numerosFiltrados);
