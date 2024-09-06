from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('test').getOrCreate()

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

from pyspark.sql.types import StringType, StructField, StructType, ArrayType, IntegerType
from pyspark.sql.functions import explode

schema = StructType([
    StructField('id', StringType()),
    StructField('name', StringType()),
    StructField('city', ArrayType(StringType()))
])

df1.show(truncate=False)

df2 = df1.withColumn('city', explode('city'))

df2.show(truncate=False)

"""
o/p: 

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

# TODO 2: Write query for below Output
"""
Input :
col_code
red
blue
green

Output :
col1,col2
red, blue
red,green
blue,green
"""
from pyspark.sql.functions import col

data = [('red',), ('blue',), ('green',)]
df = spark.createDataFrame(data, ['col_code'])

ndf = df.alias("df1").join(df.alias("df2"), col("df1.col_code") < col("df2.col_code"))
df.createOrReplaceTempView('ndf')
ndf.show()

"""
o/p:
+--------+--------+
|col_code|col_code|
+--------+--------+
|    blue|     red|
|   green|     red|
|    blue|   green|
+--------+--------+
"""

