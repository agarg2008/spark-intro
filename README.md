# spark-intro
This is an attempt to list down resources to make it easier to engage with [Spark](https://spark.apache.org/ "Spark Homepage").

You may ask why do I need to learn just another framework for 'Big Data' processing when I know Hadoop? To quote from its [Wikipedia entry](http://en.wikipedia.org/wiki/Apache_Spark) 
>In contrast to Hadoop's two-stage disk-based MapReduce paradigm, Spark's in-memory primitives provide performance up to 100 times faster for certain applications.
 By allowing user programs to load data into a cluster's memory and query it repeatedly, Spark is well suited to machine learning algorithms.

You might find this [video](https://www.youtube.com/watch?v=qLvLg-sqxKc "NIPS 2011 : Spark: In-Memory Cluster ") 
interesting. I found [lecture slides](http://hssl.cs.jhu.edu/wiki/lib/exe/fetch.php?media=randal:teach:cs420:lec12.spark.pdf)
 (slides 1-9 and 16-19) by Prof. Randal Burns very useful for understanding Spark concepts which lead to such speedup.

---

Spark requires a cluster manager and a distributed storage system. It has its own native Spark cluster and it can be used with Hadoop YARN cluster as well. 
Instruction on how to use a YARN cluster on AWS can be accessed [here](http://spark.apache.org/docs/latest/ec2-scripts.html).

---

Python programming guide is accessible [here](https://spark.apache.org/docs/latest/programming-guide.html). Explanations of 
various transformations and actions supported is also documented there. Spark supports python 2.7 (they have recently merged python 3 support, so it might become available soon).

I have added some sample program under __python__ folder. A more comprehensive set of examples is accessible [here](https://github.com/apache/spark/tree/master/examples/src/main/python).
 
To work and test directly in an IDE like __PyCharm__, you can either add __pyspark__ module as 
  a source folder in your project or you can set appropriate environment variable (refer to __setup.py__).
 
To run a program on your local machine you can execute :
```/Users/User1/Developer/spark-1.3.0-bin-hadoop2.4/bin/spark-submit wordcount.py```

