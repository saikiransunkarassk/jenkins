import subprocess
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--changeVar",nargs=2)


args=parser.parse_args()

with open(os.path.expanduser("~/.bashrc"), "a") as outfile:
    outfile.write('export {val1}="{val2}"'.format(val1=args.changeVar[0],val2=args.changeVar[1]))
    
if(args.changeVar[0] not in os.environ.keys()):  
    print("new environment variable is created")

val=subprocess.run(["conftest","verify", "--policy" ,"./policies/policy1", "--output=table"],capture_output=True,text=True)

output=val.stdout

print(output)

if(val.returncode==0):
    print("successfully runned")
else:
    print("unsuccessful")