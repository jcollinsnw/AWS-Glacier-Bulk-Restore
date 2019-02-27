# AWS Glacier Bulk Restore

## Installation

Run the install script, make sure you have Python and Pip installed on your machine.

Open your terminal application and navigate to the AGBR directory. Run this command:

```bash
./install.sh
```

## Setup
1. Set up your AWS environment and the boto3 library by following [this guide.](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)


2. Currently the AGBR script just uses global variables for configuration. Edit the variables at the top of the script according to your requirements.

	```python
	# The region the S3 bucket 	exists in
	REGION = 'us-east-1'

	# The S3 bucket that contains glacier objects
	BUCKET = '<your-bucket-name-here>'

	# Set this to a folder or a full path. Everything under this folder will be restored.
	FOLDER = '<your-folder-path>'

	# Days for restore to remain 	active
	RESTORE_DAYS = 30
	```

3. Run the script.

	```bash
	python glacerRestore.py
	```
	
## Notes
* The restore process can take quite some time. The progress bar will give an estimate but it may not be entirely accurate.
* This only initiates restoring, actually performing file restoration is handled by Amazon and will take even longer than this script.
