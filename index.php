

<?php
   if(isset($_POST['enviar'])){ // si damos clic al botón calcular entonces ...
                        
        if($_POST['op'] === "1"){ // si esta activo el radiobutton sumar entonces ...
            $resul = $_POST['potencia'] + $_POST['demanda']; // a la variable resul le asignamos la suma de los campos
        }
        elseif($_POST['op'] === "2"){ //sino, si esta activo el radio restar entonces ...
            $resul = $_POST['potencia'] - $_POST['demanda'];
        }
        elseif($_POST['op'] === "3"){
            $resul = $_POST['potencia'] * $_POST['demanda'];
        }
        else{
            $resul = $_POST['potencia'] / $_POST['demanda'];
        }
        
    }
?>
<!DOCTYPE html>

<html lang="es">
    <head>
        <meta charset="UTF-8"/>
        <title>Calculadora malota</title>
    </head>
    
    <body>
     <h2>Calculadora de calibres</h2>    
     <form method="post"> 
        <label>Dato de potencia</label>
        <input name="potencia" type="text" pattern="[0-9.]+" placeholder="Ingrese dato de potencia" required autofocus/>
        <br /><br /><label>Factor de demanda</label>
        <input type="text" name="demanda" pattern="[0-9.]+" placeholder="Ingrese factor de demanda" required/>
		
		 <!-- <br /><br /><label>SUMAR</label>
 <input type="radio" name="op" value="1" checked/>
             -->
 <br>
 <br>
 
 <label class="text">Tipo de red</label>
 <br>
 <input type="radio" name="op" value="2"/>
 <label>Monofasica</label>
 <br>       
 <input type="radio" name="op" value="3"/>
 <label>Bifasica</label>
 <br>    
 <input type="radio" name="op" value="4"/>
 <label>Trifasica</label>
		
		<br /><br /><input type="submit" value="CALCULAR" name="enviar"/>
	 </form>
    </body>
    <br /><br /><label>Resultado:</label>
<input type="text" name="res" value="<?php if(isset($_POST['enviar'])){ echo $resul;} ?>" readonly>
                  

</html>