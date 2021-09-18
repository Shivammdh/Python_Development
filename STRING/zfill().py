'''The zfill() method adds zeros (0) at the beginning of
the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the
string, no filling is done.'''
txt = "50"

x = txt.zfill(10)

print(x)