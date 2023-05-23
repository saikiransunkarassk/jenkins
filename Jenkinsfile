pipeline{
    agent any
    //global environment varables
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
                parallel(
                stage("p1"){
                    steps{
                        echo "parallel 1"
                    }
                }
                stage("p2"){
                    steps{
                        echo "parallel 2"
                    }
                }
            )
            }
              
        }

        stage("two")
        {
            steps{
                echo "tw ${ENV_TWO}"
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