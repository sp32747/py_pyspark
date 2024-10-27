from _ast import Load

from pyspark.sql import SparkSession
from pyspark.sql.types import LongType

# Creating the SparkSession
spark = SparkSession.builder.appName("FirstApp").getOrCreate()


def cubed(s):
    return s * s * s


# register the UDF
spark.udf.register("cubed", cubed, LongType())

# generate the temp view

spark.range(1, 9).createOrReplaceTempView("udf_test")

spark.sql("select id ,cubed(id) as cubed_id from udf_test").show()
