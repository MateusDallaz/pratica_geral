//let titulo = document.querySelector("h1");
//titulo.innerHTML = "Jogo do Número Secreto";

//let paragrafo = document.querySelector("p");
//paragrafo.innerHTML = "Escolha um número entre 1 e 1000";
let numeroSecreto = numeroAleatorio();
let tentativas = 1;

function exibirTexto(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

function exibirMensagemInicial(){
    exibirTexto('h1', 'Jogo do Número Secreto');
    exibirTexto('p', 'Escolha um número entre 1 e 1000');
}

exibirMensagemInicial();

function verificarChute() {
    let chute = document.querySelector('input').value;
    console.log(numeroSecreto);
    if (chute == numeroSecreto){
        exibirTexto('h1', 'Acertou!' );
        let palavraTentativa =  tentativas > 1 ? 'tentativas': 'tentativa';
        let mensagemTentativa = `Parabéns você acertou o número secreto com ${tentativas} ${palavraTentativa}`;
        exibirTexto('p', mensagemTentativa);
        document.getElementById('reiniciar').removeAttribute('disabled');
    }else {
        if(chute > numeroSecreto){
            exibirTexto('h1', 'Você errou!');
            exibirTexto('p',  `O número secreto é menor que: ${chute}`);
        }else{
            exibirTexto('h1', 'Você errou!');
            exibirTexto('p', `O número secreto é maior que: ${chute}`);
        }
        tentativas++;
        limparCampo()
    }
}

function numeroAleatorio() {
    return parseInt(Math.random() * 1000 + 1);
}

function limparCampo() {
    chute = document.querySelector('input');
    chute.value = '';
}

function reiniciarJogo(){
    numeroSecreto = numeroAleatorio();
    limparCampo();
    tentativas = 1;
    exibirMensagemInicial();
    document.getElementById('reiniciar').setAttribute('disabled', true);
}