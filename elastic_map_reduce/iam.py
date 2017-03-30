from troposphere import Ref, Join
import troposphere.iam as iam
from awacs import aws, sts

from magicdict import MagicDict

class IAM(MagicDict):
    def __init__(self, parameters, buckets):
        super(IAM, self).__init__()
        
        
	self.emr_service_role = iam.Role(
	    "EMRServiceRole",
            Path="/",
            ManagedPolicyArns=[
                "arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole",
            ],
	    AssumeRolePolicyDocument=aws.Policy(
	        Statement=[
                    aws.Statement(
                        Effect=aws.Allow,
                        Action=[sts.AssumeRole],
                        Principal=aws.Principal(
                            "Service", ["elasticmapreduce.amazonaws.com"]
                        )
                    ),
                    aws.Statement(
                        Effect=aws.Allow,
                        Action=[sts.AssumeRole],
                        Principal=aws.Principal(
                            "Service", ["s3.amazonaws.com"]
                        )
                    )
                ]
            )
        )

#	self.emr_service_role = iam.Role(
#	    'EMRServiceRole',
#	    AssumeRolePolicyDocument={
#	        "Statement": [{
#	            "Effect": "Allow",
#	            "Principal": {
#	                "Service": [
#	                    "elasticmapreduce.amazonaws.com"
#	                ]
#	            },
#	            "Action": ["sts:AssumeRole"]
#	        }]
#	    },
#	    ManagedPolicyArns=[
#	        'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceRole'
#	    ]
#	)
	
	self.emr_job_flow_role = iam.Role(
	    "EMRJobFlowRole",
	    AssumeRolePolicyDocument={
	        "Statement": [{
	            "Effect": "Allow",
	            "Principal": {
	                "Service": [
	                    "ec2.amazonaws.com"
	                ]
	            },
	            "Action": ["sts:AssumeRole"]
	        }]
	    },
	    ManagedPolicyArns=[
	        'arn:aws:iam::aws:policy/service-role/AmazonElasticMapReduceforEC2Role'
	    ]
	)
	
	self.emr_instance_profile = iam.InstanceProfile(
	    "EMRInstanceProfile",
	    Roles=[Ref(self.emr_job_flow_role)]
	)

