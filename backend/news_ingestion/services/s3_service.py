import boto3


def upload_file_to_s3(file_name, bucket_name, object_name):
    s3 = boto3.client("s3")

    s3.upload_file(
        file_name,
        bucket_name,
        object_name
    )

    print(f"Uploaded {file_name} to {bucket_name}/{object_name}")
