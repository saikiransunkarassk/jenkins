import subprocess
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--changeVar",nargs=2)

args=parser.parse_args()

val=subprocess.run(["conftest","verify", "--policy" ,"./policies/policy1", "--output=table"],capture_output=True,text=True)

print(os.environ)

os.environ[args.changeVar[0]]=args.changeVar[1]

print(os.environ[args.changeVar[0]])

os.environ["NEW_VAR"]="hello"

if(args.changeVar[0] not in os.environ.keys()):  
    print("new environment variable is created")


output=val.stdout

print(output)

if(val.returncode==0):
    print("successfully runned")
else:
    print("unsuccessful")