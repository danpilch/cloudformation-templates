from troposphere import AWS_STACK_NAME, FindInMap, GetAtt, ImportValue, Join, Ref, Tags
from troposphere import ec2, elasticloadbalancing, route53

from magicdict import MagicDict


class EC2(MagicDict):
    def __init__(self, parameters):
        super(EC2, self).__init__()

        self.AWSInstance = ec2.Instance(
            "AWSInstance",
            Tags=Tags(
                    Name=AWS_STACK_NAME
            ),
            SecurityGroupIds=[
                "sg-1a2b217d"
            ],
            SubnetId="subnet-eafed59c",
            ImageId=Ref(parameters.InstanceImage.title),
            BlockDeviceMappings=[
                ec2.BlockDeviceMapping(
                    DeviceName="/dev/sda1",
                    Ebs=ec2.EBSBlockDevice(
                        VolumeSize=Ref(parameters.InstanceStorageOS.title),
                        VolumeType="gp2"
                )),
            ],
            KeyName=Ref(parameters.InstanceKeyPair.title),
            IamInstanceProfile="",
            InstanceType=Ref(parameters.InstanceType.title)
        )
