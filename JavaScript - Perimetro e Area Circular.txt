let raio = parseFloat(prompt("Digite o raio da sala circular:"));

function calcularSalaCircular(raio) {
    const pi = 3.14;

    let area = pi * raio * raio;
    let perimetro = 2 * pi * raio;

    console.log(`Área: ${area.toFixed(2)}`);
    console.log(`Perímetro: ${perimetro.toFixed(2)}`);
}

calcularSalaCircular(raio);