# luhn
Calculate Control digit for all possible 4-digit numbers, disallowing certain substrings.

# Usage

```bash
python generateLuhnCompatibleIDs.py
#00018
#00026
#00034
#00042
#...
```

# Details

This script generates all possible 4-digit string with added control digit using Luhn's algorithm. 

The following two-digit substrings are disallowed (and therefore not printed) since Luhn's algorithm doesn't alter the control digit for these changes. 

* `09`, `90` (transposition)
* `22`, `55`
* `33`, `66`
* `44`, `77`

The IDs are also available in the file [ALLOWED_IDS.txt]() in this repo for easy access.

# License

MIT

