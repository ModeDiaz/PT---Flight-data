import logging

from flight_data_module import (
    load_json_data,
    load_csv_data,
    parse_log_data,
    combine_data,
    calculate_revenue_per_passenger
)

error_handler = logging.FileHandler("error.log")
error_handler.setLevel(logging.ERROR)

debug_handler = logging.FileHandler("debug.log")
debug_handler.setLevel(logging.DEBUG)

json_data = load_json_data("./data.json")
csv_data = load_csv_data("./data.csv")
log_data = parse_log_data("./data.log")

combined_data = combine_data(json_data, csv_data, log_data)

calculate_revenue_per_passenger(combined_data)
print(combined_data)