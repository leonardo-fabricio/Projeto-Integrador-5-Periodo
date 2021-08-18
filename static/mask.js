window.onload = function(){
    try{
        const labels = document.querySelectorAll('div.form-criar-evento > form > div > label')
        const inputs = document.querySelectorAll('input')
        labels[0].innerText = 'Quantidade de pessoas'
        labels[1].innerText = 'Hora inicial do evento'
        labels[2].innerText = 'Hora final do evento'
        labels[3].innerText = 'Data do evento'
        inputs[1].type = 'number'
    }catch(err){
        console.log('Erro ao modificar labels: ' + err)
    }
}

$(function(){
    $('#id_telefone').mask('+00(00)0.0000-0000', {reverse: true})
});

$(function(){
    var mask = "HH:MM",
    pattern = {
        'translation': {
            'H': {
                pattern: /[00-23]/
            },
            'M': {
                pattern: /[00-59]/
            }
        }
    };

    $('#id_horaInicial').mask(mask, pattern)
    $('#id_horaFinal').mask(mask,pattern)
});

$(function(){
    $('#id_dataEvento').mask('00/00/0000', {reverse:true})
});


