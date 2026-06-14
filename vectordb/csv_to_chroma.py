import os
import pandas as pd
import chromadb

def csv_to_chroma(csv_path: str, db_directory: str, collection_name: str):
    # load and validate CSV
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {csv_path}")
    df = pd.read_csv(csv_path)

    client = chromadb.PersistentClient(path=db_directory)
    collection = client.get_or_create_collection(
        name=collection_name
        )
    
    documents = []
    metadata = []
    ids = []

    for index, row in df.iterrows():
        input_text = str(row['user_input']).strip()
        response_text = str(row['response_msg']).strip()
        
        if not input_text or not response_text:
            continue  # Skip rows with empty input or response

        documents.append(response_text)
        metadata.append({'user_input': input_text})
        ids.append(str(index))  # Use the index as a unique ID
    
    if documents:
        print(f"Adding {len(documents)} documents to the collection '{collection_name}'...")
        collection.add(
            documents=documents,
            metadatas=metadata,
            ids=ids
        )
        print("Data added successfully.")
    else:
        print("No valid documents found to add to the collection.")
    
    