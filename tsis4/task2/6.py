regex_pattern = r"[IVXLCDM][IVXLCDM]*"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))