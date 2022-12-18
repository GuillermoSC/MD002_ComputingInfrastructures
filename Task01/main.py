import matplotlib.pyplot as plt
import requests



def import_data() -> list:
    data = requests.get(url='https://randomuser.me/api/', params={'results': 10})
    data.raise_for_status()

    return data.json()["results"]



def get_ages() -> list:
    get_ages = []
    for person in import_data():
        get_ages.append(person['dob']['age'])
    return get_ages




def mean_ages() -> int:
    mean_ages_var = 0
    for person in get_ages():
        mean_ages_var += person
    return mean_ages_var / len(get_ages())

def median() -> int:
    assert len(get_ages()) > 0
'''
- Pending to calculate median 
'''





def variance() -> int:
    var = 0
    for person in range(0, len(get_ages())):
        var = var + (person - mean_ages()) ** 2
    return var / len(get_ages())
'''
- Pending to calculate variance based on median rather than average
'''




def process_plot():
    plt.xlabel('Age')
    plt.ylabel('Population')
    plt.title('Age hist')
    plt.hist(ages, bins=(max(ages) - min(ages)))
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')

    plt.savefig('hist_age.png')
    plt.show()


if __name__ =="__main__":
    info = import_data()
    ages_mean = mean_ages()
    ages = get_ages()
    hist_age = process_plot()
    variance = variance()
'''
    with open('results.txt', 'w') as f:
        f.write(text)
'''









