class Retriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def search(self, query, source_type=None, k=5):
        """
        query: user prompt
        source_type: pdf | website | article | None
        """
        results = self.vector_store.similarity_search(query, k=k)

        if source_type:
            results = [r for r in results if r.metadata.get("source") == source_type]

        return results
