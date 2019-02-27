import boto3
import progressbar

# The region the S3 bucket exists in
REGION = 'us-east-1'

# The S3 bucket that contains glacier objects
BUCKET = '<your-bucket-name>'

# Set this to a folder or a full path. Everything under this folder will be restored.
FOLDER = '<your-folder-path>'

# Days for restore to remain active
RESTORE_DAYS = 30

""" DO NOT EDIT BELOW THIS LINE """

client = boto3.client('s3', region_name=REGION)

current = None
allObjects = client.list_objects(
  Bucket=BUCKET,
  Prefix=FOLDER
)['Contents']

while True:
  last = allObjects[-1]['Key']
  objects = client.list_objects(
    Bucket=BUCKET,
    Prefix=FOLDER,
    Marker=last
  )
  if ('Contents' not in objects):
    break
  current = objects['Contents'][-1]['Key']

  print('Retrieved %s objects...' % (len(allObjects)))

  if (last == current):
    break
  else:
    allObjects = allObjects + objects['Contents']

print('Retrieved %s objects...' % (len(allObjects)))

i = 0
with progressbar.ProgressBar(max_value=len(allObjects), redirect_stdout=True) as bar:
  for obj in allObjects:
    restoreRequest = {
      'Days': RESTORE_DAYS
    }

    print('Restore: %s' % (obj['Key']))
    try:
      response = client.restore_object(Bucket=BUCKET, Key=obj['Key'], RestoreRequest=restoreRequest)
      print('Response: %s' % (response['ResponseMetadata']['HTTPStatusCode'])) # 200 is good
    except:
      print('Restore failed or already in progress...')
    i += 1
    bar.update(i)
