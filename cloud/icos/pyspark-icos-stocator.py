#%%
# Write a Spark (pyspark) DataFrame as CSV file into an IBM Cloud Object Store (COS) bucket via Stocator.
from pyspark.sql import SparkSession

stocator_jar = '/path/to/stocator-1.1.2-SNAPSHOT-IBM-SDK.jar'
cos_instance_name = '<myCosIntanceName>'
bucket_name = '<bucketName>'
s3_region = '<region>'
cos_iam_api_key = '*******'
iam_servicce_id = 'crn:v1:bluemix:public:iam-identity::<****************>'

spark_builder = (
    SparkSession
        .builder
        .appName('test_app'))

spark_builder.config('spark.driver.extraClassPath', stocator_jar)
spark_builder.config('spark.executor.extraClassPath', stocator_jar)
spark_builder.config(f"fs.cos.{cos_instance_name}.iam.api.key", cos_iam_api_key)
spark_builder.config(f"fs.cos.{cos_instance_name}.endpoint", f"s3.{s3_region}.cloud-object-storage.appdomain.cloud")
spark_builder.config(f"fs.cos.{cos_instance_name}.iam.service.id", iam_servicce_id)
spark_builder.config("spark.hadoop.fs.stocator.scheme.list", "cos")
spark_builder.config("spark.hadoop.fs.cos.impl", "com.ibm.stocator.fs.ObjectStoreFileSystem")
spark_builder.config("fs.stocator.cos.impl", "com.ibm.stocator.fs.cos.COSAPIClient")
spark_builder.config("fs.stocator.cos.scheme", "cos")

spark_sess = spark_builder.getOrCreate()

dataset = spark_sess.range(1, 10)
dataset = dataset.withColumnRenamed('id', 'user_idx')

dataset.repartition(1).write.csv(
    f'cos://{bucket_name}.{cos_instance_name}/test.csv',
    mode='overwrite',
    header=True)

spark_sess.stop()
print('done!')
