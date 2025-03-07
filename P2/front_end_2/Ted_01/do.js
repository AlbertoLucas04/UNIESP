const alturasMasc = [1.75, 1.80, 1.78, 1.82, 1.76, 1.85, 1.79, 1.74, 1.81, 1.77, 1.83, 1.86, 1.90, 1.88, 1.84];  

const alturasFem = [1.65, 1.70, 1.68, 1.72, 1.66, 1.75, 1.69, 1.64, 1.71, 1.67, 1.73, 1.76, 1.78, 1.74, 1.68];  

const maxMasc = Math.max(...alturasMasc);
const maxFem = Math.max(...alturasFem);

const minMasc = Math.min(...alturasMasc);
const minFem = Math.min(...alturasFem);

const mediaAlturasMasc = alturasMasc.length > 0 
    ? alturasMasc.reduce((a, b) => a + b, 0) / alturasMasc.length : 0;

    const mediaAlturasMascModelado = mediaAlturasMasc.toFixed(2);

const qtdFem = alturasFem.length;


const putOption = parseInt(prompt("=== Olá, seja bem-vindo(a) ao Expositor de Dados ===\n\nDe qual grupo você deseja obter os dados?\n\n1. Masculino\n2. Feminino\n3. Ambos os grupos"));

switch (putOption) {

    case 1:
        console.log("\nSegue os dados solicitados.\n");
        console.log("Dados (Grupo Masculino)");
        console.log(`Maior altura: ${maxMasc} m`);
        console.log(`Menor altura: ${minMasc} m`);
        console.log(`Média das alturas: ${mediaAlturasMascModelado} m\n`);
        break;

    case 2:
        console.log("\nSegue os dados solicitados.\n");
        console.log("Dados (Grupo Feminino)");
        console.log(`Maior altura: ${maxFem} m`);
        console.log(`Menor altura: ${minFem} m`);
        console.log(`Quantidade de pessoas: ${qtdFem}\n`);
        break;

    case 3:
        console.log("\nSegue os dados solicitados.\n");
        console.log("Dados (Grupo Masculino)");
        console.log(`Maior altura: ${maxMasc} m`);
        console.log(`Menor altura: ${minMasc} m`);
        console.log(`Média das alturas: ${mediaAlturasMascModelado} m\n`);
        console.log("Dados (Grupo Feminino)");
        console.log(`Maior altura: ${maxFem} m`);
        console.log(`Menor altura: ${minFem} m`);
        console.log(`Quantidade de pessoas: ${qtdFem}`);
        break;

    default:
        console.log("Insira um código válido.");

}
