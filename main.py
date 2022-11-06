import matplotlib.pyplot as plt
import requests


def import_data() -> list:
    data = requests.get(url='https://randomuser.me/api/', params={'results': 1000})
    data.raise_for_status()

    return data.json()["results"]



def get_ages() ->list:
    get_ages = []
    for person in info:
        get_ages.append(person['dob']['age'])
    return get_ages




def mean_ages() ->int:
    mean_ages = 0
    for person in get_ages():
        mean_ages += person
    return mean_ages/len(get_ages())



def variance() -> int:
    var = 0
    ages = get_ages()
    m = ages_mean
    n = len(ages)
    for person in ages:
        var = var + (person - m) ** 2

    return var / n



def process_plot():
    plt.xlabel('Age')
    plt.ylabel('Population')
    plt.title('Age hist')
    plt.hist(get_ages(), bins=(max(get_ages()) - min(get_ages())))
    plt.grid(True)
    plt.xticks(rotation=45, ha='right')

    plt.savefig('hist_age.png')
    plt.show()


if __name__ =="__main__":
    info = import_data()
    ages_mean = mean_ages()
    hist_age = process_plot()
    variance = variance()






print(ages_mean)
print(hist_age)
print(variance)
