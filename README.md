# Análisis de padrones electorales

El informe final del script *analyze.py* incluye:  
.- Detectar votantes duplicados dentro de un mismo padron y crontra todos los cargados.  
.- Hacer un informe de votantes por domiclio de cada padron.  
  
### Padrones a procesar
  
Son los encontrados en la carpeta **/padronesListos** en formato CSV.  
Estos archivos son derivados en general de PDFs obtenidos. En algunos 
casos fue necesario algun posprocesamiento (que se incluye).  
  
### Padrones no terminados
  
Algunos padrones todavía no han podido procesarse y se encuentran en la 
carpeta **/padronesAProcesar**.  
  
### Ejecutar todos los procesos

```
$ python analize.py
```

### Resultados

Luego de ejecutados los procesos en la carpeta **/domicilios-mas-usados** se 
escribirá un archivo por cada padrón con los docimicilios más usados. Este 
archivo es bastante extenso y entrega primero una lista de los domicilios y 
en segunda instancia el detalle de los votantes incluidos en cada domicilio.  

Por otro lado el archivo **dnis_repetidos.csv** incluirá los votantes repetidos 
en todos los padrones vía el Documento Nacional de Identidad de cada uno.  

### Colaboración

Aquel que tenga padrones oficiales puede enviarlos por email a andres@data99.com.ar 
o realizar los procesos y enviar un *pull-request*.  

### Conclusiones

Claramente la forma de estos datos es bastante poco prolija. Las justicias electorales 
deberán *aggiornarse* incluyendo en sus procesos de control a analistas de datos.  
Los partidos políticos deben involucrarse tambien con nuevas formas de control.  
Los estados provinciales y nacionales deben avanzar en la clarificación de los 
domicilios solicitando se especifiquen mejor los numeros de casa (notablemente 
ausentes en muchos casos) y llamando a nombrar las numerosas calles *públicas* 
que todavía existen.  
