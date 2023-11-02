import boto3

BUCKET_NAME = None

class AmazonS3:
    def upload_file(self, filepath):
        s3 = boto3.client("s3")
        bucket_name = BUCKET_NAME
        file_name = filepath.split('/')[-1]
        s3.upload_file(filepath, bucket_name, file_name)
        s3.put_object_acl(Bucket=bucket_name, Key=file_name, ACL="public-read")
        public_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}"
        return public_url



 