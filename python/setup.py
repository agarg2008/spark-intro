# Original source: http://renien.github.io/blog/accessing-pyspark-pycharm/

import os
import sys

# Path for spark source folder
os.environ['SPARK_HOME'] = "/Users/User1/Developer/spark-1.3.0-bin-hadoop2.4"

# Append pyspark to Python Path
sys.path.append("/Users/User1/Developer/spark-1.3.0-bin-hadoop2.4/python/")

try:
    from pyspark import SparkContext
    from pyspark import SparkConf

    print("loaded spark")

    sc = SparkContext('local')

except ImportError as e:
    print
    "Can not import Spark Modules", e
sys.exit(1)