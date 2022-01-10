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
    
    document.getElementsByClassName("form-puntuacion").value() = contador
    } 
};

function mediaEstrellas(item, mediaValoracion){
    console.log(item);
    let nombre= item.id.substring(1);
    for(let i=0; i <5; i ++){
        if(i<mediaValoracion){
            document.getElementById((i+1)+nombre).style.color="orange";
        }else{
            document.getElementById((i+1)+nombre).style.color="black";
        }
    }
};
