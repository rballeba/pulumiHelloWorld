"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('pulumi-bucket', website=s3.BucketWebsiteArgs(index_document="index.html"))

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Creating site index.html
bucketObject = s3.BucketObject('index.html', acl='public-read', content_type='text/html', bucket=bucket, content=open('staticsite/index.html').read())

# Export the endpoint
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))
