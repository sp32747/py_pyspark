from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import pyspark.sql.functions as func

#Creating the SparkSession
spark = SparkSession.builder.appName("FirstApp").getOrCreate()

#Defining schema for your DataFrame
myschema = StructType([\
                       StructField("userID", IntegerType(), True),
                       StructField("name", StringType(), True),
                       StructField("age",IntegerType(), True),
                       StructField("friends",IntegerType(), True),
                        ])
#Creating DataFrame on a CSV file
people = spark.read.format("csv")\
    .schema(myschema)\
    .option("path","C:/Users/WIN-10/fakefriends.csv")\
    .load()


people.show(5)

#Performing all thetransformations
output = people.select(people.userID,people.name\
                       ,people.age,people.friends)\
         .where(people.age < 30).withColumn('insert_ts', func.current_timestamp())\
         .orderBy(people.userID)
#Creating a Temp View
output.createOrReplaceTempView("peoples")
#Running a simple Spark SQL query
#spark.sql("select name,age,friends,insert_ts from peoples").show()

spark.sql("select name,age from peoples ").show(5)

output.write.format("csv").mode("overwrite").option("path","C:/Users/WIN-10/output/op/").partitionBy("age").save()