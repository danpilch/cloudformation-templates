from troposphere import AWS_STACK_NAME, Join, Ref, Base64, Tags
from troposphere import autoscaling, policies
from troposphere import ecs, ec2

from magicdict import MagicDict
from parameters import Parameters

class ECS(MagicDict):
    def __init__(self, parameters, IAM):
        super(ECS, self).__init__()

        self.Cluster = ecs.Cluster(
            "Cluster"
        )

        self.LaunchConfiguration = autoscaling.LaunchConfiguration(
            "LaunchConfiguration",
            IamInstanceProfile=Ref(IAM.InstanceProfile),
            ImageId=Ref(parameters.InstanceImageId.title),
            InstanceType=Ref(parameters.InstanceType.title),
            KeyName=Ref(parameters.InstanceKeyName.title),
            SecurityGroups=[], # TODO
            UserData=Base64(
                Join("\n",
                    ["#!/bin/bash", Join("",
                        ["echo $ECS_CLUSTER=", Ref(self.Cluster)," >> /etc/ecs/ecs.config"])
                    ]
                )
            )
        )

        self.AutoScalingGroup = autoscaling.AutoScalingGroup(
            "AutoScalingGroup",
            Cooldown=Ref(parameters.Cooldown.title),
            DesiredCapacity=1,
            HealthCheckGracePeriod=Ref(parameters.InstanceGracePeriod.title),
            HealthCheckType="EC2",
            LaunchConfigurationName=Ref(self.LaunchConfiguration),
            MaxSize=Ref(parameters.InstanceMax.title),
            MinSize=1,
            TerminationPolicies=[
                "ClosestToNextInstanceHour",
                "Default"
            ],
            Tags=[
                autoscaling.Tag("Name", Ref(AWS_STACK_NAME), True),
            ],
            VPCZoneIdentifier=[   # TODO
                "",
                ""
            ],
            UpdatePolicy=policies.UpdatePolicy(
                AutoScalingRollingUpdate=policies.AutoScalingRollingUpdate(
                    MaxBatchSize="2",
                    MinInstancesInService="1",
                    WaitOnResourceSignals=False,
                    PauseTime="PT30S"
                )
            )
        )

        self.AutoScalingGroupDownPolicy = autoscaling.ScalingPolicy(
            "AutoScalingGroupDownPolicy",
            AdjustmentType="ChangeInCapacity",
            AutoScalingGroupName=Ref(self.AutoScalingGroup),
            Cooldown=Ref(parameters.Cooldown.title),
            ScalingAdjustment="-1"
        )
        
        self.AutoScalingGroupUpPolicy = autoscaling.ScalingPolicy(
            "AutoScalingGroupUpPolicy",
            AdjustmentType="ChangeInCapacity",
            AutoScalingGroupName=Ref(self.AutoScalingGroup),
            Cooldown=Ref(parameters.Cooldown.title),
            ScalingAdjustment="1"
        )

        self.InstanceSG = ec2.SecurityGroup(
            "InstanceSG",
            GroupDescription="Security group for cluster instances",
            VpcId="", #TODO
            Tags=Tags(
                Name=Join("", [Ref(AWS_STACK_NAME), "-cluster-instance"])
            )
        )
