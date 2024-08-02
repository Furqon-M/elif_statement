# ELIF -> ELSE IF

nama = input("Nama Kamu Siapa? ")

if nama == "kelana": # kondisi 1
    print("Hello kelana") # aksi true 1
elif nama == "angan": # kondisi 2
    print("Hello angan") # aksi true 2
elif nama == "angga": # kondisi 3
    print("Hello angga") # aksi true 3
else:
    print("Hello siapa ?") # aksi false
print("Selamat Datang", nama)