import boto3
import botocore
from keys_aws import access_key
from keys_aws import private_key

session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=private_key)
region = 'sa-east-1'


def get_files():
    BUCKET = 'inputbucketslide'

    s3 = session.resource('s3')

    input_bucket = s3.Bucket(BUCKET)

    for my_bucket_object in input_bucket.objects.filter(Prefix='word/'):
        KEY = my_bucket_object.key
    try:
        save_path = '/home/ec2-user/input_file/' + KEY
        input_bucket.download_file(Key=KEY, Filename=save_path)
    except Exception as err:
        print(err)
        # add notification of error


def clean_bucket():
    BUCKET = 'inputbucketslide'

    input_bucket = session.client('s3')

    for my_bucket_object in input_bucket.objects.all():
        KEY = my_bucket_object.key
        input_bucket.delete_object(Bucket=BUCKET, Key=KEY)


def kill_ec2():
    client = session.client('ec2', region_name=region)
    try:
        client.stop_instances(
            InstanceIds=[
                'i-07151776ee1c83765',
            ],
            DryRun=False
        )
    except Exception as err:
        print(err)


def send_ppt():
    BUCKET = 'slide-output-bucket'
    s3 = session.resource('s3')
    input_bucket = s3.Bucket(BUCKET)
    KEY = "presentation.pptx"
    save_path = '/home/ec2-user/output/' + KEY
    input_bucket.upload_file(Key=KEY, Filename=save_path)


def send_wordx(path):
    BUCKET = 'inputbucketslide'
    s3 = session.resource('s3')
    input_bucket = s3.Bucket(BUCKET)
    KEY = "word/input.wordx"
    input_bucket.upload_file(Key=KEY, Filename=path)


def send_email_address(email):
    text_file = open("email.txt", "w")
    text_file.write(email)
    text_file.close()

    BUCKET = 'inputbucketslide'
    s3 = session.resource('s3')
    input_bucket = s3.Bucket(BUCKET)
    KEY = 'receiver/email.txt'
    input_bucket.upload_file(Key=KEY, Filename="email.txt")
