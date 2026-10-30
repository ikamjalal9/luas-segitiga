phi=3.14
pilihan = int(input("pilih:1=keliling,2=luas:"))
r=float(input("masukan jari-jari linkaran:"))
if pilihan ==1:
    keliling =2*phi*r
    print("keliling lingkaran=",keliling)
elif pilihan ==2:
    luas=phi*r*r
    print("luas linkaran =",keliling)
else:
    print("pilihan tidak valid")