import random
import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Muestra los embeddings de una película seleccionada al azar"

    def handle(self, *args, **kwargs):
        movies = list(Movie.objects.all())
        if not movies:
            self.stdout.write(self.style.ERROR("⚠️ No hay películas en la base de datos."))
            return

        # Selecciona una película al azar
        movie = random.choice(movies)

        # Recuperar el vector desde el campo binario
        embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)

        # Mostrar resultados
        self.stdout.write(self.style.SUCCESS(f"🎬 Película seleccionada: {movie.title}"))
        self.stdout.write(f"Primeros 10 valores del embedding:\n{embedding_vector[:10]}")
        self.stdout.write(f"Tamaño total del embedding: {len(embedding_vector)}")
