from openai import OpenAI

# OpenRouter Client
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

def embed_chunks(chunks):

    embeddings = []

    for chunk in chunks:

        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )

        embedding = response.data[0].embedding

        embeddings.append(embedding)

    return embeddings