def chunk_pages(pages, chunk_size=500):
    chunks = []

    for page in pages:

        # Skip empty pages
        if not page:
            continue

        # Split text into smaller chunks
        for i in range(0, len(page), chunk_size):
            chunk = page[i:i + chunk_size]
            chunks.append(chunk)

    return chunks