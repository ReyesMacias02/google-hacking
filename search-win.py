import googlesearch

def search_google(query, num_results=5):
    results = list(googlesearch.search(query, num_results=num_results))
    return results

def save_results_to_file(results, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(result + '\n')

if __name__ == "__main__":
    # Introduce el objetivo
    search_query = input("Introduce el objetivo de la búsqueda: ")

    # Realiza la búsqueda
    search_results = search_google(search_query)

    # Guarda los resultados en un archivo de texto
    file_name = "resultados_busqueda.txt"
    save_results_to_file(search_results, file_name)

    print(f"Los resultados de la búsqueda se han guardado en {file_name}")
