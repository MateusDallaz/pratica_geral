let altura = parseFloat(prompt("Digite a altura da sala:"));
let largura = parseFloat(prompt("Digite a largura da sala:"));

function calcularSala(altura, largura) {
    let area = altura * largura;
    let perimetro = 2 * (altura + largura);

    console.log(`Área: ${area}`);
    console.log(`Perímetro: ${perimetro}`);
}

calcularSala(altura, largura);