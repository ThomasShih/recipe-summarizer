import os
import pinecone

pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="gcp-starter")
index = pinecone.Index('recipe-summaries-index')

def add_summary(title: str, summary: str, vector: list[float]) -> int:
    key = hash(title)
    index.upsert(
        vectors=[
            {
                'id': str(key), 
                'values': vector, 
                'metadata':{'summary': summary}, # Probablly want to store this in a proper database
            },
        ],
    )
    return key

def fetch_summary(vector: list[float]) -> str:
    results = index.query(
        vector=vector, 
        top_k=1,
        include_metadata=True,
    )

    if len(results.get("matches")) == 0:
        return "No results found"
    
    return results.get("matches")[0].get("metadata").get("summary")
