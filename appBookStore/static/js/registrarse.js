var usuarioCrear1;


function registrarse(item){
    
/*
    alert('El usuario es'+document.getElementById("usuarioCrear").value);

    usuarioCrear1=document.getElementsById("usuarioCrear");
    nombreCrear = document.getElementsById("nombreCrear");
    usuarioCrear = toString(document.getElementsById(usuarioCrear));
    passCrear = toString(document.getElementsById(passCrear));

   */ 

    var nombre=document.getElementById("nombreCrear").value;
    var usuario=document.getElementById("usuarioCrear").value;
    var password=document.getElementById("passCrear").value;

    alert('El usuario es'+nombre+usuario+password);

    /*

    usuarioCrear1 = Usuario(nombre=document.getElementById("nombreCrear").value, usuario=document.getElementById("usuarioCrear").value, password=document.getElementById("passCrear").value);
    usuarioCrear1.save();  

    console.log(item);

    alert('El usuario es'+document.getElementById("usuarioCrear").value);
    
    */
    
};