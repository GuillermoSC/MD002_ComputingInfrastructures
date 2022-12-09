import requests
from collections import Counter
import json


CACHE_FILENAME = 'api_cache.json'

def import_data() -> dict:
    try:
        with open(CACHE_FILENAME, 'r') as cache_file:
            data = json.load(cache_file)
            print('Se ha cargado el resultado de la llamada a la API desde el caché')
    except FileNotFoundError:
        data = requests.get("https://api.publicapis.org/entries")
        data.raise_for_status()
        data = data.json()
        with open(CACHE_FILENAME, 'w') as cache_file:
            json.dump(data, cache_file)
            print('Se ha guardado el resultado de la llamada a la API en el caché')
    return data


def get_categories(data) -> Counter:
    categories = []
    for entry in data['entries']:
        categories.append(entry['Category'])
    category_counts = Counter(categories)
    return category_counts

def get_apis(data) -> Counter:
    apis = []
    for entry in data['entries']:
        apis.append(entry['Auth'])
    apis_counts = Counter(apis)
    return apis_counts

def mean_categories(data) -> float:
    counts = list(get_categories(data).values())
    mean_cat = 0
    for count in counts:
        mean_cat += count
    return mean_cat / len(counts)

def mean_apis(data) -> float:
    counts = list(get_apis(data).values())
    mean_a = 0
    for count in counts:
        mean_a += count
    return mean_a / len(counts)

def variance_cat(data) -> float:
    mean = mean_categories(data)
    counts = list(get_categories(data).values())
    sum_cuadrados = 0
    for count in counts:
        sum_cuadrados += (count - mean) ** 2
    return sum_cuadrados / len(counts)

def variance_auth(data) -> float:
    mean = mean_apis(data)
    counts = list(get_apis(data).values())
    sum_cuadrados = 0
    for count in counts:
        sum_cuadrados += (count - mean) ** 2
    return sum_cuadrados/len(counts)

def stdev_cat(data) -> float:
    var = variance_cat(data)
    return var ** (1/2)

def stdev_auth(data) -> float:
    var = variance_auth(data)
    return var ** (1/2)

if __name__ == "__main__":
    data = import_data()
    cat = get_categories(data)
    apis = get_apis(data)
    mean_c = mean_categories(data)
    mean_a = mean_apis(data)
    var_c = variance_cat(data)
    var_a = variance_auth(data)
    std_cat = stdev_cat(data)
    std_auth = stdev_auth(data)


    print("-\n" * 10)
    print("TASK.2 --> ETL USING AN API AND A DOCKER CONTAINER\n"),
    print("-\n" * 10)
    print("EXISTING CATEGORIES\n")
    print(str(cat))
    print("-\n" * 10)
    print("EXISTING APIs AUTHENTIFICATIONS\n")
    print(str(apis))
    print("-\n" * 10)
    print("MEAN OF NUMBER OF APIs ON DIFFERENT CATEGORIES\n")
    print(str(mean_c))
    print("-\n" * 10)
    print("MEAN OF NUMBER OF APIs WITH DIFFERENT AUTHENTIFICATION\n")
    print(str(mean_a))
    print("-\n" * 10)
    print("VARIANCE OF ALL APIs WITH DIFFERENT CATEGORY\n")
    print(str(var_c))
    print("-\n" * 10)
    print("VARIANCE OF ALL APIs WITH DIFFERENT AUTHENTIFICATION\n")
    print(str(var_a))
    print("-\n" * 10)
    print("STANDARD DEVIATION OF ALL APIs WITH DIFFERENT CATEGORIES\n")
    print(str(std_cat))
    print("-\n" * 10)
    print("STANDARD DEVIATION OF ALL APIs WITH DIFFERENT AUTHENTIFICATIONS\n")
    print(str(std_auth))
    print("-\n" * 10)










