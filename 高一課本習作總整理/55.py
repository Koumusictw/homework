for i in range(2,10,4):
    for j in range(1,10):
        print("{}*{}={:>2}".format(i,j,i*j),end="")
        print("\t{}*{}={:>2}".format(i+1,j,(i+1)*j),end="")
        print("\t{}*{}={:>2}".format(i+2,j,(i+2)*j),end="")
        print("\t{}*{}={:>2}".format(i+3,j,(i+3)*j),)
    print()