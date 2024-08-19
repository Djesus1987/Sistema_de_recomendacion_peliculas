from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = FastAPI()

# Suponiendo que tienes un DataFrame global
df = pd.read_csv('Datasets/MoviesF.csv')

class ResponseMessage(BaseModel):
    message: str

@app.get('/cantidad_filmaciones_mes/{mes}', response_model=ResponseMessage)
async def cantidad_filmaciones_mes(mes: str):
    try:
        # Convertir mes de español a inglés
        mes_dict = {
            'enero': 'January', 'febrero': 'February', 'marzo': 'March',
            'abril': 'April', 'mayo': 'May', 'junio': 'June',
            'julio': 'July', 'agosto': 'August', 'septiembre': 'September',
            'octubre': 'October', 'noviembre': 'November', 'diciembre': 'December'
        }
        mes_en = mes_dict.get(mes.lower())
        if not mes_en:
            raise HTTPException(status_code=400, detail="Mes inválido")
        
        # Filtrar y contar
        df['release_date'] = pd.to_datetime(df['release_date'])
        count = df[df['release_date'].dt.strftime('%B') == mes_en].shape[0]
        return ResponseMessage(message=f'{count} cantidad de películas fueron estrenadas en el mes de {mes.capitalize()}')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/cantidad_filmaciones_dia/{dia}', response_model=ResponseMessage)
async def cantidad_filmaciones_dia(dia: str):
    try:
        # Convertir día de español a inglés
        dia_dict = {
            'lunes': 'Monday', 'martes': 'Tuesday', 'miércoles': 'Wednesday',
            'jueves': 'Thursday', 'viernes': 'Friday', 'sábado': 'Saturday',
            'domingo': 'Sunday'
        }
        dia_en = dia_dict.get(dia.lower())
        if not dia_en:
            raise HTTPException(status_code=400, detail="Día inválido")
        
        # Filtrar y contar
        df['release_date'] = pd.to_datetime(df['release_date'])
        count = df[df['release_date'].dt.strftime('%A') == dia_en].shape[0]
        return ResponseMessage(message=f'{count} cantidad de películas fueron estrenadas en los días {dia.capitalize()}')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/score_titulo/{titulo}', response_model=ResponseMessage)
async def score_titulo(titulo: str):
    try:
        movie = df[df['title'].str.contains(titulo, case=False, na=False)]
        if movie.empty:
            raise HTTPException(status_code=404, detail="Película no encontrada")
        
        movie = movie.iloc[0]
        return ResponseMessage(message=f'La película {movie["title"]} fue estrenada en el año {movie["release_year"]} con un score/popularidad de {movie["popularity"]}')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/votos_titulo/{titulo}', response_model=ResponseMessage)
async def votos_titulo(titulo: str):
    try:
        movie = df[df['title'].str.contains(titulo, case=False, na=False)]
        if movie.empty:
            raise HTTPException(status_code=404, detail="Película no encontrada")
        
        movie = movie.iloc[0]
        if movie['vote_count'] < 2000:
            return ResponseMessage(message='La película no cumple con la condición de tener al menos 2000 valoraciones.')
        
        return ResponseMessage(message=f'La película {movie["title"]} fue estrenada en el año {movie["release_year"]}. La misma cuenta con un total de {movie["vote_count"]} valoraciones, con un promedio de {movie["vote_average"]}')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/get_actor/{nombre_actor}")
def get_actor(nombre_actor: str):
    # Suponemos que el DataFrame ya está cargado en una variable global
    dataset = pd.read_csv('Datasets/Actores.csv')
    
    # Filtrar el dataset por el nombre del actor
    actor_data = dataset[dataset['name'] == nombre_actor]
    
    if actor_data.empty:
        raise HTTPException(status_code=404, detail="Actor no encontrado")
    
    # Calcular el retorno total y el promedio de retorno
    total_return = actor_data['return'].sum()
    average_return = actor_data['return'].mean()
    
    # Contar la cantidad de películas
    film_count = actor_data.shape[0]
    
    return {
        "mensaje": f"El actor {nombre_actor} ha participado de {film_count} cantidad de filmaciones.",
        "total_return": total_return,
        "average_return": average_return
    }


class MovieDetails(BaseModel):
    title: str
    release_date: str
    budget: float
    revenue: float
    return_on_investment: float

@app.get('/get_director')
def get_director(nombre_director: str) -> Dict[str, List[MovieDetails]]:
    # Aquí se asume que el dataset ha sido cargado en una variable global o contexto.
    # Vamos a simular esto con un ejemplo de cómo podrías acceder a los datos.
    dataset = pd.read_csv('Datasets/Directores.csv')
    # Cargar datos del dataset. Esto debería hacerse en el archivo principal.
    # Por ejemplo:
    # dataset = cargar_dataset()
    
    # Filtrar datos por director
    director_data = dataset[dataset['name'] == nombre_director]
    
    if director_data.empty:
        raise HTTPException(status_code=404, detail="Director no encontrado")
    
    # Obtener películas del director
    movies = []
    for _, row in director_data.iterrows():
        movie_details = {
            "title": row['title'],
            "release_date": row['release_date'],
            "budget": row['budget'],
            "revenue": row['revenue'],
            "return_on_investment": (row['revenue'] - row['budget']) / row['budget'] if row['budget'] > 0 else 0
        }
        movies.append(movie_details)
    
    return {"success": True, "movies": movies}


# Función de recomendación
@app.get('/get_recomendacion')
def recomendacion(titulo: str, top_n: int = 5):
    # Cargar el dataset
    dataset = pd.read_csv('Datasets/MoviesML.csv')
    
    # Filtrar las películas existentes
    if titulo not in dataset['title'].values:
        raise ValueError("El título de la película no se encuentra en el dataset.")
    
    # Crear una matriz TF-IDF de los títulos de las películas
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['title'])
    
    # Obtener el índice del título de la película
    idx = dataset.index[dataset['title'] == titulo].tolist()[0]
    
    # Calcular la similitud de coseno entre la película seleccionada y todas las demás
    cosine_sim = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    
    # Obtener los índices de las películas más similares
    similar_indices = cosine_sim.argsort()[-top_n-1:-1][::-1]
    
    # Obtener los nombres de las películas similares
    similar_titles = dataset.iloc[similar_indices]['title'].tolist()
    
    return similar_titles