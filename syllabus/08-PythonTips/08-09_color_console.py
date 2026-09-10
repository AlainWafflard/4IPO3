class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

str = "Warning: No active frommets remain."
print(bcolors.HEADER + str + bcolors.ENDC)
print(bcolors.OKBLUE + str + bcolors.ENDC)
print(bcolors.OKCYAN + str + bcolors.ENDC)
print(bcolors.OKGREEN + str + bcolors.ENDC)
print(bcolors.WARNING + str + bcolors.ENDC)
print(bcolors.FAIL + str + bcolors.ENDC)
print(bcolors.BOLD + str + bcolors.ENDC)
print(bcolors.UNDERLINE + str + bcolors.ENDC)
