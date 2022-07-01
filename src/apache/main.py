import glob
import logging
import os
import pathlib
import sys

import pyspark.sql


def main():
    """
    Probably for identifying identical experiment areas

    :return:
    """

    # instantiating
    spark: pyspark.sql.SparkSession = pyspark.sql.SparkSession.builder \
        .appName("Networks") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.master", "local[4]") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("WARN")

    # data sources
    hub = pathlib.Path(os.getcwd()).parent
    paths = glob.glob(pathname=os.path.join(hub, 'infections', 'warehouse',
                                            'data', 'ESPEN', 'networks', 'linear', '*.csv'))

    # networks
    graphs = src.apache.graphs.Graphs(spark=spark)
    for path in paths[1:2]:
        logger.info(path)
        graphs.exc(path=path)


if __name__ == '__main__':

    # directories
    root = os.getcwd()
    sys.path.append(root)
    sys.path.append(os.path.join(root, 'src'))

    graphDirectory = os.path.join(os.getcwd(), 'tmp')

    # logging
    logging.basicConfig(level=logging.INFO,
                        format='\n\n%(message)s\n%(asctime)s.%(msecs)03d',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(__name__)

    # custom classes
    import src.apache.graphs

    main()
