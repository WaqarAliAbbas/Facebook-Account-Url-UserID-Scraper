# -- Developer Waqar Ali Abbas --
filename=input("Enter file name with .txt extension:  ")
with open(filename,"r",encoding="UTF") as f:
    a=f.readlines()
with open("saverecords.txt","a",encoding="UTF-8") as f:
    for i in a:
        if "profile.php?id" in i:
            b=i.split("=")
            user_Id=b[1].split("&")[0]
            f.write(f"{user_Id}\n")
        else:
            b=i.split("/")
            user_Id=b[3].split("?")[0]
            f.write(f"{user_Id}\n")
