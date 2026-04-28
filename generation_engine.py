import asyncio

class GenerationEngine:
    def __init__(self, model, context_limit=1024):
        self.model = model  # The underlying language model
        self.context_limit = context_limit  # Max context length
        self.context = []  # Initialize context

    def add_to_context(self, prompt):
        self.context.append(prompt)
        # Keep the context within the limit
        if len(self.context) > self.context_limit:
            self.context.pop(0)

    async def generate(self, prompt):
        self.add_to_context(prompt)
        output = await self.stream_response(prompt)
        return output

    async def stream_response(self, prompt):
        # Simulate a response being streamed back from the model
        for chunk in self.model.stream(prompt):
            yield chunk

    def validate_response(self, response):
        # Basic validation of the response
        return bool(response) and isinstance(response, str)

    async def generate_with_validation(self, prompt):
        response = await self.generate(prompt)
        if self.validate_response(response):
            return response
        else:
            raise ValueError('Invalid response generated.')

# Example usage (assuming an async capable framework):
# async def main():
#     engine = GenerationEngine(model)
#     result = await engine.generate_with_validation('What is the capital of France?')
#     print(result)

# asyncio.run(main())