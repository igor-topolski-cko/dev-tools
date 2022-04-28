import argparse
import os
import sys
from urllib.request import urlopen
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser()
parser.add_argument("--input", help="Input file path")
parser.add_argument("--output", help="Output file path")
parser.add_argument("--overwrite", help="If present it will write output to the same file as source", action='store_true')
args = parser.parse_args()

if not args.input:
    print("Input file path is required")
    sys.exit(0)
elif not os.path.isfile(args.input):
    print("Input file does not exist")
    sys.exit(0)


if not args.output and not args.overwrite:
    print("Output file path is required")
    sys.exit(0)
elif not args.overwrite and os.path.isfile(args.output):
    print("Output file exists already - provide a file that does not exist")
    sys.exit(0)

def get_last_stable_release_version(package):
    url = f"https://www.nuget.org/packages/{package}/atom.xml"
    try:
        xml = urlopen(url).read()
        tree = ET.fromstring(xml)
        for x in tree:
            if(str(x.tag).endswith('entry')):
                for entry in x:
                    if(str(entry.tag).endswith('id')):
                        version = entry.text.split('/')[-1:][0]
                        if(version.find('-') == -1):
                            return version
    except:
        return False

    return False


def upgrade_csproj(path):
    source_file = open(path, "r")
    file = source_file.readlines()

    for line in enumerate(file):
        if line[1].lower().find("<targetframework>") != -1 and line[1].lower().find("</targetframework>") != -1:
            start_index = line[1].lower().find("<targetframework>")
            framework = line[1][start_index:].replace("<TargetFramework>", "").replace("</TargetFramework>", "").replace("\n", "")
            file[line[0]] = line[1].replace(framework, "net6.0")

        if line[1].lower().find("version=") != -1 and line[1].lower().find("include=") != -1 and line[1].lower().find("packagereference") != -1:
            include_index = line[1].lower().find("include=")
            include = line[1][include_index:].replace("Include=\"", "").replace("Include=\"", "")
            include = include[:include.find("\"")]

            version_index = line[1].lower().find("version=")
            version = line[1][version_index:].replace("Version=\"", "").replace("Version=\"", "")
            version = version[:version.find("\"")]

            new_nuget_version = get_last_stable_release_version(include)

            if(new_nuget_version):
                file[line[0]] = line[1].replace(version, new_nuget_version)


    source_file.close()
    return file

output_file = None

updated = upgrade_csproj(args.input)

if args.overwrite:
    output_file = open(args.input, "w")
else:
    output_file = open(args.output, "w")

output_file.write("".join(updated))
output_file.close()
