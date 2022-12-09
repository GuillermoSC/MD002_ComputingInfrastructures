from matplotlib import pyplot as plt

from Model.Person import Person


class Plotter:

    @staticmethod
    def plot_age_distribution(data: list[Person]):
        """
        Method to generate a plot of the age distribution histogram of the given data
        :param data: Reference data from where the ages are obtained
        """
        plt.clf()

        age_list = list(person.age for person in data)

        plt.xlabel('Ages')
        plt.ylabel('Population')
        plt.title('Age histogram')
        plt.grid(True)
        plt.xticks(rotation=45, ha='right')

        max_age = max(age_list)
        min_age = min(age_list)
        age_range = max_age - min_age
        plt.hist(age_list, bins=age_range)

        plt.savefig('age_hist.png')
        plt.close()

    @staticmethod
    def plot_country_distribution(data: list[Person]):
        """
        Method to generate a plot of the country users distribution histogram of the given data
        :param data: Reference data from where the countries are obtained
        """
        plt.clf()

        country_list = list(person.country for person in data)

        plt.xlabel('Country')
        plt.ylabel('Population')
        plt.title('Users by country histogram')
        plt.grid(True)
        plt.xticks(rotation=35, ha='right')
        plt.hist(country_list, bins=len(set(country_list)))

        plt.subplots_adjust(bottom=0.23)
        plt.savefig('country_hist.png')

