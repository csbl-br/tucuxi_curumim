# Tucuxi-Curumim
Generates personal information for Brazilians, such as: ID, Name (linked mother's surname), Mother's Name, birth, gender and valid CPF.

## Need
Sometimes we need to do processing with real data information. So when we want to solve this quickly we go to
internet and downloaded somewhere.
We must be very careful, this information may violate the right to personal information.

## Solution
This simple script generates the amount of simulated Brazilian first and last name data you need to test your programs.

### Available fields:
```
Identifier;
Name;
Mother's Name;
Birth date;
Sex;
Valid CPF.
```
Tucuxi-Curumim run example:
>python tucuxi_curumim.py -n 100 -s ',' -o output.tsv

```
Subtitle:
-n = number of records
-s = Column delimiter [default='\t']
-o = Output file
```

