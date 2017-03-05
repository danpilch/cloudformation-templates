from troposphere import AWS_STACK_NAME, FindInMap, GetAtt, ImportValue, Join, Ref, Tags
from troposphere import autoscaling
from troposphere import ecs

from magicdict import MagicDict
from parameters import Parameters
from iam_policy import IAM

class ECS(MagicDict):
    def __init__(self, parameters):
        super(ECS, self).__init__()

        self.Cluster = ecs.Cluster(
            "Cluster"
        )

        self.LaunchConfiguration = autoscaling.LaunchConfiguration(
            "LaunchConfiguration",
            IamInstanceProfile=Ref(IAM.InstanceProfile)
        )
