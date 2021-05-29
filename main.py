import argparse
import sys

SUBDOMAINS_FILENAME = "subdomains.txt"

C_RESET = "\033[0m"
C_RED = "\033[1;31m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_WHITE = "\033[1;37m"

def get_domain_from_cl():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='target domain', dest='domain', default="")
    args = parser.parse_args()
    return args.domain

def perform_brute_force(domain):
    with open(SUBDOMAINS_FILENAME) as f:
        for line in f:
            resolve_subdomain(line.strip() + '.' + domain)

def resolve_subdomain(subdomain):
    print(f"{C_RED}[-] {subdomain} {C_RESET}")

    print(f"{C_YELLOW}[!] {subdomain} {C_RESET}")
    print(f"{C_GREEN}[+] {subdomain} {C_RESET}")

def main():
    # get domain from command line using -d option
    domain = get_domain_from_cl()

    if (not domain):
        print("Parent domain not specified using -d flag.")
        sys.exit(1)

    perform_brute_force(domain)

main()