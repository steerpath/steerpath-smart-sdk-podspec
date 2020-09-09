#!/usr/bin/env python

#Dependencies
import sys
import json
import subprocess
import os

print("Attempting to list local cocoapod repositories: \n")

#List CocoaPod repositories
listRepositories = "cd ~/.cocoapods/repos/; ls;"
error = subprocess.call(listRepositories, cwd=os.getcwd(), shell=True)
if error is not 0:
   sys.exit("ERROR! Failed to open local cocoapods repository folder. Make sure you have installed CocoaPods: https://cocoapods.org/")

print("\n")
#Show prompt for selecting repository
repository = input("Select repository for publish: ")
#Confirmation prompt
confirm = input("Are you sure you want to publish to " + repository + "? (y/n): ")
if confirm != 'y':
   sys.exit("Canceled publish process")

#Attempt to read the SDK version from the podspec file
podspecJson = None
podspecFileName = "SteerpathSmartSDK.podspec.json"

try:
   with open(podspecFileName) as jsonData:
      podspecJson = json.load(jsonData)
      jsonData.close()
except:
   sys.exit("ERROR! Failed to open podspec file " + podspecFileName)

if podspecJson is None:
   sys.exit("ERROR! Failed to read podspec file " + podspecFileName)

sdkVersion = podspecJson["version"]

#Commit and tag release version
createTag = "git add -A && git commit -m 'Release " + sdkVersion + "'; git tag " + sdkVersion
error = subprocess.call(createTag, cwd=os.getcwd(), shell=True)
if error is not 0:
   sys.exit("ERROR! Failed to tag version " + sdkVersion)

#Attempt to push into CocoaPod repository
pushCocoapod = "pod repo push " + repository + " " + podspecFileName
error = subprocess.call(pushCocoapod, cwd=os.getcwd(), shell=True)
if error is not 0:
   sys.exit("ERROR! Failed to push changes into CocoaPod repository " + repository)
   
