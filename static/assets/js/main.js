try{
    let eventExists = document.querySelector('.card.mb-3.event-card.bbbb')
    if(!eventExists){
        let us = document.querySelector('.h4.mb-0.text-gray-800.alg')
        us.innerHTML = '<h3>Olá, comece criando seus eventos clicando em <b>Criar Agendamento</b> <br>ou <a href="http://127.0.0.1:8000/criarEvento"><b>Clicando Aqui</b></a></h3>'
        
        us.style.marginTop = '75px'
        us.style.marginLeft = '145px'
    }else{
      us.innerHTML = '<br><h4 id="h4Stile" class="h4 mb-0 text-gray-800 alg" style="margin-top: -5px;">ALGUNS EVENTOS CRIADOS POR VOCÊ</h4>'
    }
}catch(err){
    console.log('ERRO: ' + err)
}

var urlAtual = window.location.href;
if(urlAtual == "http://127.0.0.1:8000/criarEvento"){;
  let text = document.querySelector("h4.mb-0.text-gray-800.alg");
  let text2 = document.querySelector("h4.mb-3.text-gray-800.create")
  text.style.display = 'none';
  text2.style.marginTop = '7px';
}
$(document).ready(function(){
  $("#id_horaInicial").inputmask("h:s",{ "placeholder": "hh/mm" });
});

(function($) {
  
  "use strict";  

  $(window).on('load', function() {

  /*Page Loader active
  ========================================================*/
  $('#preloader').fadeOut();

  // Sticky Nav
    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 50) {
            $('.scrolling-navbar').addClass('top-nav-collapse');
        } else {
            $('.scrolling-navbar').removeClass('top-nav-collapse');
        }
    });

    // one page navigation 
    $('.navbar-nav').onePageNav({
      currentClass: 'active'
    });

    /* Auto Close Responsive Navbar on Click
    ========================================================*/
    function close_toggle() {
        if ($(window).width() <= 768) {
            $('.navbar-collapse a').on('click', function () {
                $('.navbar-collapse').collapse('hide');
            });
        }
        else {
            $('.navbar .navbar-inverse a').off('click');
        }
    }
    close_toggle();
    $(window).resize(close_toggle);

    /* WOW Scroll Spy
    ========================================================*/
     var wow = new WOW({
      //disabled for mobile
        mobile: false
    });

    wow.init();    

     /* Testimonials Carousel 
    ========================================================*/
    var owl = $("#testimonials");
      owl.owlCarousel({
        loop: true,
        nav: false,
        dots: true,
        center: true,
        margin: 15,
        slideSpeed: 1000,
        stopOnHover: true,
        autoPlay: true,
        responsiveClass: true,
        responsiveRefreshRate: true,
        responsive : {
            0 : {
                items: 1
            },
            768 : {
                items: 2
            },
            960 : {
                items: 3
            },
            1200 : {
                items: 3
            },
            1920 : {
                items: 3
            }
        }
      });  
      

    /* Back Top Link active
    ========================================================*/
      var offset = 200;
      var duration = 500;
      $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
          $('.back-to-top').fadeIn(400);
        } else {
          $('.back-to-top').fadeOut(400);
        }
      });

      $('.back-to-top').on('click',function(event) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: 0
        }, 600);
        return false;
      });

  });      

}(jQuery));

var googleUser = {};
  var startApp = function() {
    gapi.load('auth2', function(){
      // Retrieve the singleton for the GoogleAuth library and set up the client.
      auth2 = gapi.auth2.init({
        client_id: 'YOUR_CLIENT_ID.apps.googleusercontent.com',
        cookiepolicy: 'single_host_origin',
        // Request scopes in addition to 'profile' and 'email'
        //scope: 'additional_scope'
      });
      attachSignin(document.getElementById('customBtn'));
    });
  };

  function attachSignin(element) {
    console.log(element.id);
    auth2.attachClickHandler(element, {},
        function(googleUser) {
          document.getElementById('name').innerText = "Signed in: " +
              googleUser.getBasicProfile().getName();
        }, function(error) {
          alert(JSON.stringify(error, undefined, 2));
        });
  }