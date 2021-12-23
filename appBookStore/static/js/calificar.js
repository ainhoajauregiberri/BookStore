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

function mediaBD(item, id, mediaValoracion, numValoraciones){

    const sqlite3 = require('sqlite3').verbose();

    let db = new sqlite3.Database('./db.sqlite3.db')

    alert('¡Gracias por calificar este libro con '+contador+' estrellas!');
    item.disabled= true;
    mediaValoracion=((numValoraciones*mediaValoracion)+contador)/(numValoraciones+1);
    numValoraciones+=1;

    let data = [mediaValoracion, mediaValoracion];
     
    var sql = 'UPDATE Libro set mediaValoracion=? and numValoraiones=? where id=?'

    db.run(sql, data, function(err){
        if(err){
            return console.error(err.message);
        }
        console.log('Row(s) updated: ${this.changes}');

    });

    alert('Se ha guardado la media '+mediaValoracion+' y el numero de valoraciones es '+numValoraciones);

    db.close();
}
/*

parseInt(document.getElementById(1).media)

*/
