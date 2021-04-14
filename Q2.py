def replace(s):
    changed = s.split()
    new = ""
    for i in range(0, len(changed)):
        if 'a' <= changed[i] <= 'z':
            changed[i] = changed[i].upper()
        else:
            changed[i] = changed[i]
    new = new.join(changed)
    return new

s1 = "hkken*()7"
s2 = "09*a£Ert45"
s3 = "Hello, hello"

changed_s1 = replace(s1)
changed_s2 = replace(s2)
changed_s3 = replace(s3)

print("original:", s1, "changed:", changed_s1)
print("original:", s2, "changed:", changed_s2)
print("original:", s3, "changed:", changed_s3)