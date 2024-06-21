import csv

# Generate fuzzy rules for the Osteospermum ecklonis plant.
def GenerateFuzzyRules():
    # Define the fuzzy rules data
    fuzzy_rules = [
        [1, 'cold', 'low', 'dry', 'low', 'much'],
        [2, 'cold', 'low', 'dry', 'medium', 'much'],
        [3, 'cold', 'low', 'dry', 'high', 'medium'],
        [4, 'cold', 'low', 'medium', 'low', 'much'],
        [5, 'cold', 'low', 'medium', 'medium', 'medium'],
        [6, 'cold', 'low', 'medium', 'high', 'little'],
        [7, 'cold', 'low', 'wet', 'low', 'medium'],
        [8, 'cold', 'low', 'wet', 'medium', 'little'],
        [9, 'cold', 'low', 'wet', 'high', 'none'],
        [10, 'cold', 'medium', 'dry', 'low', 'much'],
        [11, 'cold', 'medium', 'dry', 'medium', 'much'],
        [12, 'cold', 'medium', 'dry', 'high', 'medium'],
        [13, 'cold', 'medium', 'medium', 'low', 'much'],
        [14, 'cold', 'medium', 'medium', 'medium', 'medium'],
        [15, 'cold', 'medium', 'medium', 'high', 'little'],
        [16, 'cold', 'medium', 'wet', 'low', 'medium'],
        [17, 'cold', 'medium', 'wet', 'medium', 'little'],
        [18, 'cold', 'medium', 'wet', 'high', 'none'],
        [19, 'cold', 'high', 'dry', 'low', 'much'],
        [20, 'cold', 'high', 'dry', 'medium', 'much'],
        [21, 'cold', 'high', 'dry', 'high', 'medium'],
        [22, 'cold', 'high', 'medium', 'low', 'much'],
        [23, 'cold', 'high', 'medium', 'medium', 'medium'],
        [24, 'cold', 'high', 'medium', 'high', 'little'],
        [25, 'cold', 'high', 'wet', 'low', 'medium'],
        [26, 'cold', 'high', 'wet', 'medium', 'little'],
        [27, 'cold', 'high', 'wet', 'high', 'none'],
        [28, 'medium', 'low', 'dry', 'low', 'much'],
        [29, 'medium', 'low', 'dry', 'medium', 'much'],
        [30, 'medium', 'low', 'dry', 'high', 'medium'],
        [31, 'medium', 'low', 'medium', 'low', 'medium'],
        [32, 'medium', 'low', 'medium', 'medium', 'medium'],
        [33, 'medium', 'low', 'medium', 'high', 'little'],
        [34, 'medium', 'low', 'wet', 'low', 'medium'],
        [35, 'medium', 'low', 'wet', 'medium', 'little'],
        [36, 'medium', 'low', 'wet', 'high', 'none'],
        [37, 'medium', 'medium', 'dry', 'low', 'much'],
        [38, 'medium', 'medium', 'dry', 'medium', 'much'],
        [39, 'medium', 'medium', 'dry', 'high', 'medium'],
        [40, 'medium', 'medium', 'medium', 'low', 'medium'],
        [41, 'medium', 'medium', 'medium', 'medium', 'medium'],
        [42, 'medium', 'medium', 'medium', 'high', 'little'],
        [43, 'medium', 'medium', 'wet', 'low', 'medium'],
        [44, 'medium', 'medium', 'wet', 'medium', 'little'],
        [45, 'medium', 'medium', 'wet', 'high', 'none'],
        [46, 'medium', 'high', 'dry', 'low', 'much'],
        [47, 'medium', 'high', 'dry', 'medium', 'much'],
        [48, 'medium', 'high', 'dry', 'high', 'medium'],
        [49, 'medium', 'high', 'medium', 'low', 'medium'],
        [50, 'medium', 'high', 'medium', 'medium', 'medium'],
        [51, 'medium', 'high', 'medium', 'high', 'little'],
        [52, 'medium', 'high', 'wet', 'low', 'medium'],
        [53, 'medium', 'high', 'wet', 'medium', 'little'],
        [54, 'medium', 'high', 'wet', 'high', 'none'],
        [55, 'hot', 'low', 'dry', 'low', 'much'],
        [56, 'hot', 'low', 'dry', 'medium', 'medium'],
        [57, 'hot', 'low', 'dry', 'high', 'medium'],
        [58, 'hot', 'low', 'medium', 'low', 'medium'],
        [59, 'hot', 'low', 'medium', 'medium', 'medium'],
        [60, 'hot', 'low', 'medium', 'high', 'little'],
        [61, 'hot', 'low', 'wet', 'low', 'medium'],
        [62, 'hot', 'low', 'wet', 'medium', 'little'],
        [63, 'hot', 'low', 'wet', 'high', 'none'],
        [64, 'hot', 'medium', 'dry', 'low', 'much'],
        [65, 'hot', 'medium', 'dry', 'medium', 'medium'],
        [66, 'hot', 'medium', 'dry', 'high', 'medium'],
        [67, 'hot', 'medium', 'medium', 'low', 'medium'],
        [68, 'hot', 'medium', 'medium', 'medium', 'medium'],
        [69, 'hot', 'medium', 'medium', 'high', 'little'],
        [70, 'hot', 'medium', 'wet', 'low', 'medium'],
        [71, 'hot', 'medium', 'wet', 'medium', 'little'],
        [72, 'hot', 'medium', 'wet', 'high', 'none'],
        [73, 'hot', 'high', 'dry', 'low', 'medium'],
        [74, 'hot', 'high', 'dry', 'medium', 'medium'],
        [75, 'hot', 'high', 'dry', 'high', 'little'],
        [76, 'hot', 'high', 'medium', 'low', 'medium'],
        [77, 'hot', 'high', 'medium', 'medium', 'medium'],
        [78, 'hot', 'high', 'medium', 'high', 'little'],
        [79, 'hot', 'high', 'wet', 'low', 'medium'],
        [80, 'hot', 'high', 'wet', 'medium', 'little'],
        [81, 'hot', 'high', 'wet', 'high', 'none']
    ]

    # Define the CSV file name
    csv_file = 'osteospermum_ecklonis_fuzzy_rules.csv'

    # Write the data to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Rule Index', 'Temperature', 'Humidity', 'Moisture', 'Light', 'Watering'])
        # Write the rules
        for rule in fuzzy_rules:
            writer.writerow(rule)

    print(f'CSV file "{csv_file}" has been created.')
