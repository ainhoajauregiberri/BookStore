var contador=0;

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

function mediaBD(item, mediaValoracion, numValoraciones){

    mediaValoracion=((numValoraciones*mediaValoracion)+ contador)/(numValoraciones+1);
    alert('Media '+mediaValoracion);
    numValoraciones+=1;
    
}
/*

parseInt(document.getElementById(1).media)
alert('¡Gracias por calificar este libro con '+contador+' estrellas!');
    item.disabled= true;

    


    alert('¡Gracias por calificar este libro con '+contador+' estrellas!');


item.disabled= true;

media=((libro.numValoraciones*ilbro.media)+ contador)/(libro.numValoraciones+1);

alert('Media '+media);
libro.numValoraciones+=1;
*/
