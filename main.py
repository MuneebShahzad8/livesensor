from sensor.exception import SensorException
import sys
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection

# def test_exception():
#     try:
#         logging.info("Jani")
#         a = 1/0
#     except Exception as e:
#         raise SensorException(e, sys)



if __name__ == "__main__":
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)
    file_path = "../livesensor/aps_failure_training_set1.csv"
    database_name = "MachineLearningProject"
    collection_name = "sensor"

    dump_csv_file_to_mongodb_collection(file_path, database_name, collection_name)