var containerLogin = document.getElementById('container-login');  
var containerRegistration = document.getElementById('container-registration');
var containerChange = document.getElementById('container-change');
var containerButton = document.getElementById('container-button');
var Logo = document = document.getElementById('logo');
var buttonLogin = document.getElementById('button-login');
var buttonRegistration = document.getElementById('button-registration');

//Navegação entre formulários
function Registration(){
    containerLogin.style.display = 'none';
    containerRegistration.style.display = 'block';

    buttonLogin.style.color = 'var(--color-text)';
    buttonLogin.style.borderBottom = '2px solid var(--color-text)';

    buttonRegistration.style.color = 'var(--color-highlight)';
    buttonRegistration.style.borderBottom = '2px solid var(--color-highlight)';
}

function Login(){
    containerRegistration.style.display = 'none';
    containerLogin.style.display = 'block';

    buttonLogin.style.color = 'var(--color-highlight)';
    buttonLogin.style.borderBottom = '2px solid var(--color-highlight)';

    buttonRegistration.style.color = 'var(--color-text)';
    buttonRegistration.style.borderBottom = '2px solid var(--color-text)';
}

function chagePassword(){
    containerRegistration.style.display = 'none';
    containerLogin.style.display = 'none';
    containerButton.style.display = 'none';
    Logo.style.display = 'none';
    containerChange.style.display = 'block';
}

function closeChange(){
    containerChange.style.display = 'none';
    Logo.style.display = 'block';
    containerButton.style.display = 'block';
    containerLogin.style.display = 'block';
}

var Senha = document.getElementById('password-registration');
var Minimo = document.getElementById('minimo');
var Maiuscula = document.getElementById('maiuscula');
var Minuscula = document.getElementById('minuscula');
var Numero = document.getElementById('numero');
var Especial = document.getElementById('especial');


//Validação de senha
function verificarSenhaForte() {
    var senha = Senha.value;
    if (senha.length < 8) {
        return false;
    }

    var temMaiuscula = /[A-Z]/.test(senha);
    var temMinuscula = /[a-z]/.test(senha);
    var temNumero = /\d/.test(senha);
    var temEspecial = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(senha);

    if (temMaiuscula && temMinuscula && temNumero && temEspecial) {
        return true;
    } else {
        return false;
    }
}


function verificarSenha() {
    var senha = Senha.value;
    if (verificarSenhaForte(senha)) {
        return true;
    } else {
        alert('A senha não atende aos padrões');
        event.preventDefault();
        return false;
    }
}
//Alteração de cores para os requisitos da senha
Senha.addEventListener("input", function () {
    var senha = this.value;

    
    if (senha.length >= 8) {
        Minimo.style.color = 'var(--color-text)';
    }
        else{
            Minimo.style.color = 'var(--color-highlight)';
        }

    if (/[A-Z]/.test(senha)) {
        Maiuscula.style.color = 'var(--color-text)';
    }
        else{
            Maiuscula.style.color = 'var(--color-highlight)';
        }

    if (/[a-z]/.test(senha)) {
        Minuscula.style.color = 'var(--color-text)';
    }
        else{
            Minuscula.style.color = 'var(--color-highlight)';
        }

    if (/\d/.test(senha)) {
        Numero.style.color = 'var(--color-text)';
    }
    else{
        Numero.style.color = 'var(--color-highlight)';
    }

    if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(senha)) {
        Especial.style.color = 'var(--color-text)';
    }
    else{
        Especial.style.color = 'var(--color-highlight)';
    }
});

//Validação de confirmação de senha
function validatePassword(){
    var password = Senha.value;
    var confirmPassword = document.getElementById("confirm-password").value;

        if (password != confirmPassword) {
            alert("As senhas não correspondem!");
            event.preventDefault();
            return false;
        }
        else {
            return true;
        }
}

//Validação de senha change
var SenhaChange = document.getElementById('password-change');
var MinimoC = document.getElementById('minimo-change');
var MaiusculaC = document.getElementById('maiuscula-change');
var MinusculaC = document.getElementById('minuscula-change');
var NumeroC = document.getElementById('numero-change');
var EspecialC = document.getElementById('especial-change');

function verificarSenhaForteC() {
    var senhaC = SenhaChange.value;
    if (senhaC.length < 8) {
        return false;
    }

    var temMaiusculaC = /[A-Z]/.test(senhaC);
    var temMinusculaC = /[a-z]/.test(senhaC);
    var temNumeroC = /\d/.test(senhaC);
    var temEspecialC = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/.test(senhaC);

    if (temMaiusculaC && temMinusculaC && temNumeroC && temEspecialC) {
        return true;
    } else {
        return false;
    }
}


function verificarSenhaC() {
    var senhaC = SenhaChange.value;
    if (verificarSenhaForteC(senhaC)) {
        return true;
    } else {
        alert('A senha não atende aos padrões');
        event.preventDefault();
        return false;
    }
}
//Alteração de cores para os requisitos da senha
SenhaChange.addEventListener("input", function () {
    var senhaC = this.value;

    
    if (senhaC.length >= 8) {
        MinimoC.style.color = 'var(--color-text)';
    }
        else{
            MinimoC.style.color = 'var(--color-highlight)';
        }

    if (/[A-Z]/.test(senhaC)) {
        MaiusculaC.style.color = 'var(--color-text)';
    }
        else{
            MaiusculaC.style.color = 'var(--color-highlight)';
        }

    if (/[a-z]/.test(senhaC)) {
        MinusculaC.style.color = 'var(--color-text)';
    }
        else{
            MinusculaC.style.color = 'var(--color-highlight)';
        }

    if (/\d/.test(senhaC)) {
        NumeroC.style.color = 'var(--color-text)';
    }
    else{
        NumeroC.style.color = 'var(--color-highlight)';
    }

    if (/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(senhaC)) {
        EspecialC.style.color = 'var(--color-text)';
    }
    else{
        EspecialC.style.color = 'var(--color-highlight)';
    }
});

//Validação de confirmação de senha
function validatePasswordC(){
    var passwordC = SenhaChange.value;
    var confirmPasswordC = document.getElementById("confirm-passwordc").value;

        if (passwordC != confirmPasswordC) {
            alert("As senhas não correspondem!");
            event.preventDefault();
            return false;
        }
        else {
            return true;
        }
}

//Lembrar dados no localStorage
window.onload = function() {
    var rememberedData = JSON.parse(localStorage.getItem('rememberedData'));
    if (rememberedData && rememberedData.remember) {
        document.getElementById('email-login').value = rememberedData.username;
        document.getElementById('password-login').value = rememberedData.password;
        document.getElementById('remember').checked = true;
    }
};

document.getElementById('remember').addEventListener('change', function(event) {
    var username = document.getElementById('email-login').value;
    var password = document.getElementById('password-login').value;
    var remember = document.getElementById('remember').checked;
    
    if (remember) {
        localStorage.setItem('rememberedData', JSON.stringify({username: username, password: password, remember: true}));
    } else {
        localStorage.removeItem('rememberedData');
    }
});

//contagem regressiva
var intervalo;

function contagemRegressiva(tempoTotal) {
    var contadorElemento = document.getElementById("contador");

    clearInterval(intervalo); // Limpa o intervalo anterior, se existir

    intervalo = setInterval(function() {
        var minutos = Math.floor(tempoTotal / 60);
        var segundos = tempoTotal % 60;

        contadorElemento.innerHTML = minutos + " : " + segundos;

        tempoTotal--;

        if (tempoTotal < 0) {
            clearInterval(intervalo);
            contadorElemento.innerHTML = "Tempo esgotado!";
            alert('Seu tempo esgotou gere um novo código de segurança clicando em gerar código de segurança.')
        }
    }, 1000); // Atualiza a cada 1 segundo (1000 milissegundos)
}

// Defina o tempo em segundos para a contagem regressiva (3 minutos = 180 segundos)
var tempoTotal = 180;




function securityCode(){
    var emailInput = document.getElementById('email-change');
    var emailValue = emailInput.value.trim();

    if (emailValue === '') {
        alert('Por favor, preencha o campo de e-mail antes de enviar o código.');
        return false;
    }
        else{
            alert('Clique em ok e enviaremos um código de segurança para seu e-mail, prencha o campo dentro de 3 minutos.Verifique se preencheu o e-mail corretamente.');
        }

}