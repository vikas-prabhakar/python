#!/usr/bin/python
import boto3
import getpass
import pprint
import sys
import os

test1=[]
profile=str(input("AWS profile:"))
token_duration=int(input("Allowed values between 900 (15 minutes) - 43200 (12 hours) sec: "))

if token_duration < 900 or token_duration > 43200:
  print ("Kindly enter time duration between 900 (15 minutes) - 43200 (12 hours)")
  sys.exit()

user=input("AWS username:")
mfa_code=getpass.getpass(prompt="Enter MFA code")
def sts_token(user,token_duration,mfa_code,profile):
  session = boto3.Session(profile_name=profile)
  sts_client=session.client('sts')
  iam = session.client('iam')
  user_detail=iam.list_mfa_devices(UserName=user)['MFADevices']
  mfa=(next(iter(user_detail))['SerialNumber'])

  temp_credential=sts_client.get_session_token(DurationSeconds=token_duration,SerialNumber=mfa,TokenCode=mfa_code)
  return temp_credential


token=sts_token(user,token_duration,mfa_code,profile)
test1.append(token['Credentials']['AccessKeyId'])
test1.append(token['Credentials']['SecretAccessKey'])
test1.append(token['Credentials']['SessionToken'])

sys.stdout=open("/tmp/session.sh","w")
print(f"export AWS_ACCESS_KEY_ID={token['Credentials']['AccessKeyId']}")
print(f"export AWS_SECRET_ACCESS_KEY={token['Credentials']['SecretAccessKey']}")
print(f"export AWS_SESSION_TOKEN={token['Credentials']['SessionToken']}")
sys.stdout.close()
