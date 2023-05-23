pipeline{
    agent any
    environment{
        ENV_ONE=1
        ENV_TWO=2
        ENV_THREE=3
    }
    stages{
        stage("inbuildEnvironmentVariables")
        {
            steps{
                
                echo "JENKINS_URL : ${JENKINS_URL}\n GIT_AUTHOR_NAME : ${GIT_AUTHOR_NAME}\n GIT_AUTHOR_EMAIL : ${GIT_AUTHOR_EMAIL}\n GIT_COMMITTER_NAME : ${GIT_COMMITTER_NAME}\n GIT_COMMITTER_EMAIL : ${GIT_COMMITTER_EMAIL}\n GIT_URL : ${GIT_URL}\n BRANCH_NAME : ${BRANCH_NAME}\n"
            }
        }
        stage("parallel stages")
        {
             when{
                 branch "main1"   
                }
            parallel{
               
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
                 stage("p3"){
                    steps{
                        echo "parallel 2"
                    }
                }
                }
        }
        stage("one")
        {
            steps{
                echo "one ${ENV_ONE}"
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