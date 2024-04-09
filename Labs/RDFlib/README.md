## Run py script
Este lab consulta el servicio [Users]([https://duckduckgo.com](https://reqres.in/api/users), parse el objecto JSON de la respuesta e inserta un set de RDF triplas en un nuevo graph. Utiliza [RDFlib](https://rdflib.readthedocs.io/en/stable/) y [SPARQLWrapper](https://sparqlwrapper.readthedocs.io/en/latest/)

#### Preconfigurar script

<ol>
<li>Crear un repositorio llamado 'curso-kg' en GraphDB. </li>
<li>Reemplazar la URI del repositorio en el script 'api2RDF.py'. </li>
Notar que la API de GraphDB requiere esta estructura '/repositories/{repositoryID}/statements'
</ol>

#### Instalar dependencias
```
pip3 install requirements.txt
```
#### Ejecutar script
```
python3 api2RDF.py
```

## Autores
Germán Braun - Laura Cecchi

