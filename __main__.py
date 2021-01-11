"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

instance_assume_role_policy = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
    actions=["sts:AssumeRole"],
    principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
        type="Service",
        identifiers=["lambda.amazonaws.com"],
    ),
      aws.iam.GetPolicyDocumentStatementPrincipalArgs(
        type="Service",
        identifiers=["logs.eu-central-1.amazonaws.com"],
    )],
)])

lambda_role = aws.iam.Role("lambda_role",
    path="/system/",
    assume_role_policy=instance_assume_role_policy.json)

lambda_function = aws.lambda_.Function(
  "example_lambda_function",
  code=pulumi.FileArchive('./handler'),
  role=lambda_role.arn,
  runtime='nodejs12.x',
  handler = 'index.handler'
)