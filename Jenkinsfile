pipeline{

    agent any
    environment{
        TEXT = "Hello World!"
    }
    stages
    {
        stage("pythonExecution"){
        steps{
        sh "python3 -u ./scripts/main.py --location policies --policyName policy1 --printEnvVarName TEXT"
        }
        }
    }

}