pipeline{

    agent any
    environment{
        TEXT = "Hello World!"
    }
    stage("pythonExecution")
    {
        sh "python3 -u ./scripts/main.py --location policies --policyName policy1 --printEnvVarName TEXT"
    }

}