import boto3
import os 

class AmazonS3:
    def upload_file(self, filepath):
        s3 = boto3.client(
            service_name='s3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
            aws_secret_access_key=os.environ.get('AWS_SECRET_KEY'))
        bucket_name = os.environ.get('AWS_BUCKET_NAME')
        file_name = filepath.split('/')[-1]
        print(bucket_name)
        s3.upload_file(filepath, bucket_name, file_name)
        # s3.put_object_acl(Bucket=bucket_name, Key=file_name, ACL="public-read")
        public_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        return public_url



 