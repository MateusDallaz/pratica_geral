let peso = parseFloat(prompt('Digite seu peso (kg):'));
let altura = parseFloat(prompt('Digite sua altura (m): '));

function calcularImc(peso, altura){
    let imc = peso / (altura * altura);
    return imc;
}
let imc = calcularImc(peso, altura);
let resultado = `O valor final do IMC é: ${imc.toFixed(2)}`;
console.log(resultado);