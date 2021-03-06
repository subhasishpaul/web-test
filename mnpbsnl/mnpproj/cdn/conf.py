import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='sp-k8s-django'
AWS_S3_ENDPOINT_URL="https://sgp1.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION="https://sp-k8s-django.sgp1.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "mnpproj.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "mnpproj.cdn.backends.StaticRootS3BotoStorage"
