import argparse
from xml.etree import ElementTree as et


parser = argparse.ArgumentParser("simple_example")
parser.add_argument("version", help="A string denoting the version to be realeased", type=str)
args = parser.parse_args()
print(args.version)

tree = et.parse("../HappyLittleHelpers.AdhocDataQueries.csproj")
tree.find('.//PackageVersion').text = args.version
tree.find('.//Version').text = args.version
tree.write("../HappyLittleHelpers.AdhocDataQueries.csproj",encoding='UTF-8',xml_declaration=False)
