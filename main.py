import argparse

def getDomainFromCL():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='target domain', dest='domain', default="")
    args = parser.parse_args()
    return args.domain

# with open("./subdomains.txt") as f:
#     for line in f:
#         print(line.strip())

def main():
    # get domain from command line using -d option
    domain = getDomainFromCL()
    print(domain)
    
main()