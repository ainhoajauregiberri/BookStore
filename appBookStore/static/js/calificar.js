var contador;

function calificar(item){
    console.log(item);
    contador=item.id[0]; //captura primer caracter del id
    let nombre= item.id.substring(1);//captura toda la cadena despues del primer caracter (estrella)
    for(let i=0; i <5; i ++){
        if(i<contador){
            document.getElementById((i+1)+nombre).style.color="orange";

        }else{
            document.getElementById((i+1)+nombre).style.color="black";
        }
    }
    
};

function mensaje(item){
    alert('¡Gracias por calificar este libro con '+contador+' estrellas!');
    item.disabled= true;
  
}

function calcularMedia(item){

    var numValoraciones;
var media=1;
media=((libro.numValoraciones*media)+ contador)/(libro.numValoraciones+1);
libro.numValoraciones+=1;


}

