pipeline{
    agent any
    environment{
        ENV_ONE=1
        ENV_TWO=2
        ENV_THREE=3
    }
    parameters{
         string(name:'newString',defaultValue:"hello",description:"")
    }
    stages{
        stage("directoryContents")
        {
            steps{
                sh "python3 ./scripts/demo.py"
            }
        }
        stage("inbuildEnvironmentVar")
        {
            steps{
          
                echo "JENKINS_URL : ${JENKINS_URL}"
//                 echo "GIT_AUTHOR_NAME : ${GIT_AUTHOR_NAME}"
//                 echo "GIT_AUTHOR_EMAIL : ${GIT_AUTHOR_EMAIL}"
//                 echo "GIT_COMMITTER_NAME : ${GIT_COMMITTER_NAME}"
//                 echo "GIT_COMMITTER_EMAIL : ${GIT_COMMITTER_EMAIL}"
//                 echo "GIT_URL : ${GIT_URL}"
//                 echo "BRANCH_NAME : ${BRANCH_NAME}"
            
            }
        }
        stage("pythonScript")
        {
            steps{
                sh "python3 ./scripts/demo.py --jenkinvars env"
            }
        }
        stage("parameters")
        {
            steps{
               
                echo "parameters variable newString : ${params.newString}"
                
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
