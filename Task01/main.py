from Model.Person import Person, get_age, get_name_len, get_years_registered, get_gender_value
from Utils import Utils
from Utils.DataLoader import DataLoader, API_URL
from Utils.Plotter import Plotter


def get_str_info(name: str, data: list[Person], getter) -> str:
    """
    Method to obtain a string with a verbose text to show the analysis of a value sequence. It obtains the statistics
    for the average value, the mean and standard deviation of the complete sequence given
    :param name: Name of the data to analyse
    :param data: Structure with all the necessary data and instances
    :param getter: function to use to extract the necessary value to analyse from a given instance of the sequence
    :return: The string in verbose format containing the results from the analysis
    """

    msg = "-" * 50 + '\n'
    msg += "%s Avg:  %.3f\n" % (name, Utils.average(data, getter))
    msg += "%s Mean: %.3f\n" % (name, Utils.mean(data, getter))
    msg += "%s Sd:   %.3f\n" % (name, Utils.standard_deviation(data, getter))
    return msg


def process_file(data: list[Person]):
    """
    Method to generate an output file with a series of analysis and statistics obtained by the given data
    :param data: List of Person objects that contain all the necessary info to evaluate
    """

    text = "Collected %d instances from %s" % (len(data), API_URL)
    text += get_str_info("Age", data, get_age)
    text += get_str_info("Name length", person_list, get_name_len)
    text += get_str_info("Years reg.", person_list, get_years_registered)
    text += get_str_info("Gender", person_list, get_gender_value)

    with open('results.txt', 'w') as f:
        f.write(text)


def process_plot(data: list[Person]):
    """
    Method to generate a plot of the age distribution histogram of the given data
    :param data: Reference data from where the ages are obtained
    """
    Plotter.plot_age_distribution(data)
    Plotter.plot_country_distribution(data)


if __name__ == "__main__":
    print("Loading data...", end='')
    info = DataLoader.import_data(n_values=1000, load_cache=True)
    print("[Done]")

    print("Processing data...", end='')
    person_list = DataLoader.convert_to_people(info)
    print("[Done]")

    # Process person data structure and generate output file with statistics and analysis
    process_file(person_list)

    # Process data to generate an output plot of the age distribution histogram
    process_plot(person_list)
