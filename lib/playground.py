import os
import cohere 

co = cohere.Client(os.getenv("COHERE_API_KEY"))

def summarize_recipe(text):
    response = co.summarize( 
        text=f"Extract all the relevant steps to make the recipe, include no redundant information: {text}",
        length='long',
        format='bullets',
        model='summarize-xlarge',
        temperature=0.3,
    ) 
    return response