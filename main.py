import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-d', help='target domain', dest='domain', default="")
args = parser.parse_args()
domain = args.domain

print(domain)
