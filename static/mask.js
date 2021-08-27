window.onload = function(){
    try{
        const labels = document.querySelectorAll('div.form-criar-evento > form > div > label')
        const inputs = document.querySelectorAll('input')
        labels[0].innerText = 'Título do Evento'
        labels[1].innerText = 'Descrição do Evento'
        labels[2].innerText = 'Quantidade de pessoas'
        labels[3].innerText = 'Hora inicial do evento'
        labels[4].innerText = 'Hora final do evento'
        labels[5].innerText = 'Data do evento'
        labels[7].innerText = 'Imagem do Evento'
        inputs[3].type = 'number'
        inputs[4].type = 'time'
        inputs[5].type = 'time'
        inputs[6].type = 'date'
    }catch(err){
        console.log('Erro ao modificar labels: ' + err)
    }
}

$(function(){
    $('#id_telefone').mask('00(00)0.0000-0000', {reverse: true})
});

$(function(){
    $('#id_cep').mask('00000-000', {reverse: true})
});


