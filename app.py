import Linux
import test #added thisnew
# Initialize EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')  # Change region as needed

# Instance ID to stop
instance_id = 'i-0123456789abcdef0'  # Replace with your EC2 instance ID

# Stop the instance
response = ec2.stop_instances(InstanceIds=[instance_id])

# Print response
print("Stopping instance:", instance_id)
print(response)
