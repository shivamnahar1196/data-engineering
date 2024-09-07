# Spark Theory

[Playlist link](https://www.youtube.com/watch?v=FNMoeE849Yw&list=PLTsNSGeIpGnGkpfKMf7ilFmzfx6AjMKyT)

----
[Lec-1]

1. Spark: 
    - It is a unified computing engine and set of libraries for parallel processing data on computer cluster.
    - It doen't have it's own storage. Can connect with diff sources: HDFS, JDBC/ODBC, S3, etc.
    - It works as Master-Slave architecture.

[Lec-2]
	
1. Big data: 
  		- Volume | Variety(Structured, sem-struct, un-struct) | Velocity
  		- DW (ETL)
  		- Data Lake (ELT)

2. Issues:
		  - Processing(distributed) & Storage	(cloud)

[Lec-3]

1. Hadoop Vs Spark:
  - Misconceptions:
    - Hadoop is a db. | Spark is 100 times faster. | Spark processes in RAM and Hadoop doesn't.

  - Differences:
    A. Performance:
      - H : slower than spark. coz it writes the data to disk and read it again from the disk to in-memory.
      - S	: It is faster as spark does all the computation in memory.

    B. Processing:
      - H : Batch
      - S : Batch & Streaming

    C. Usage:
      - H : Difficult to use. Hence, Hive was used.
      - S : Easy to use with high level and low level API's.

    D. Security:
      - H : Uses kerberos authetication and ACL (Folder level access) Authorzation. More secured then Spark.
      - S : doesn't have solid security feature. It leverages HDFS (ACL Security) & YARN (kerberos).  

    E. Fault Tolerance: 
      - H : It stores data in blocks and has replication factor to handle failure.
      - S : uses DAG to provide Fault tolerance.
[Lec-4]
	
1. Spark Ecosystem:
  - Spark Core (Low level API - python, R, JAVA, Scala) [RDD] + Spark Engine
  - Libraries (High level API - ML lib, Spark SQL, Spark Streaming, GraphX) [Dataframe/Dataset API]
[Lec-5]
	
1. Spark Architecture:
  - Master: Resource Manager [YARN, Mesos, Kubernetes, Standalone]
  - Worker: Node Manager

    - Container : It's a container created by driver known as application master. 
                  (written in Python, Java/Scala)
      Python - Pyaspark | Java/Scala -- JVM main() method is called & this creates Application driver.
      Spark Core ---> Java Wrapper ---> Python Wrapper
      This will create the main method. This will be called the application driver. Now, it will go back 
      to resource manager to create executors and cpu core as needed. Then new containers will be created
      equivalent to num of executors i.e., Executor Container.

    - Executor Container:
      - try to use less of user defined function as they required python workers for process execution,
        wherein all the executors have JVM main() method to run on.
 
[Lec-6]
	
1. Transformations and Actions:
  - Tx: Narrow:that doesn't require data movement between partitions. Ex: filter(),union(), select(), map()
      Wide:that require data movement between partitions. Ex: join, groupBy, distinct
  - Actions: count, show, collect, read(), inferSchema
    --> whenever an action is called job is created and data goes to driver.	  
         A pyspark code is called as spark application, which can have multiple jobs in it, equivalent
         to number of actions.
[Lec-7]
	
1. DAG & Lazy Evaluation:
    - Every Job will have it's own DAG. For each action new Job is created.
    - df.explain() -- can show us the final plan made by catalyst optimiser. --> Pyhsical plan
[Lec-8]
	
1. Spark SQL Engine (Catalyst Optimiser):

  - It works in 4 phases: Analysis | Logical Planning (LP) | Physical/Spark Planning (PP) | Code Generation
  - Flow:

  code ---> unresolved logical plan ---> catalog(analysis) ---> Resolved logical plan ---> logical optimisation ---> optimised logical plan ---> physical plan


  catalog: keeps metadata (tables, files, databases)
  physical plan: Multiple PP are created with the LP, then code based optimisation is performed to get the best PP(i.e., RDD)

  - Spark SQL engine is a compiler, it converts our code into Java Bytecode.

[Lec-9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	
1. RDD: Data Structure of Spark |  Fault tolerant | Immutable
  cons: no optimisation done by spark
  pros: helpful in unstructured data API | type safe (it gives error while compile time.)

2. SparkSession & SparkContext

3. Job, Stage, Task, Application:

  - Whenever a job is made it will have minimum of one stage and one task.
  - Application: One spark-submit command creates one application.
  - Job: equivalent to number of actions.
  - Stage: Number of transforamtions took place. (Logical)
  - Task: Actual where the data is performed. (Executor) Equal to number of partitions
  - By default spark creates 200 partitions.

4. Repartition Vs Coalesce	
   R : Evenly distributed but shuffling takes places. Can increase/decrease partition.
   C : Un-Evenly distributed but no shuffling. Can only decrease partition.

5. Spark Joins:

  - Shuffle sort merge join (Onlogn) - first shuflfing then sorting is done. CPU utilisation. Default join by spark.
  - Shuffle hash join : makes hash table out of samll table on the basis of keys and this is in-memory. (O(1))
  - Broadcast hash join		
  - Cartesian Join
  - Broadcast nested loop join (Most costly join)

  Broadcast hash join: 
    - Table < 10mb can be used to Broadcast. Removes Shuffling. 
    - driver broadcasts small data on to the executors.
    - We should define the samll table based on our cluster size.
    - To get the broadcast size: spark.conf.get("spark.sql.autoBroadcastJoinThreshold")
    - To set the broadcast size: spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1) -- this disables it.
    - To increase broadcast size: spark.conf.set("spark.sql.autoBroadcastJoinThreshold", byte value)

6. Driver out of Memory (OOM):
  - This error comes when we perform an action, which has more data then that of driver memory.
  - driver memory is defined as : pyspark --driver-memory 1g 
  - there are two types of memory: 
    spark.driver.memory -- JVM Process
    spark.driver.memory.Overhead (10% or 384mb whichever higher) -- For Non JVM process and container space
  - When we do show only one of the complete partitions go to the driver and 20 records are displayed by default.
  - When collect is used data from all the partitions goes to driver, and if the data size of all partitions
    is greater than driver memory, we will get OOM exceptions. 


  Reasons for OOM:
    - COLLECT()
    - Broadcast process
    - More objects used in the process - when we are using more objects i.e., non-jvm process.

7. Executor out of Memory (OOM):
  - spark.executor.memory
  - spark.executor.memory.Overhead. -- 10%
  - It is a physical memory inside a cluster.
  - When we exceed the total executor size, memoryoverHead we get OOM.

  - Overhead memory usage:
    - used for Non-JVM process.
    - 300-400 MB Used by container.
    - 600-700 MB used by pyspark applications.

  - Executor size must be 1.5 times the reserved memory. 
  - We can spill the data on to the disk, but we won't be able to spill when we do a join suppose and our executor memory pool size is 2.9GB, now the joining makes data skewed and some id join makes data size of around 3gb in this case the data will not able able to spill and hence, we use salting and repartitioning to overcome this issue.

  - Memory manager: Static | Unified (>1.6+)

8. Spark Submit:
  - command line tool which helps us to run spark applications.
    \bin\spark-submit\
      -- master local[5] \   # this is nothing but the cluster we are using (YARN, local, Kubernetes, Mesos)
      -- deploy-mode cluster\ # can be client also
      -- class main-class.scala \. # for java and scala only not used with pyspark
      -- jars file_path \
      -- conf spark.dynamicAllocation.enabled=true \
              -- conf spark.dynamicAllocation.minExecutors=1 \
              -- conf spark.dynamicAllocation.minExecutors=10 \
              -- conf spark.sql.broadcastTimeout=3600 \
              -- conf spark.sql.autoBroadcastJoinThreshold=100000 \
              -- driver-memory 1G \
              -- executor-memory 2G \
              -- num-executors 5 \
              -- executor-cores 2 \
              -- py-files spark-session.py, logging-config.py....
              -- files config.py, .ini, c:/file path

      - Edge node is a place from where we use spark-submit.                        

9. Deployment modes in spark:
  - Edge Node: It is a machine outside cluster that is been bought seperately to connect with spark cluster,
        this is done to control the access of a user and also provide authentication if required.
        This node in turn further connects with cluster manager and then cluster manager performs the work
        further. Hadoop admin helps us to create an edge node. spark bin path gets installed on this.

  Client Mode 								| 					Cluster Mode			

  1.Logs are generated on client machine.     | Logs are generated in std out or std err. Suitable for prod
    Easy to debug.							| workload.

  2. n/w latency is high.						| n/w latency is less.
  3. Driver OOM can be there.					| Driver can go into OOM but chances are less.
  4. Goes away once the edge node server is   | Even if edge server is closed, process still runs.
    disconnected.  							| Gives application_id, to check running logs on Spark UI.

  5. Driver resides on edge node.				| Driver resides on one of the worker node.		


10. AQE in spark:
   - Can optimise the query at run time.
   - It comes into picture when data shuffling is taking place.

  Features:
   - Dynamically coalescing shuffle partitions.
    - If your skewed data is 5 times more than the median and size of the skewed data is greater than 256mb.
    - Data gets coalesced in this from number of partitions so that the partitions size becomes equal.

   - Dynamically switching join startegies.
    - After the transformations has taken place on two tables and the DAG has been created and by default spark uses sort-merge join. Now if we see that after our multiple transforamtion the data size has become
    smaller, spark can read the runtime analytics and change the join to broadcast join. This can only
    be done, if we have AQE enabled.
   - Dynamically optimizing skew Joins.
    - This causes OOM (Salting , aqe - 2 solutions we have.)
    - It will split the partition data of larger partitions and the data from other source so that the join
      can take place between the two.

11. Salting in spark:
    - It is a technique of removing data skewness.


12. Cache & Persist in spark:
    - Cache data gets stored in storage pool of executor. First it tries to store partition in memory and 
      if the partitions are more it stores the data in disk.
    - Both are optimising technique.
    - Cache stores the intermediate result in storage pool executor memory, so that we do not have to read 
      repeatedly from source and we can refer that cached data directly. df.cache()

    - Persist: Takes arguments.	
      - cache is nothing but the wrapper over persist.
      - df.persist(storageLevel)	
        - storageLevel: 
          - MEMORY_ONLY
            : RAM | Accessed in deserialised form | Process fast but high memory utilisation high

          - MEMORY_AND_DISK:
            : First data in RAM then DISK ( in it data stores in serialised form always.)
            : Memory will used intermediate but CPU usage high as data would desrialised.

          - MEMORY_ONLY_SER:
            : RAM(serailise) | save storage | High CPU utilisation.

          - MEMORY_AND_DISK_SER:	
            : In disk data always gets stored in serialised form.

          - DISK_ONLY:
            : disk serialised -- very slow

          - Memory_only_2:
            : 2 X Replicated
      - The storageLevel which uses SER can be used only in Java/Scala but not in python.				

    - To free the data from cache or persist we use df.unpersist()				

13. Dynamic resource allocation:
    - Static & dynamic resource allocation.
    - When we give spark submit command, we need mention the details of dynamic allocation so that spark 
      can free memory and take more memory if required. The parameters to be updated are: 

      --conf spark.dynamicAllocation.enabled=true \
      --conf spark.dynamicAllocation.minExecutors=20 \
      --conf spark.dynamicAllocation.maxExecutors=49 \

    - When we empty the resource with help of dynamic allocation and if we want the resource back, there 
      is a shuffle Tracking option, which keeps the information of shuffle read and write externally,
      so that if in later half of job run if we want more resources it can help us to keep the track of the process.
      --conf spark.shuffleTracking.enabled=true \

    - To increase the number of resources, it waits for sometime, 1sec then it increase the resources in
      two fold i.e., 1 -- 2 -- 4 -- 8 -- 16

    - Resource manager runs the saprk submit command from different user in FIFO mode.
    - On Spark UI it shows as scheduling mode: FIFO.

    - Avoid dynamic allocation with some critical applications use static allocation.  	

13. Dynamic Partition Pruning:
    - Data should be partitioned. | Second table should be broadcasted. (Conditions for DPP)
    - It's an optimisation technique, which helps to update filter condition at run time.
    - Enabled by defualt.
    - .conifg("spark.sql.optimizer.dynamicPartitionPruning.enabled", "false")


