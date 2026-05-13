import boto3

# ===== CONFIGURATION =====
BUCKET_NAME = "aws-web-host-20260422-xyz"
FILE_NAME = "index.html"
OBJECT_NAME = "index.html"

# ===== CREATE S3 CLIENT =====
s3 = boto3.client('s3')

# ===== UPLOAD FILE =====
try:
    s3.upload_file(
        FILE_NAME,
        BUCKET_NAME,
        OBJECT_NAME,
        ExtraArgs={'ContentType': 'text/html'}
    )
    print("✅ Upload successful!")
    print("File uploaded to S3 bucket:", BUCKET_NAME)

except Exception as e:
    print("❌ Upload failed!")
    print("Error:", e)