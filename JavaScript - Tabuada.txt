let numero = parseInt(prompt('Insira um número: '));

function mostrarTabuada(numero) {
    let i = 1;

    while (i <= 10) {
        console.log(`${numero} x ${i} = ${numero * i}`);
        i++;
    }
}
mostrarTabuada(numero);