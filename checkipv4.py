def checkipv4(ipStr):
    ipv4 = ipStr.split(".")
    print(ipv4)
    if 0<=int(ipv4[0])<=255 and 0<=int(ipv4[1])<=255 and 0<=int(ipv4[2])<=255 and 0<=int(ipv4[3])<=255:
        print("True")
        return True
    else:
        print("False")
        return False
   
if __name__ == "__mian__":
    main()
checkipv4("22.3.34.2231")
# tt = checkipv4("22.3.34.2231")
# if tt:
    # print("True")
# else:
    # print("False")