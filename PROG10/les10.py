with open('fa_testkluizen.txt') as f:
    kluizen = f.readlines()

for kluis in kluizen:
    print(kluis.strip("\n").split(';'))

