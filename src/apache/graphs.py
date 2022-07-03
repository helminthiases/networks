import os
import pathlib
import pyspark.sql
import graphframes

import src.functions.directories


class Graphs:

    def __init__(self, spark: pyspark.sql.SparkSession):
        """

        :param spark:
        """

        self.spark = spark

        # the network check point directory
        directories = src.functions.directories.Directories()
        self.tunnel = os.path.join(os.getcwd(), 'tmp')
        directories.cleanup(self.tunnel)
        directories.create(self.tunnel)

    def __read(self, path):
        """

        :param path:
        :return:
        """

        data = self.spark.read.format("csv").option("inferSchema", "true").option("header", "true").load(path)
        data.printSchema()

        return data

    def exc(self, path: str):
        """

        :param path:
        :return:
        """

        # the network check point directory
        self.spark.sparkContext.setCheckpointDir(os.path.join(self.tunnel, pathlib.Path(path).stem))

        # the data in focus, and the vertices & edges data therein
        data = self.__read(path=path)
        vertices = data.selectExpr("id", "id as name").distinct()
        edges = data.select('id', 'admin1_id', 'admin2_id', 'longitude', 'latitude', 'shortest', 'src', 'dst')
        
        # the graphs
        entities = graphframes.GraphFrame(v=vertices, e=edges)
        graphs: pyspark.sql.DataFrame = entities.connectedComponents()
        graphs.show()
