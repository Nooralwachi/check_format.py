import re
def check_format(filename):
	costs={}
	with open(filename) as f:
		for line in f:
			license = line.strip()
			pattern= r'^[1-9][A-HJ-NP-Z]{3}(\d)((?!\1)\d{2})$'
			if re.match(pattern, license):
				print(license)

check_format('licenses.txt')