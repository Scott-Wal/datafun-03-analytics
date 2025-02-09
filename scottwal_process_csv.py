"""
Process a CSV file on baseball statistics to analyze the `RBI` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def analyze_rbi_statistics(file_path: pathlib.Path) -> dict:
    """Analyze the RBI column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        rbi_statistics = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    rbi = float(row["rbi"])  # Extract and convert to float
                    # append the score to the list
                    rbi_statistics.append(rbi)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(rbi_statistics),
            "max": max(rbi_statistics),
            "mean": statistics.mean(rbi_statistics),
            "stdev": statistics.stdev(rbi_statistics) if len(rbi_statistics) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze RBIs, and save the results."""
    input_file = pathlib.Path(fetched_folder_name, "baseball.csv")
    output_file = pathlib.Path(processed_folder_name, "baseball_stats.txt")
    
    stats = analyze_rbi_statistics(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("RBI Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")