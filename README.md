<!--
title: 'Swaous Senior Project: Employee Reports Portal API for Risen One Consulting'
description: 'Project created for senior project at University of Central Misouri. This project is developed for Risen One Consulting to allow employees to submit reports and view already submitted reports. Developed using Angular for the frontend services and the Serverless Framework connected through AWS for backend services. The API comes equipped with a sign in and sign up page, reports page for viewing reports, profile page for updating user information, and an admin page for viewing all employee reports and deleting them if necessary.' 
layout: Doc
framework: v3
platform: AWS
language: nodeJS
priority: 1
authorLink: 'https://github.com/ucmo-cs/Swaous_SP23'
authorName: 'Dakota Reid, Jackson Boster, Jakob Bush, Joshua Jackson'
-->

# Swaous Senior Project: Employee Reports Portal API with Angular, Serverless Framework, and AWS

Project created for senior project at University of Central Misouri. This project is developed for Risen One Consulting to allow employees to submit reports and view already submitted reports. Developed using Angular for the frontend services and the Serverless Framework connected through AWS for backend services. The API comes equipped with a sign in and sign up page controlled by AWS Cognito, reports page for viewing reports, profile page for updating user information, and an admin page for viewing all employee reports and deleting them if necessary.


## Anatomy of the Project

This project was developed with Angular for both frontend and AWS (IAM, API Gateway, Lambda, DynamoDb, Cognito, S3, and SES) and Serverless Framework for backend.

Base URL: http://risen-one-consulting-dev-serverlessdeploymentbuck-1pvofqrnrgpcu.s3-website-us-east-1.amazonaws.com/

### Authorers

Dakota Reid,
Jackson Boster,
Jakob Bush,
Joshua Jackson

### Version repo 
This repo used github actions along with semantic-release to create git tags. 
A git tag is a lightweight, permanent label that is attached to a specific point in git history. I like to think about tags as a different type of branch but instead of changing over time it is immutable. 

Semantic-release is a lightweight way of using commit messages to update the tag number. The only requirement to use this system is that we stick to a standardized way of making commits for now this follows the [default angular commit syntax](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit-message-header). Please note that the `[type]: your message` is required but the `(scope)` is no longer included in our version. This can be changed if we decide this is wanted.

```
Commit Message Header
<type>: <short summary>
  │       │
  │       └─⫸ Summary in present tense. Not capitalized. No period at the end.                                                                        
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test

Both fields are mandatory for the commit.
```

### Type
Must be one of the following:
- build: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- ci: Changes to our CI configuration files and scripts (examples: CircleCi, SauceLabs)
- docs: Documentation only changes
- feat: A new feature
- fix: A bug fix
- perf: A code change that improves performance
- refactor: A code change that neither fixes a bug nor adds a feature
- test: Adding missing tests or correcting existing tests
