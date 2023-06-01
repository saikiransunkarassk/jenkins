pipeline{

    agent any
    environment{
        TEXT = "Hello World!"
    }
    stages
    {
        stage("pythonExecution"){
        steps{
        sh "python3 -u ./scripts/main.py --location policies --policyName policy1 --printEnvVarName TEXT --changeEnvVal TEXT hello --addEnvVar NEW_ENV hello"
        sh "cat tempFile"
        }
        }
    }

}