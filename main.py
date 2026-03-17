def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    
    cleaned_heartrate_data = []
    skipped_count = 0
    
    for number in data:
        try:
            hr = int(number)
            if 30 <= hr <= 220:
                cleaned_heartrate_data.append(hr)
            else:
                skipped_count += 1
        except ValueError:
            skipped_count += 1
            
    return tuple(cleaned_heartrate_data), skipped_count


def average(data: list) -> float:
    """
    Calculate average of a list of integers using a for-loop. Assumes data is clean.
    """

    total = 0
    for value in data:
        total += value
    average = total / len(data)
    return float(average)



def median(data: list) -> float:
    """
    """

    sorted_data = sorted(data)
    n = len(sorted_data)
    median = n // 2

    if n % 2 == 0:
        return (sorted_data[median - 1] + sorted_data[median]) / 2
    else:
        return float(sorted_data[median])
   



def range(data: list) -> float:
    """
    """

    max = data[0]
    min = data[0]

    for value in data:
        if value > max:
           max = value
        if value < min:
            min = value
    range = max - min
    return float(range)
    


def rolling_avg(data: list, k: int) -> float:
    """
    CHALLENGE FUNCTION (Optional)
    """
 
    pass


def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []

    # open file using file I/O and read it into the `data` list
    
    file_object = open(file)

    data = file_object.readlines()
        

    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    cleaned_list, removed_values = clean_heartrate_data(data)

    # calculate the average, median, and range of this file using the functions you've wrote
    
    average_hr = average(cleaned_list)
    median_hr = median(cleaned_list)
    range_hr = range(cleaned_list)
    

    # print out your data quality measure to the console
    
    print("File:", file)
    print("Skippend Rows:", removed_values)

    # print out your descriptive statistics to the console
    
    print("Average:", average_hr, "Median:", median_hr, "Range:", range_hr)
    print("_" * 30)
    
    
if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
