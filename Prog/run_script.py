#!/usr/bin/env python3
import os
import subprocess
import sys

# sys.argv[0] -> program name
# sys.argv[1] -> first real argument


def call_cmake():
    os.system("cmake ../ >/dev/null -DCMAKE_BUILD_TYPE=Debug -D CMAKE_CXX_FLAGS=-DDOCKER .")
    #             { ../ >/dev/null } will suppress cmake console output --


def run(input_command):
    code = subprocess.Popen(input_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        code.communicate(timeout=12)
        return code.returncode
    except subprocess.TimeoutExpired:
        code.kill()
        code.communicate()
        return -2000  # timeout error


def file_write_code(return_code):
    with open("err_output.txt", "a") as file:
        file.write(str(return_code))
    file.close()


def main():
    print("Container running...")
    call_cmake()
    make_command = "make"
    return_code: int = run(make_command)
    app_execute_command = "./Tests/UnitTests.exe"
    if return_code == 0:
        return_code: int = run(app_execute_command)
        file_write_code(return_code)
        exit(-1)
    else:
        file_write_code(-1000)  # make compilation error
        exit(-1)
    exit(0)


main()
