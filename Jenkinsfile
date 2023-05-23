pipeline{
    agent any
    environment{
        ENV_ONE=1
        ENV_TWO=2
        ENV_THREE=3
    }
    stages{
        stage("one")
        {
            steps{
                echo "one ${ENV_ONE}"
            }
        }
        stage("two")
        {
            steps{
                echo "two ${ENV_TWO}"
            }
        }
        stage("three")
        {
            steps{
                echo "three ${ENV_THREE}"
            }
        }
    }
}