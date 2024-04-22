package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		amazonLinux, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
			MostRecent: pulumi.BoolRef(true),
			Filters: []ec2.GetAmiFilter{
				{
					Name: "name",
					Values: []string{
						"amzn2-ami-hvm-*-x86_64-gp2",
					},
				},
				{
					Name: "virtualization-type",
					Values: []string{
						"hvm",
					},
				},
			},
			Owners: []string{
				"amazon",
			},
		}, nil)
		if err != nil {
			return err
		}
		_, err = ec2.NewInstance(ctx, "web", &ec2.InstanceArgs{
			Ami:          pulumi.String(amazonLinux.Id),
			InstanceType: pulumi.String(ec2.InstanceType_T3_Micro),
			UserData: pulumi.String(`#!/bin/bash
yum update -y
amazon-linux-extras install docker -y
service docker start
usermod -a -G docker ec2-user
# Pull the Docker image
docker pull himanshu954/restapiv2:latest
# Run the Docker container
docker run -d -p 80:5000 himanshu954/restapiv2:latest
`),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("Restapi"),
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
