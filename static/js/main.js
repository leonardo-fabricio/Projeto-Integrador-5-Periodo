/**
  Renderiza o botão de login na tela
*/

let divWarning = document.querySelector('div.alert.alert-danger')
if(divWarning){
    divWarning.addEventListener("click", function() {
        divWarning.style.display = 'none'
    });
}

// card-suas-reservas
try{
    let eventsDisponible = document.querySelector('#card-suas-reservas.card.mb-3.event-card')

    if(!eventsDisponible){
        let message = document.querySelector('.h4.mb-0.text-gray-800.even')
        message.textContent = 'Olá, você ainda não está participando de nenhum evento. ' /* <b>Criar Agendamento</b> <br>ou <a href="http://127.0.0.1:8000/criarEvento"><b>Clicando Aqui</b></a></h3>' */
        message.style.padding = '120px'
        message.style.marginTop = '0px'

        let x = document.createElement('img')
        x.setAttribute("src", "https://i.pinimg.com/originals/26/1d/79/261d79eba10658c0dfb9da61c5b28755.png")
        x.setAttribute("width", "40px")
        x.style.marginTop = '0px'
        
        message.appendChild(x)

    }
}catch(err){
    console.log("ERRO 2: " + err)
}

function renderButton() {
    gapi.signin2.render('meu-botao', {
        'scope': 'email profile https://www.googleapis.com/auth/plus.login', // solicitando acesso ao profile e ao e-mail do usuário
        'width': 250,
        'height': 50,
        'longtitle': true,
        'theme': 'dark',
        'onsuccess': onSuccess,
        'onfailure': onFailure
    });
}

/**
  Função executada quando o login é efetuado com sucesso
*/
function onSuccess(googleUser) {
    // Recuperando o profile do usuário
    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log("Name: " + profile.getName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());

    // Recuperando o token do usuario. Essa informação você necessita passar para seu backend
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);
}

/**
  Função executada quando ocorrer falha no logn
*/
function onFailure(error) {
    console.log(error);
}

/**
  Função de deslogar o usuário
*/
function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
        console.log('User signed out.');
    });
}

(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);

$(document).ready(function(){
    $("#id_horaInicial").inputmask("h:s",{ "placeholder": "hh/mm" });
  });