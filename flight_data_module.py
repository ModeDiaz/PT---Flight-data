import json
import logging
import csv
from typing import List,Dict, Any

#Procesamiento de datos

def load_json_data(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
            if "flights" in data:
                return data["flights"]
            else:
                logging.warning("No se encontró flights en el JSON.")
                return []
    except Exception as e:
        logging.error(f"Error al cargar el JSON data desde {file_path}: {e}")
        return []

def load_csv_data(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
            return data
    except Exception as e:
        logging.error(f"Error al cargar el CSV data desde {file_path}: {e}")
        return []

def parse_log_data(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path, "r") as log_file:
            data = []
            for line in log_file:
                fields = line.strip().split(",")
                log_entry = {
                    "Date": fields[0],
                    "Flight_ID": fields[1],
                    "Departure_Airport": fields[2],
                    "Arrival_Airport": fields[3],
                }
                data.append(log_entry)
            return data
    except Exception as e:
        logging.error(f"Error al analizar el log data desde {file_path}: {e}")
        return []



#Transformación de datos

def combine_data(json_data: List[Dict[str, Any]], csv_data: List[Dict[str, Any]], log_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    try:
        combined_data = []
        for json_entry in json_data:
            flight_id = json_entry.get("Flight_ID", "")
            date = json_entry.get("Date", "")
            departure = json_entry.get("Departure_Airport", "")
            arrival = json_entry.get("Arrival_Airport", "")

            csv_entry = next((entry for entry in csv_data if entry.get("Flight_ID", "") == flight_id), {})
            log_entry = next((entry for entry in log_data if entry.get("Flight_ID", "") == flight_id), {})

            combined_entry = {
                "Flight_ID": flight_id,
                "Date": date,
                "Departure_Airport": departure,
                "Arrival_Airport": arrival,
                "Duration_Minutes": log_entry.get("Duration_Minutes", ""),
                "Passengers": csv_entry.get("Passengers", ""),
                "Revenue": csv_entry.get("Revenue", "")
            }

            combined_data.append(combined_entry)

        return combined_data
    
    except Exception as e:
        logging.error(f"Error en la combinación del data: {e}")
        return []

def calculate_revenue_per_passenger(flights_data: List[Dict[str, Any]]) -> None:
    try:
        for flight in flights_data:
            passengers = int(flight.get("Passengers", 0))
            duration_minutes = int(flight.get("Duration_Minutes", 0)) if flight.get("Duration_Minutes", "") != "" else 0
            revenue = float(flight.get("Revenue", 0))

            if passengers != 0:
                flight["Revenue_Per_Passenger"] = revenue / passengers
            else:
                flight["Revenue_Per_Passenger"] = 0
    
    except Exception as e:
        logging.debug(f"Hubo un problema al calcular el valor por pasajero: {e}")
