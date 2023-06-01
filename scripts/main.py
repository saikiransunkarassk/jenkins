import subprocess
import os
import argparse


class NewClass:
    def __init__(self, location, policyName, envVarName):

        self.location = location

        self.policyName = policyName

        self.envVarName = envVarName

        self.returnCode = True

    def conftestCommand(self):

        output = subprocess.run(["conftest", "verify", "--policy", "./"+self.location +
                                "/"+self.policyName, "--output=table"], capture_output=True, text=True)

        if (output.returncode != 0):

            self.returnCode = False

        else:

            print(output.stdout)

    def opaCommand(self):

        output = subprocess.run(["opa", "test", "-c", "./"+self.location + "/"+self.policyName+"/"+self.policyName+".rego",
                                "./"+self.location + "/"+self.policyName+"/"+self.policyName+"_test.rego"], capture_output=True, text=True)

        if (output.returncode != 0):

            self.returnCode = False

        else:

            print(output.stdout)

    def printEnvVar(self):

        if (self.envVarName in os.environ.keys()):

            print(os.environ[self.envVarName])

        else:

            print("No Environment Variable with Name " +
                  self.envVarName+" is Found")


if __name__ == "__main__":

    f = open("tempFile", "w+")

    parser = argparse.ArgumentParser()

    parser.add_argument("--location")

    parser.add_argument("--policyName")

    parser.add_argument("--printEnvVarName")

    # parser.add_argument("--changeEnvVal", nargs=2)

    # parser.add_argument("--addEnvVar", nargs=2)

    inputs = parser.parse_args()

    newObject = NewClass(inputs.location, inputs.policyName,
                         inputs.printEnvVarName)

    if (inputs.location != None and inputs.policyName != None):

        newObject.conftestCommand()

        newObject.opaCommand()

    if (inputs.printEnvVarName != None):

        newObject.printEnvVar()

    if (inputs.changeEnvVal != None):

        f.write(f"c ${inputs.changeEnvVal[0]} ${inputs.changeEnvVal[1]}\n")

    if (inputs.addEnvVar != None):

        f.write(f"a ${inputs.addEnvVar[0]} ${inputs.addEnvVar[1]}")

    f.close()

    if (newObject.returnCode == True):
        print("successful")
    else:
        print("unsuccessful")


# print(os.environ)

# os.environ[args.changeVar[0]]=args.changeVar[1]

# print(os.environ[args.changeVar[0]])

# os.environ["NEW_VAR"]="hello"

# if(args.changeVar[0] not in os.environ.keys()):
#     print("new environment variable is created")


# output=val.stdout

# print(output)
