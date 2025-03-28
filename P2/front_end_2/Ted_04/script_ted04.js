function calcularTotal(precoUnitario, quantidade) {
    return precoUnitario * quantidade;
}

function aplicarDesconto(valorTotal) {
    if (valorTotal > 100) {
        return valorTotal * 0.9;  // Aplica 10% de desconto
    }
    return valorTotal;  // Sem desconto
}

function exibirResumo(precoUnitario, quantidade) {
    let valorTotal = calcularTotal(precoUnitario, quantidade);
    let valorComDesconto = aplicarDesconto(valorTotal);

    let resumo = `
        <p><strong>Resumo da Compra:</strong></p>
        <p><strong>Preço Unitário:</strong> R$ ${precoUnitario.toFixed(2)}</p>
        <p><strong>Quantidade:</strong> ${quantidade}</p>
        <p><strong>Valor Total (sem desconto):</strong> R$ ${valorTotal.toFixed(2)}</p>
        <p><strong>Valor Final (com desconto):</strong> R$ ${valorComDesconto.toFixed(2)}</p>
    `;

    document.body.innerHTML += resumo;  // Exibe o resumo no corpo da página
}

// Lê os dados do usuário usando prompt()
let precoUnitario = parseFloat(prompt("Digite o preço unitário do produto:"));
let quantidade = parseInt(prompt("Digite a quantidade comprada:"));

// Exibe o resumo
exibirResumo(precoUnitario, quantidade);