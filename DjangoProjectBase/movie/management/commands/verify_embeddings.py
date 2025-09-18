import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Verifica que los embeddings se almacenaron correctamente en la base de datos"

    def handle(self, *args, **kwargs):
        movies = Movie.objects.all()
        if not movies.exists():
            self.stdout.write(self.style.WARNING("⚠️ No hay películas en la base de datos."))
            return

        for movie in movies:
            if movie.emb:
                try:
                    embedding_vector = np.frombuffer(movie.emb, dtype=np.float32)
                    # Mostramos solo los primeros 5 valores para no saturar consola
                    self.stdout.write(f"🎬 {movie.title} → {embedding_vector[:5]}")
                except Exception as e:
                    self.stderr.write(f"❌ Error al procesar {movie.title}: {str(e)}")
            else:
                self.stdout.write(f"⚠️ {movie.title} no tiene embedding almacenado.")
