# TODO 1: Write PySpark Code to read Text file having JSON data and get the output as per below:
"""
Text File :
{
{
    "id": "1"
    "name": "sahil"
    "city": "[city1, city2, city3]"
},
{
    "id": "2"
    "name": "aditya"
    "city": "[city1, city2]"
}
}

Output :
id, name, city
1, sahil, city1
1, sahil, city2
1, sahil, city3
2, aditya, city1
2, aditya, city2
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import StringType, StructField, StructType, ArrayType, IntegerType
from pyspark.sql.functions import explode

spark = SparkSession.builder.appName('test').getOrCreate()

schema = StructType([
    StructField('id', StringType()),
    StructField('name', StringType()),
    StructField('city', ArrayType(StringType()))
])

df1.show(truncate=False)

df2 = df1.withColumn('city', explode('city'))

df2.show(truncate=False)

"""
+---+------+---------------------+
|id |name  |city                 |
+---+------+---------------------+
|1  |sahil |[city1, city2, city3]|
|2  |aditya|[city1, city2]       |
+---+------+---------------------+

+---+------+-----+
|id |name  |city |
+---+------+-----+
|1  |sahil |city1|
|1  |sahil |city2|
|1  |sahil |city3|
|2  |aditya|city1|
|2  |aditya|city2|
"""



