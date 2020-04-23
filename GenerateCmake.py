import xml.etree.cElementTree as ET
import sys
import os.path

count = len(sys.argv)

if count > 1:
    filepath = sys.argv[1]
else:
    filepath = input("Input file path: ")

splitpath = os.path.split(filepath)
directory = splitpath[0]

patterns = dict()
patterns["project"] = splitpath[1].split(".")[0]

#D:\Projects\TGEngine\TGEngine\TGEngine.vcxproj
tree = ET.ElementTree(file=filepath)
root = tree.getroot()
prefix = root.tag.replace("Project", "") # to avoid the xmlns schema
includes = root.iter(prefix + "ClInclude")
compiles = root.iter(prefix + "ClCompile")

filteredIncludes = []
for include in includes:
    filteredIncludes.append(include.get("Include"))

filteredCompile = []
for target in compiles:
    filteredCompile.append(target.get("Include"))