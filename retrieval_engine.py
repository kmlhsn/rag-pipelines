class VectorStore:
    """Abstract class for the vector store interface."""
    def add(self, document):
        raise NotImplementedError("Subclasses should implement this method")

    def retrieve(self, query, top_k=5):
        raise NotImplementedError("Subclasses should implement this method")


class DocumentRetriever:
    """Retrieves documents from a vector store with caching and batch operations."""
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.cache = {}

    def retrieve(self, query, top_k=5):
        if query in self.cache:
            return self.cache[query]
        try:
            results = self.vector_store.retrieve(query, top_k)
            self.cache[query] = results
            return results
        except Exception as e:
            print(f"Error during retrieval: {e}")
            return []

    def batch_retrieve(self, queries, top_k=5):
        results = {}
        for query in queries:
            results[query] = self.retrieve(query, top_k)
        return results
