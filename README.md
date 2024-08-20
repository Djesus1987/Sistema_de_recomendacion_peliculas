# Sistema de recomendación de Peliculas

## Descripción del proyecto
Se desarrolla una API para consultas con un sistema de recomendación de peliculas. Los endpoints permiten consultar información tal como: fechas de estreno, popularidad, directores, actores, y el rendimienbto generado y no menos importante, un sistema de recomendación segun la pelicula seleccionada.

## Desafíos y roles a desarrollar
al explorar los datasets, se percibió:
desorden y datos anidados. rol de Data Scientist: con la misión de desarrollar el sistema de recomendación, rol de Data Engineer: creacion de un MVP (Minimum Viable Product).

## Tecnologías Utilizadas
Utilizamos Python con las siguientes librerías:

- Pandas
- Numpy
- Scikit-learn
- Uvicorn
- FastAPI
- Ast
- TextBlob
- Seaborn
- Matplotlib
- Wordcloud

## 1) Transformación de Datos
Para optimizar el rendimiento de la API y del modelo de machine learning, trabajé en la lectura del dataset en el formato correcto, eliminando columnas innecesarias y realizando las transformaciones necesarias. dejando como resultado, de dos datasets originales, tres datasets: dos para las funciones principales de la API y un dataset para el sistema de recomendacion. 

## 2) Análisis Exploratorio de Datos (EDA)
Llevé a cabo un análisis exploratorio de los datos para identificar relaciones entre variables, detectar outliers y anomalías, y descubrir patrones interesantes. Este análisis fue crucial para entender los datos y prepararlos adecuadamente para el modelado.

## 3) Despliegue y uso de la API
La API está desplegada en Render y se puede acceder a través de varios endpoints:

- cantidad_filmaciones_mes( Mes ): devuelve la cantidad de películas que fueron estrenadas en el mes consultado.
                    
- cantidad_filmaciones_dia( Dia ): Devuelve la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.
                   
- score_titulo( titulo_de_la_filmación ): Decuelve el título, el año de estreno y el score.
                    
- votos_titulo( titulo_de_la_filmación ): Devuelve el título, la cantidad de votos y el valor promedio de las votaciones.

- get_actor( nombre_actor ): Devuelve el éxito del mismo medido a través del retorno, la cantidad de películas que en las que ha participado y el promedio de retorno. 

- get_director( nombre_director ):Devuelve el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, retorno individual, costo y ganancia de la misma.

# Conclusión

## Resumen
El desarrollo de un sistema de recomendación de películas combina técnicas de análisis de datos, procesamiento de texto y machine learning para ofrecer sugerencias personalizadas. En este proyecto, se implementaron dos enfoques principales: uno basado en popularidad, que recomienda películas valoradas por su puntaje promedio y cantidad de votos, y otro basado en similitud de contenido, que sugiere películas con características similares. Este sistema sirve como una base práctica que puede ser expandida con técnicas más avanzadas para mejorar la experiencia del usuario.

Por otro lado, se desarrolló un sistema de consulta para extraer información detallada sobre películas, actores y directores. A través de endpoints específicos, los usuarios pueden realizar consultas que les permiten acceder rápidamente a datos clave. Estos endpoints permiten obtener la cantidad de películas estrenadas en un mes o día específico, información sobre la recepción de una película, y un análisis del éxito de actores y directores basado en el retorno de inversión de sus películas. Este sistema es una herramienta poderosa para el análisis de la industria cinematográfica, ofreciendo información detallada para investigadores y profesionales del cine.

## Información extra
Modelo de Similitud de Coseno:
El modelo de similitud de coseno es una técnica comúnmente utilizada en la recuperación de información y el filtrado colaborativo, que permite calcular la similitud entre vectores de características. En el contexto de este sistema de recomendación de videojuegos para Steam, el modelo se utiliza para encontrar juegos similares en función de las características de los mismos.

En la implementación de este proyecto, se calculó la similitud de coseno entre vectores de características que representan diferentes juegos. Estos vectores de características pueden incluir información como género, desarrollador, reseñas de usuarios, entre otros. Una vez calculada la similitud de coseno, se identificaron los juegos más similares y se recomendaron al usuario.

Para calcular la similitud de coseno, se utilizó la biblioteca scikit-learn en Python, que proporciona herramientas eficientes para el análisis de datos y la minería de textos.

# Glosario:
- Data Scientist: Un profesional que utiliza técnicas estadísticas, de programación y de aprendizaje automático para analizar y obtener información a partir de datos.

- Data Engineer: Un especialista en el diseño y mantenimiento de sistemas de gestión de datos, incluidas bases de datos, pipelines de datos y plataformas de almacenamiento de datos.

- MVP (Minimum Viable Product): El producto mínimo viable es una versión simplificada de un producto que se utiliza para probar la viabilidad de una idea y recopilar feedback de los usuarios antes de invertir en su desarrollo completo.

- ETL (Extract, Transform, Load): Proceso utilizado para extraer datos de varias fuentes, transformarlos en un formato adecuado y cargarlos en un sistema de destino, como una base de datos.

- API (Application Programming Interface): Un conjunto de reglas y definiciones que permite a diferentes software comunicarse entre sí. En este contexto, se refiere a la interfaz de programación de la aplicación utilizada para acceder y manipular los datos de Steam.

- EDA (Exploratory Data Analysis): Proceso de análisis de datos para resumir las características principales de un conjunto de datos, a menudo con métodos visuales.

Despliegue de la API: La acción de hacer que una API esté disponible y accesible para su uso, generalmente a través de un servidor web o una plataforma en la nube.

# Autor

D´Jesús Blanco 
