% include('headerIndex.tpl')
<h1>MongoDB search </h1>
 <form action="/" method="post">
		    <label>Usuario:</label>
		       <input type="text" name="name"/>
		    <p></p>
		    <label>Base de datos:</label>
		       <input type="text" name="Base"/>
        <p></p>
		    <label>Coleccion:</label>
		       <input type="text" name="Coleccion"/>
		  <input type="submit" value="Send"/>
 </form>
% include('footer.tpl')
