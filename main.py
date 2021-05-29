import argparse
import sys

SUBDOMAINS_FILENAME = "subdomains.txt"

def get_domain_from_cl():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='target domain', dest='domain', default="")
    args = parser.parse_args()
    return args.domain

def perform_brute_force(domain):
    with open(SUBDOMAINS_FILENAME) as f:
        for line in f:
            print(line.strip() + '.' + domain)

def main():
    # get domain from command line using -d option
    domain = get_domain_from_cl()

    if (not domain):
        print("Parent domain not specified using -d flag.")
        sys.exit(1)

    perform_brute_force(domain)

main()