import json
import logging
import os

import pyspark.sql


class Schema:

    def __init__(self, spark: pyspark.sql.SparkSession):
        """

        :param spark:
        """

        self.spark = spark

        # logging
        logging.basicConfig(level=logging.INFO,
                            format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        self.logger = logging.getLogger(__name__)

    def __schema(self):
        """

        :return:
        """

        path = os.path.join(os.getcwd(), 'data', 'schema')

        # later, transform to a StructType
        stream = self.spark.sparkContext.textFile(os.path.join(path, 'experiments.json'))
        for element in stream.collect():
            self.logger.info(element)

        # the schema of the experiments data
        with open(os.path.join(path, 'experiments.json'), 'r') as disk:
            objects = json.load(disk)

        return objects

    def exc(self):
        """

        :return:
        """

        return self.__schema()
