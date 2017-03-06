from troposphere import Join, Ref, AWS_STACK_NAME
from troposphere import cloudwatch

from magicdict import MagicDict

class Cloudwatch(MagicDict):
    def __init__(self, ecs):
        super(Cloudwatch, self).__init__()

        self.LowMemoryReservedAlarm = cloudwatch.Alarm(
            "LowMemoryReservedAlarm",
            AlarmActions=Ref(ecs.AutoScalingGroupDownPolicy),
            AlarmDescription="Triggers when cluster underutilising resources",
            ComparisonOperator="LessThanThreshold",
            Dimensions=[
                cloudwatch.MetricDimension(
                    Name="ClusterName",
                    Value=Ref(ecs.Cluster)
                ),
            ],
            EvaluationPeriods="30",
            MetricName="MemoryReservation",
            Namespace="AWS/ECS",
            Period="60",
            Statistic="Maximum",
            Threshold="30"
        )


        self.HighMemoryReservedAlarm = cloudwatch.Alarm(
            "HighMemoryReservedAlarm",
            AlarmActions=Ref(ecs.AutoScalingGroupUpPolicy),
            AlarmDescription="Triggers when cluster running low on resources",
            ComparisonOperator="GreaterThanThreshold",
            Dimensions=[
                cloudwatch.MetricDimension(
                    Name="ClusterName",
                    Value=Ref(ecs.Cluster)
                ),
            ],
            EvaluationPeriods="1",
            MetricName="MemoryReservation",
            Namespace="AWS/ECS",
            Period="60",
            Statistic="Maximum",
            Threshold="80"
        )
