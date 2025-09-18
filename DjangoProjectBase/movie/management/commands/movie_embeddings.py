import os
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from movie.models import Movie

class Command(BaseCommand):
    help = "Generate embeddings for all movies"

    def handle(self, *args, **kwargs):
        # 👇 Cargar variables desde openAI.env
        load_dotenv("openAI.env")

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.stdout.write(self.style.ERROR("❌ No se encontró la API Key. Revisa tu archivo openAI.env"))
            return

        client = OpenAI(api_key=api_key)

        movies = Movie.objects.all()
        self.stdout.write(f"🎬 Encontradas {movies.count()} películas en la base de datos")

        for movie in movies:
            response = client.embeddings.create(
                input=[movie.description],
                model="text-embedding-3-small"
            )
            emb_array = np.array(response.data[0].embedding, dtype=np.float32)
            movie.emb = emb_array.tobytes()
            movie.save()
            self.stdout.write(f"👌 Embedding generado para: {movie.title}")

        self.stdout.write(self.style.SUCCESS("🌟 Embeddings generados para todas las películas"))
