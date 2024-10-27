import sys

from pyspark import SparkConf
from pyspark.sql import *

from lib.logger import Log4j
from lib.utils import load_survey_df, count_by_country

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Hello Spark").master("local[2]").getOrCreate()
    logger = Log4j(spark)

    logger.info("starting hello Spark")

    survey_df = spark.read.option("header", "true").option("inferSchema", "true").csv(sys.argv[1])

    partitioned_survey_df = survey_df.repartition(2)

    count_df = count_by_country(partitioned_survey_df)

    logger.info(count_df.collect())
    # survey_df.show()

    #input("press enter")
    logger.info("Ending hello Spark")
