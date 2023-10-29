#!/bin/bash

# Get the directory path of the script file
script_dir=$(dirname "$0")

pushd "${script_dir}" || exit
./main
popd || exit