import argparse
import sys
import dns.resolver

SUBDOMAINS_FILENAME = "subdomains.txt"

C_RESET = "\033[0m"
C_RED = "\033[1;31m"
C_GREEN = "\033[1;32m"
C_YELLOW = "\033[1;33m"
C_WHITE = "\033[1;37m"

NXDOMAIN = "NXDOMAIN"
NAMESERVER = "8.8.8.8"


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
    print(f"{C_YELLOW}[!] {subdomain} {C_RESET}")

    try:
        resolver = dns.resolver.Resolver()
        resolver.nameserver = [NAMESERVER]
        answers = resolver.resolve(subdomain, rdtype=dns.rdatatype.A)
        print(f"{C_GREEN}[+] {subdomain} {C_RESET}")
    except (dns.resolver.NXDOMAIN, dns.name.EmptyLabel, dns.resolver.NoAnswer):
        print(f"{C_RED}[-] {subdomain} {C_RESET}")


def main():
    # get domain from command line using -d option
    domain = get_domain_from_cl()

    if (not domain):
        print(f"{C_RED}[-] Parent domain not specified.\nUse -d flag. {C_RESET}")
        sys.exit(1)

    perform_brute_force(domain)


main()