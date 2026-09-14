from shared.shared_models import embedding_model


class EmbeddingGenerator:

    def __init__(self):

        self.model = embedding_model

    def generate_embeddings(self, chunks):

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embeddings