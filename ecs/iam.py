from troposphere import iam, Join, Ref, AWS_STACK_NAME
from awacs import aws
from awacs import sts

from magicdict import MagicDict

class IAM(MagicDict):
    def __init__(self, parameters):
        super(IAM, self).__init__()

        self.InstanceRole = iam.Role(
            "InstanceRole",
            AssumeRolePolicyDocument=aws.Policy(
                Statement=[
                    aws.Statement(
                        Effect=aws.Allow,
                        Action=[sts.AssumeRole],
                        Principal=aws.Principal("Service", ["ec2.amazonaws.com"])
                    )
                ]
            )
        )

        self.InstanceProfile = iam.InstanceProfile(
            "InstanceProfile",
            Path="/",
            Roles=[self.InstanceRole]
        )
	
	self.InstancePolicy = iam.ManagedPolicy(
            "InstancePolicy",
            Description="",
            Roles=[Ref(self.InstanceRole)],
            PolicyDocument=aws.Policy(
                Statement=[
                    aws.Statement(
                        Action=[
                            aws.Action("ecs", "CreateCluster"),
                            aws.Action("ecs", "DeregisterContainerInstance"),
                            aws.Action("ecs", "DiscoverPollEndpoint"),
                            aws.Action("ecs", "Poll"),
                            aws.Action("ecs", "RegisterContainerInstance"),
                            aws.Action("ecs", "StartTelemetrySession"),
                            aws.Action("ecs", "Submit*"),
                            aws.Action("ecs", "GetAuthorizationToken"),
                            aws.Action("ecs", "BatchCheckLayerAvailability"),
                            aws.Action("ecs", "GetDownloadUrlForLayer"),
                            aws.Action("ecs", "BatchGetImage"),
                            aws.Action("logs", "CreateLogStream"),
                            aws.Action("logs", "PutLogEvents"),
                            aws.Action("sqs", "*"),
                            aws.Action("s3", "*")
                        ],
                        Effect=aws.Allow,
                    )
                ]
            )
        )	
