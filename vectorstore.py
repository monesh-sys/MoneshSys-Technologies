def store_in_pinecone(chunks, embeddings):

    print("Storing vectors...\n")

    for i in range(len(chunks)):

        print(f"Chunk {i+1} stored successfully")