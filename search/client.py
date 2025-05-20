from algoliasearch_django import algolia_engine

def get_client():
    client = algolia_engine.client
    print("Client type:", type(client))  # Should print the class of the client
    print("Client methods:", dir(client))  # List available methods
    return client

def get_index(index_name='naruto_Product'):
    client = get_client()
    index = client.init_index(index_name)  # Correct, this is the method
    return index

def perform_search(query, **kwargs):
    index = get_index()
    results = index.search(query)
    return results