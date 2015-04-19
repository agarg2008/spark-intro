__author__ = 'ankit'

from pyspark import SparkContext
from pyspark import SparkConf


def word_count():
    sc = SparkContext('local')

    data = sc.parallelize(['a', 'a1', 'a2', 'b', 'b', 'a1'])
    output = data.flatMap(lambda line: line.split(" ")) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda a, b: a + b) \
        .collect()

    for tuple in output:
        print tuple

if __name__ == "__main__":
    word_count()