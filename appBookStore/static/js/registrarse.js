var usuarioCrear1;


function registrarse(item){
    
/*
    alert('El usuario es'+document.getElementById("usuarioCrear").value);

    usuarioCrear1=document.getElementsById("usuarioCrear");
    nombreCrear = document.getElementsById("nombreCrear");
    usuarioCrear = toString(document.getElementsById(usuarioCrear));
    passCrear = toString(document.getElementsById(passCrear));

   */ 

    var nombreCrear=document.getElementById("nombreCrear").value;
    var usuarioCrear=document.getElementById("usuarioCrear").value;
    var passwordCrear=document.getElementById("passCrear").value;

  

    usuarioCrear1 = Usuario(nombre='Eneida', usuario='eneida98', password='kaixo1234');
    usuarioCrear1.save();
    alert('El usuario es'+nombreCrear+usuarioCrear+passwordCrear);

    /*
    usuarioCrear1
    nombre=nombreCrear, usuario=usuarioCrear, password=passwordCrear, notificar=false
    usuarioCrear1.save();  

    alert('El usuario es'+nombreCrear+usuarioCrear+passwordCrear);

    */

    console.log(item);
    
    
};