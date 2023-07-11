while(True):
    print(f"")
    print(f"REGISTRATION DETAIL")
    print(f"")
    print(f"1. NEW ADMISSION")
    print(f"2. DISPLAY ALL THE STUDENT DETAIL")
    print(f"3. SEARCH STUDENT RECORD")
    print(f"4. UPADATE STUDENT DETAIL")
    print(f"5. DELETE STUDENT")
    print(f"6. COURSE WISE LIST")
    print(f"7. NO OF ADMISSION, ACCORDING TO COURSE")
    print(f"8. EXIT")
    print(f"")
    task=int(input("Choice the OPERATION to do :"))
    
    if(task==1):
        uucms=input("Enter Registration NO :")
        name=input("Enter Student Name :")
        print("1.Male")
        print("2.Famele")
        gender=int(input("Choice the gender :"))
        if(gender==1):
            gender="Male"
        else:
            gender="Female"
        while(True):
            file=open("admission.csv","a")
            print(f"1.BCA")
            print(f"2.BSC")
            print(f"3.BBA")
            print(f"4.Bcom")
            print(f"5.BA")
            course=int(input("Choice Student Course :"))
            if(course==1):
                course="BCA"
                break
            elif(course==2):
                course="BSC"
                break
            elif(course==3):
                course="BBA"
                break
            elif(course==4):
                course="BCOM"
                break
            elif(course==5):
                course="BA"
                break
            else:
                print(f"Choice the current course from the list")
        sem=input(f"Enter Semester :")
        fees=int(input("Enter course fees :"))
        detail=f"{uucms},{name},{gender},{course},{sem},{fees}\n"
        file.write(detail)
        print(f"")
        print(f"STUDENT RECORD SAVE SUCCESSFULL")
        file.close()
        
    elif(task==2):
        file=open("admission.csv","r")
        data=file.read()
        d=data.split('\n')
        d=d[0:len(d)-1]
        print(f"STUDENT LIST IS AS FOLLOW ")
        print(f"UUCMS_NO\tNAME\tGENDER\tCOURSE\tSEM\tFEES")
        print(f"--------------------------------------------")
        for s in d:
            l=s.split(',')
            print(f"{l[0]}\t\t{l[1]}\t{l[2]}\t{l[3]}\t{l[4]}\t{l[5]}")
        file.close()
    
    elif(task==3):
        print(f"TO GET THE DETAILS OF PERTICULAR  STUDENT ")
        uucms=input("Enter the student registration No. :")
        file=open("admission.csv","r")
        data=file.read()
        d=data.split('\n')
        d=d[0:len(d)-1]
        item=None
        for s in d:
            l=s.split(',')
            if(l[0]==uucms):
                item=l
        if(item==None):
            print(f"STUDENT {uucms} IS NOT FOUND")
        else:
            print(f"Uucms\t\tName\t\tGender\t\tCourse\t\tSem\t\tFees")
            print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\t\t{item[3]}\t\t{item[4]}\t\t{item[5]}")
        file.close()
    
    elif(task==4):
        print(f"TO UPDATE THE DETAILS OF PERTICULAR  STUDENT")
        uucms=input("Enter the student registration No. :")
        file=open("admission.csv","r")
        data=file.read()
        d=data.split('\n')
        d=d[0:len(d)-1]
        file.close()
        filew=open("admission.csv","w")
        item=None
        for s in d:
            l=s.split(',')
            if(l[0]==uucms):
                item=l
                print(f"ENTER BELOW DETIAL TO UPDATE")
                name=input("Enter Student Name :")
                print("1.Male")
                print("2.Famele")
                gender=int(input("Choice the gender :"))
                if(gender==1):
                    gender="Male"
                else:
                    gender="Female"    
                while(True):
                    print(f"1.BCA")
                    print(f"2.BSC")
                    print(f"3.BBA")
                    print(f"4.Bcom")
                    print(f"5.BA")
                    course=int(input("Choice Student Course :"))
                    if(course==1):
                        course="BCA"
                        break
                    elif(course==2):
                        course="BSC"
                        break
                    elif(course==3):
                        course="BBA"
                        break
                    elif(course==4):
                        course="Bcom"
                        break
                    elif(course==5):
                        course="BA"
                        break
                    else:
                        print(f"Choice the current course from the list")
                sem=input(f"Enter Semester :")
                fees=int(input("Enter course fees :"))
                detail=f"{uucms},{name},{gender},{course},{sem},{fees}\n"
                filew.write(detail)
            else:
                filew.write(s+"\n") 
        if(item==None):
            print(f"STUDENT {uucms} IS NOT EXIST")
        else:
            print(f"UPDATE OF STUDENT RECORD SUCCESSFULL")
        filew.close()
            
               
    elif(task==5):
        print(f"TO DELETE THE DETAILS OF PERTICULAR  STUDENT")
        uucms=input("Enter regitration NO.  :")
        file=open("admission.csv","r")
        data=file.read()
        d=data.split('\n')
        d=d[0:len(d)-1]
        file.close()
        filew=open("admission.csv","w")
        item=None
        for s in d:
            l=s.split(',')
            if(l[0]==uucms):
                item=l
            else:
                filew.write(s+"\n")
        if(item==None):
            print(f"STUDENT {uucms} IS NOT FOUND")
        else:
            print(f"STUDENT RECORD DELETED SUCCESSFULL")
        filew.close()

    
    elif(task==6):
        print("DISPLAY THE STUDENTS ACCORDING TO COURSE")
        course=input("Enter course name :")
        c=course.upper()
        print(f"")
        file=open("admission.csv","r")
        data=file.read()
        d=data.split('\n')
        d=d[0:len(d)-1]
        print(f"STUDENTS ACCORDING TO {c} COURSE WISE :")
        print(f"UUCMS\tNAME\tGENDER\tCOURSE\tSEM\tFEES")
        print(f"----------------------------------------------")
        item=0
        for s in d:
            if c in s:
                item=item+1
                l=s.split(',')
                for i in range(0,len(l)):
                    print(l[i],end="\t")
                print(f"\n")
        if(item==0):
            print(f"NOT ANY OF THE STUDENTS ARE ENROLLED IN COURSE {c}")    
        file.close()
    

    elif(task==7):
        print("NO OF STUDENTS ADDMITIONED ACCORDING TO COURSE WISE")
        print(f"")
        file=open("admission.csv","r")
        data=file.read()
        d=data.split('\n')
        d=d[0:len(d)-1]
        print(f"NO OF STUDENTS ENROLLED In PERTICULAR COURSE :")
        print(f"COURSE\tCOUNT")
        print(f"---------------------------------------")
        bca,bsc,bba,bcom,ba=0,0,0,0,0
        for s in d:
            l=s.split(',')
            if(l[3]=="BCA"):
                bca=bca+1
            elif(l[3]=="BSC"):
                bsc=bsc+1
            elif(l[3]=="BBA"):
                bba=bba+1
            elif(l[3]=="Bcom"):
                bcom=bcom+1
            else:
                ba=ba+1
        if(bca==0):
            print(f"BCA\t{bca}")
        else:
            print(f"BCA\t{bca}")
        if(bsc==0):
            print(f"BSC\t{bsc}")
        else:
            print(f"BSC\t{bsc}")
        if(bba==0):
            print(f"BBA\t{bba}")
        else:
            print(f"BBA\t{bba}")
        if(bcom==0):
            print(f"BCOM\t{bcom}")
        else:
            print(f"BCOM\t{bcom}")
        if(ba==0):
            print(f"BA\t{ba}")
        else:
            print(f"BA\t{ba}")
        file.close()
        
    
    elif(task==8):
        print(f"***********")
        break
    else:
        print(f"CHOICE THE CORRECT OPERATION WITHIN 1 TO 8 TO DO")