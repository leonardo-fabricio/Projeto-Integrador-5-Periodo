{% load static %}
{% load bootstrap4%}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerenciamento de Reservas</title>
    <link rel="stylesheet" href="{% static 'css/style.css'%}">
    <link rel="shortcut icon" type="image/png" href="{% static 'img/icon.png' %}" />
</head>
<body>
    <!-- Imagem e texto -->
<nav class="nav nav-pills">
    <li class="nav-item">
        <a class="nav-link disabled" href="#">
            <img src="{% static 'img/reservado.png'%}" width="30" height="30" class="d-inline-block align-top" alt="">
            Gerenciamento de Reservas
        </a>
    </li>
  
    <li class="nav-item">
        <a class="nav-link disabled" href="#">Reservas</a>
    </li>
    <li class="nav-item">
        <a class="nav-link disabled" href="#">Confirmações</a>
    </li>
    <li class="nav-item">
        <a class="nav-link disabled" href="#">Meus agendamentos</a>
    </li>
</nav>
<br>
<!-- Cards -->
<div class="card text-center">
  <div class="card-body">
    <h5 class="card-title">Agendameto 1</h5>
    <p class="card-text">
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type
        specimen book. It has survived not only five centuries, but also the leap 
        into electronic typesetting, remaining essentially unchanged. It was 
        popularised in the 1960s with the release of Letraset sheets containing 
        Lorem Ipsum passages, and more recently with desktop publishing software 
          ike Aldus PageMaker including versions of Lorem Ipsum.
    </p>
    <a href="#" class="btn btn-primary">Participar</a>
  </div>
</div>

<div class="card text-center">
  <div class="card-body">
    <h5 class="card-title">Agendamento 2</h5>
    <p class="card-text">
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
        Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
        when an unknown printer took a galley of type and scrambled it to make a type
        specimen book. It has survived not only five centuries, but also the leap 
        into electronic typesetting, remaining essentially unchanged. It was 
        popularised in the 1960s with the release of Letraset sheets containing 
        Lorem Ipsum passages, and more recently with desktop publishing software 
          ike Aldus PageMaker including versions of Lorem Ipsum.
    </p>
    <a href="#" class="btn btn-primary">Participar</a>
  </div>
</div>

   
</body>
</html>