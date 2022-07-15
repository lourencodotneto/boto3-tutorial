import boto3
import json
import csv
import requests


exportfilepath = "/home/ec2-user/boto3-tutorial/iam/Regions_Export_Output_14072022.csv"
exportfilepath1 = "/home/ec2-user/boto3-tutorial/iam/Availability_Zones_Export_Output_14072022.csv"


# Call API.
headers = "Accept: application/json, text/plain, */*"

print("--------------------------S-T-A-R-T iam code-------------------------------")

# Create IAM client
iam = boto3.client('iam')

# List users with the paginator interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)

print("\n")
print("------------------------E-N-D iam code-------------------------------------")

print("\n")
print("\n")


ec2 = boto3.resource('ec2')
myinstance = ec2.Instance('i-0d1ac03b5c5d2fd9f')

print('myinstance.image_id: ', myinstance.image_id)



print('myinstance.ami_launch_index', myinstance.ami_launch_index)
print('myinstance.architecture', myinstance.architecture)
print('myinstance.block_device_mappings', myinstance.block_device_mappings)
print('myinstance.boot_mode', myinstance.boot_mode)
print('myinstance.capacity_reservation_id', myinstance.capacity_reservation_id)
print('myinstance.capacity_reservation_specification', myinstance.capacity_reservation_specification)
print('myinstance.client_token', myinstance.client_token)
print('myinstance.cpu_options', myinstance.cpu_options)
print('myinstance.ebs_optimized', myinstance.ebs_optimized)
print('myinstance.elastic_gpu_associations', myinstance.elastic_gpu_associations)
print('myinstance.elastic_inference_accelerator_associations', myinstance.elastic_inference_accelerator_associations)
print('myinstance.ena_support', myinstance.ena_support)
print('myinstance.enclave_options', myinstance.enclave_options)
print('myinstance.hibernation_options', myinstance.hibernation_options)
print('myinstance.hypervisor', myinstance.hypervisor)
print('myinstance.iam_instance_profile', myinstance.iam_instance_profile)
print('myinstance.image_id', myinstance.image_id)
print('myinstance.instance_id', myinstance.instance_id)
print('myinstance.instance_lifecycle', myinstance.instance_lifecycle)
print('myinstance.instance_type', myinstance.instance_type)

print('myinstance.kernel_id', myinstance.kernel_id)
print('myinstance.key_name', myinstance.key_name)
print('myinstance.launch_time', myinstance.launch_time)
print('myinstance.licenses', myinstance.licenses)

print('myinstance.metadata_options', myinstance.metadata_options)
print('myinstance.monitoring', myinstance.monitoring)
print('myinstance.network_interfaces_attribute', myinstance.network_interfaces_attribute)
print('myinstance.outpost_arn', myinstance.outpost_arn)
print('myinstance.placement', myinstance.placement)
print('myinstance.platform', myinstance.platform)

print('myinstance.private_dns_name', myinstance.private_dns_name)

print('myinstance.private_ip_address', myinstance.private_ip_address)
print('myinstance.product_codes', myinstance.product_codes)
print('myinstance.public_dns_name', myinstance.public_dns_name)
print('myinstance.public_ip_address', myinstance.public_ip_address)
print('myinstance.ramdisk_id', myinstance.ramdisk_id)
print('myinstance.root_device_name', myinstance.root_device_name)
print('myinstance.root_device_type', myinstance.root_device_type)
print('myinstance.security_groups', myinstance.security_groups)
print('myinstance.source_dest_check', myinstance.source_dest_check)
print('myinstance.spot_instance_request_id', myinstance.spot_instance_request_id)
print('myinstance.sriov_net_support', myinstance.sriov_net_support)
print('myinstance.state', myinstance.state)
print('myinstance.state_reason', myinstance.state_reason)
print('myinstance.state_transition_reason', myinstance.state_transition_reason)
print('myinstance.subnet_id', myinstance.subnet_id)
print('myinstance.tags', myinstance.tags)



print('myinstance.virtualization_type', myinstance.virtualization_type)
print('myinstance.vpc_id', myinstance.vpc_id)




myimage = ec2.Image(myinstance.image_id)


print('myimage.architecture', myimage.architecture)
print('myimage.block_device_mappings', myimage.block_device_mappings)
print('myimage.boot_mode', myimage.boot_mode)
print('myimage.creation_date', myimage.creation_date)
print('myimage.deprecation_time', myimage.deprecation_time)
print('myimage.description', myimage.description)
print('myimage.ena_support', myimage.ena_support)
print('myimage.hypervisor', myimage.hypervisor)
print('myimage.image_id', myimage.image_id)
print('myimage.image_location', myimage.image_location)
print('myimage.image_owner_alias', myimage.image_owner_alias)
print('myimage.image_type', myimage.image_type)
print('myimage.kernel_id', myimage.kernel_id)
print('myimage.name', myimage.name)
print('myimage.owner_id', myimage.owner_id)
print('myimage.platform', myimage.platform)
print('myimage.platform_details', myimage.platform_details)
print('myimage.product_codes', myimage.product_codes)
print('myimage.public', myimage.public)
print('myimage.ramdisk_id', myimage.ramdisk_id)
print('myimage.root_device_name', myimage.root_device_name)
print('myimage.root_device_type', myimage.root_device_type)
print('myimage.sriov_net_support', myimage.sriov_net_support)
print('myimage.state', myimage.state)
print('myimage.state_reason', myimage.state_reason)
print('myimage.tags', myimage.tags)

print('myimage.virtualization_type', myimage.virtualization_type)

# class EC2.Vpc(id)

myvpc = ec2.Vpc(myinstance.vpc_id)

# These are the resource's available attributtes:

print('myvpc.cidr_block', myvpc.cidr_block)

#print('myvpc.cidr_blocks [JSON]: ', json.dumps(myvp.cidr_block))

print("\n")


print('myvpc.cidr_block_association_set', myvpc.cidr_block_association_set)
print('myvpc.cidr_blocks_association_set [JSON]: ', json.dumps(myvpc.cidr_block_association_set))

print("\n")



print('myvpc.dhcp_options_id', myvpc.dhcp_options_id)
print('myvpc.instance_tenancy', myvpc.instance_tenancy)
print('myvpc.ipv6_cidr_block_association_set', myvpc.ipv6_cidr_block_association_set)


print('myvpc.is_default', myvpc.is_default)
print('myvpc.owner_id', myvpc.owner_id)
print('myvpc.state', myvpc.state)
print('myvpc.tags', myvpc.tags)
print('myvpc.vpc_id', myvpc.vpc_id)


# Let's use Amazon S3


print("let's use S3 - start+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

s3 = boto3.resource('s3')

#print out bucket names

for bucket in s3.buckets.all():
    print('bucket.name: ', bucket.name)


my_bucket_1 = "elasticbeanstalk-us-east-1-741213953240"
my_bucket_2 = "elasticbeanstalk-us-west-2-741213953240"

bucket1 = s3.Bucket(my_bucket_1)
for obj in bucket1.objects.all():
    print("objects in bucket_1", obj.key)

bucket2 = s3.Bucket(my_bucket_2)
for obj in bucket2.objects.all():
    print("objects in bucket_2", obj.key)


print("\n")

print (" S-T-A-R-T ")

print("\n")

client = boto3.client('s3')
response = client.list_buckets()

print("\n")



# Load JSON data.
# json_loads is a Python dictionary


print('Buckets', response['Buckets'])


# information_loads = json_loads

jsondata3 = response['Buckets']
jsondata2 = response



print("\n")

print('jsondata3 [Python]: \n', jsondata3)

print('\n')
print('jsondata2 [Python]: \n', jsondata2)


print("\n")

print("\n")

print('response: ', response)


print("\n")


#*******************************************************************************
# ************ Start Converting from Python to JSON " json.dumps " "************
#*******************************************************************************




#*******************************************************************************
# ************ End Converting from Python to JSON " json.dumps " "**************
#*******************************************************************************

print (" E-N-D ")

print("\n")



print("let's use S3 - end +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# Start -  client describe account attributes

client = boto3.client('ec2')

response = client.describe_account_attributes(
        AttributeNames=['supported-platforms', 'default-vpc', 'vpc-max-security-groups-per-interface', 'max-elastic-ips', 'vpc-max-elastic-ips'],
        
                
)

print('Account Attributes [Python]: ', response['AccountAttributes'])

print("\n")



response = client.describe_addresses(
        Filters=[
            {
                'Name': 'private-ip-address',
                'Values': [
                    '172.31.91.247',
                    ]
                },
            ],
        DryRun=False,
        
        
    
        )
print('Addresses [Python]: ', response['Addresses'])

print("\n")



response = client.describe_availability_zones(
    Filters=[
        {
            'Name': 'region-name',
            'Values': [
                'us-east-1',
            ]
        },
    ],
    
)


print('Availability Zones[Python]: ', response['AvailabilityZones'])

print("\n")


response = client.describe_key_pairs(
    Filters=[
        {
            'Name': 'key-name',
            'Values': [
                'ldn_keypair_us-east-1_rsa_putty',
            ]
        },
        

        ],
        DryRun=False
        )



print('KeyPairs [Python]: ', response['KeyPairs'])

print("\n")



waiter = client.get_waiter('security_group_exists')
waiter.wait(
    Filters=[
        {
            'Name': 'group-name',
            'Values': [
                'CertBookL',
            ]
        },
    ],
    
      
    
    WaiterConfig={
        'Delay': 20,
        'MaxAttempts': 10
    }
)
        


# End -  client describe account attributes





ec2 = boto3.client('ec2')

# Retrieves all regions/endpoints that work with EC2
response = ec2.describe_regions()

print('Regions [PYTHON]: ', response['Regions'])


print("\n")


#*******************************************************************************
# ************ Start Converting from Python to JSON " json.dumps " "************
#*******************************************************************************

print('Regions [JSON]: ', json.dumps(response['Regions']))

print("\n")

jsondata1 = (json.dumps(response['Regions']))

print('\n')
print('jsondata1 [JSON]: ', jsondata1)


#*******************************************************************************
# ************ End Converting from Python to JSON " json.dumps " "**************
#*******************************************************************************
        

#*******************************************************************************
# ************ Start Converting from JSON to Python " json.loads "  ************
#*******************************************************************************


jsondata2 = json.loads(jsondata1)

print('\n')
print('jsondata2 [Python]: ', jsondata2)




print('\n')


#*******************************************************************************
# ************ End Converting from JSON to Python " json.loads "  **************
#*******************************************************************************

# jsondata4 = (json.dumps((jsondata3), sort_keys=False, indent=4))
jsondata3 = (json.dumps((jsondata2)))

# The result is a JSON string
print('\n')
print('jsondata3 [JSON]: ', jsondata3)
jsondata4 = json.loads(jsondata3)

print('\n')
print('jsondata4 [Python]: ', jsondata4)

print('\n')



# Open CSV file for writing.
csv_file = open(exportfilepath, 'w')



# create the CSV Writer Object.
csv_writer = csv.writer(csv_file)



# Counter variable used for writing
# headers to the CSV file
count = 0

# Process JSON data -> CSV
for info in jsondata4:
    
    if count == 0:

        # Writing headers of CSV
        
        header = info.keys()
        csv_writer.writerow(header)
        count += 1

    #Writing data of CSV file
    csv_writer.writerow(info.values())

# Close file
csv_file.close()


# Retrieves availability zones only for region of the ec2 object

response = ec2.describe_availability_zones()
# print('Availability Zones: ', response['AvailabilityZones'])

# print("\n")

print('Availability Zones [JSON]: ', json.dumps(response['AvailabilityZones']))





print("\n")

jsondata_AV1 = (json.dumps(response['AvailabilityZones']))

print('\n')
print('jsondata_AV1 [JSON]: ', jsondata_AV1)


#*******************************************************************************
# ************ End Converting from Python to JSON " json.dumps " "**************
#*******************************************************************************


#*******************************************************************************
# ************ Start Converting from JSON to Python " json.loads "  ************
#*******************************************************************************


jsondata_AV2 = json.loads(jsondata_AV1)

print('\n')
print('jsondata2 [Python]: ', jsondata_AV2)




print('\n')


#*******************************************************************************
# ************ End Converting from JSON to Python " json.loads "  **************
#*******************************************************************************

# jsondata4 = (json.dumps((jsondata3), sort_keys=False, indent=4))
jsondata_AV3 = (json.dumps((jsondata_AV2)))

# The result is a JSON string
print('\n')
print('jsondata_AV3 [JSON]: ', jsondata_AV3)
jsondata_AV4 = json.loads(jsondata_AV3)

print('\n')
print('jsondata_AV4 [Python]: ', jsondata_AV4)

print('\n')





# Open CSV file for writing.
csv_file_1 = open(exportfilepath1, 'w')


# create the CSV Writer Object.
csv_writer_1 = csv.writer(csv_file_1)



# Counter variable used for writing
# headers to the CSV file
count = 0

# Process JSON data -> CSV
for info in jsondata_AV4:

    if count == 0:

        # Writing headers of CSV

        header = info.keys()
        csv_writer_1.writerow(header)
        count += 1

    #Writing data of CSV file
    csv_writer_1.writerow(info.values())

# Close file
csv_file_1.close()


