import boto3
import botocore
import paramiko
import time
from botocore.exceptions import ClientError
from boto3 import client


#Describing all of the instances 
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)


# #Run ec2 instances
client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-099a8245f5daa82bf',
                    InstanceType='t2.micro',
                    MinCount = 1,
                    MaxCount = 1)


instance_id = resp['Instances'][0]['InstanceId']
print(instance_id)

# time.sleep(120)

# #Stop or Terminate instances
ids = [instance_id]
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).stop() 

# ec2.instances.filter(InstanceIds = ids).terminate() 


#Create Security Group
# ec2 = boto3.client('ec2')

# response = ec2.describe_vpcs()
# #print(response)
# vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

# try:
#     response = ec2.create_security_group(GroupName='mySecurityGroup',
#                                          Description='Security group for ec2 instances',
#                                          VpcId=vpc_id)
#     security_group_id = response['GroupId']
#     print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

#     data = ec2.authorize_security_group_ingress(
#         GroupId=security_group_id,
#         IpPermissions=[
#             {'IpProtocol': 'tcp',
#              'FromPort': 80,
#              'ToPort': 80,
#              'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
#             {'IpProtocol': 'tcp',
#              'FromPort': 22,
#              'ToPort': 22,
#              'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
#         ])
#     print('Ingress Successfully Set %s' % data)
# except ClientError as e:
#     print(e)


#descibe security group
# ec2 = boto3.client('ec2')

# try:
#     response = ec2.describe_security_groups(GroupIds=['sg-0e41a4768197fa86a'])
#     print(response)
# except ClientError as e:
#     print(e)


#ec2 = boto3.resource('ec2')
# for instance in ec2.instances.all():
#     print (instance.id , instance.state, instance.placement, instance.publicipaddress)

# ec2 = boto3.client('ec2')
# response = ec2.describe_instances()
# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         # This sample print will output entire Dictionary object
#         # print(instance)
#         # This will print will output the value of the Dictionary key 'InstanceId'
#         print(instance['InstanceId'], instance["Placement"]["AvailabilityZone"], instance["PublicIpAddress"])


#Create key pair
# ec2 = boto3.client('ec2')
# keypair = ec2.create_key_pair(KeyName='foo',)
# print(keypair)
# pemkey = keypair['KeyMaterial']
# print(pemkey)
# output = open('foo.pem', 'w')
# output.write(str(pemkey))
# output.close()

#Describe Key pair
# response = ec2.describe_key_pairs(
#     KeyNames=[
#         'foo',
#     ],
# )
# print(response)
# response.key_material

#Delete Key Pair
# response = ec2.delete_key_pair(
#     KeyName='foo',
# )
# print(response)

# SSH into EC2 instance
# key = paramiko.RSAKey.from_private_key_file("C:/Users/guruz/Downloads/test.pem")
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect(hostname='34.245.34.10', username="ec2-user", pkey=key)
# stdin, stdout, stderr = client.exec_command('pwd')
# print(stdout.read())
# client.close()

#Alternatively, use Putty to open an SSH client and then type "ssh -i "foo.pem" ec2-user@ec2-54-171-237-184.eu-west-1.compute.amazonaws.com" on cmd