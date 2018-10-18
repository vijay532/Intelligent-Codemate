import re
import random
import subprocess
import sys

# from install_packages import toString, runrealtime
# import install_packages


def toString(byte):
    return byte.decode("utf-8").strip()


def run(args):
    process = subprocess.Popen(
        args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.communicate()


def runrealtime(args):
    process = subprocess.Popen(
        args, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    while process.poll() is None:
        output = process.stdout.readline().decode("utf-8").strip()
        print(output)
    return process.communicate()

print("\nChecking for the error in testing file...")
output, error = runrealtime(["python", "buggy-file.py"])

if len(error) == 0:
    print('Done, Good to GO!')
else:
    err = toString(error)

    er = re.search(
        r'Traceback \(most recent call last\):\n(?:[ ]+.*\n)*(\w+: .*)', err).groups()
    # print(error)
    print(toString(er))
    print()
    print('Error...Unable to run file!')
    sys.exit()
