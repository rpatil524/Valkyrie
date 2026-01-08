"""S3 upload utilities for the tracker service."""

import boto3

S3_BUCKET_NAME = "agentic-harness"


def upload_to_s3(file_content: bytes, s3_key: str) -> None:
    """
    Upload file content to S3.

    Args:
        file_content: File content as bytes
        s3_key: S3 object key (path in bucket)

    Raises:
        ValueError: If AWS credentials are not configured or bucket doesn't exist
    """
    bucket_name = S3_BUCKET_NAME

    # TODO: Error handling?
    s3_client = boto3.client("s3")
    s3_client.put_object(Bucket=bucket_name, Key=s3_key, Body=file_content)
