#!/bin/bash

# Get the directory path of the script file
script_dir=$(dirname "$0")

# Build UI
pushd "${script_dir}/UI" || exit
npm i
npm run publish
popd || exit

# Build backend
pushd "${script_dir}/API" || exit
pipenv install
pipenv run python setup.py build
popd || exit

# Move build assets to release folder
rm -r Release
mkdir Release
mv ./API/build/exe.linux-x86_64-3.10/** ./Release
rm -r ./API/build