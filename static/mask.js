$(function(){
    $('.mask-cep').mask('00000-000', {reverse : true})
});

$(function(){
    $('#id_telefone').mask('+00 (00) 0.0000-0000', {reverse: true})
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


