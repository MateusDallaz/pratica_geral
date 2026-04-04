let valor = parseFloat(prompt("Digite o valor em dólar:"));
function converterDolarParaReal(valorDolar) {
    const cotacao = 4.80;
    return valorDolar * cotacao;
}

let resultado = converterDolarParaReal(valor);

console.log(`Valor em reais: R$ ${resultado.toFixed(2)}`);
