while True:
    print("1_ADI")
    print("2_FOGHOLADEH")
    print("3_DELKHAH")
    print("4_BANOVAN")
    print("5_JAVANAN")
    print("6_VAFADARI")
    print("7_RAMZ CHARGE")
    print("00-exit")
    x=int(input("select:"))
    match x:
        case 1:
            print("KHARID CHARGE(RIAL)")
            print("1-50,000","2-100,000","3-200,000","4-500,000","5-SAYER MABALEGH")
            a=int(input("select:"))
            if a==5:
                print("1-1,000,000","2-2,000,000","3-5,000,000")
                s=int(input("select:"))
            else:
                print("SHOMAREH MOSHTARAK MORED NAZAR RA BA FORMAT 9********* VARED KONID")
                b=int(input(">>>"))
                print("VOROOD YA ENTEKHAB CARD")
                i=int(input(">>>"))
                
        case 2:
            print("MODAT ETEBAR CHARGE ASLI VA HEDIEH MAHDOOD VA MOTENASEB BA MISAN CHARGE ")
            print("1-KHARID","2-RAHNAMA")
            c=int(input("select:"))
            if c==2:
                print("natige pyamak mishavad")
            else:
                print("1-50,000","2-100,000","3-200,000","4-500,000","5-1,000,000")
                f=int(input("select:"))
                print("SHOMAREH MOSHTARAK MORED NAZAR RA BA FORMAT 9********* VARED KONID")
                print("VOROOD YA ENTEKHAB CARD")
                k=int(input(">>>>>"))
        case 3:
            print("mablagh delkhah jahat charge ra vared konid.")
            print("(mazrab 1000 rial)")
            q=int(input("enter>>>"))
            print("shoma mablagh",q,"rial vared nemoodeh eid dar soorat taeid adad 1 ra vared konid")
            r=int(input(">>>"))
            print("SHOMAREH MOSHTARAK MORED NAZAR RA BA FORMAT 9********* VARED KONID")
            e=int(input(">>>"))
            print("VOROOD YA ENTEKHAB CARD")
            o=int(input(">>>>"))
        case 4:
            print("charge banovan")
            print("1-50,000")
            print("2-100,000")
            print("3-200,000")
            print("4-rahnama")
            t=int(input("select:"))
            if t==4:
                print("natige pyamak mishavad")
            else:
                 print("SHOMAREH MOSHTARAK MORED NAZAR RA BA FORMAT 9********* VARED KONID")
                 w=int(input(">>>>"))
                 print("VOROOD YA ENTEKHAB CARD")
                 p=int(input(">>>>"))
        case 5:
            print("charge JAVANAN")
            print("1-50,000")
            print("2-100,000")
            print("3-200,000")
            print("4-500,000")
            print("5-1,000,000")
            print("9-rahnama")
            r=int(input("select"))
            if r==9:
                 print("natige pyamak mishavad")
            else:
                  print("SHOMAREH MOSHTARAK MORED NAZAR RA BA FORMAT 9********* VARED KONID")
                  y=int(input(">>>"))
                  print("VOROOD YA ENTEKHAB CARD")
                  g=int(input(">>>>"))
                  print("MOSHTARAK GERAMI TANHA MOSHTARAKIN ETEBARI ZIR 25 SAL MASHMOOL HEDIEH CHARGE JAVANAN MIBASHAND")
        case 6:
            print("CHARGE VAFADARI")
            print("3-50,000" , "4-100,000" , "5-200,000")
            print("8-SAYER MABALEGH")
            print("9-RAHNAMA")
            u=int(input("select:"))
            if u==9:
                print("natige pyamak mishavad")
            elif u==8:
                print("CHARGE VAFADARI")
                print("6-500,000" ," 7-1,000,000")
                u=int(input(">>>"))
                print("SHOMAREH MOSHTARAK MORED NAZAR RA BA FORMAT 9********* VARED KONID")
                t=int(input(">>>"))
            else:
                 print("SHOMAREH MOSHTARAK MORED NAZAR RA BA FORMAT 9********* VARED KONID")
                 t=int(input(">>>"))
                 print("VOROOD YA ENTEKHAB CARD")
                 h=int(input(">>>"))
        case 7:
            print("KHARID CHARGE(RIAL)")
            print("2-50,000","3-100,000","4-200,000","5-500,000")
            a=int(input("select:"))
            print("VOROOD YA ENTEKHAB CARD")
            b=int(input(">>>"))
        case 00:
            exit()
        case _:
            print("error")









