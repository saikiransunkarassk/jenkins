import subprocess
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--jenkinvars")

args=parser.parse_args()

print(args)

print(os.environ)
commandList=["conftest","verify", "--policy" ,"./policies/policy1", "--output=table"]

val=subprocess.run(commandList,capture_output=True,text=True)

output=val.stdout

print(output)

if(val.returncode==0):
    print("successfully runned")
else:
    print("unsuccessful")