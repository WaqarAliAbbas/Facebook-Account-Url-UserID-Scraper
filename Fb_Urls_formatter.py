-- Developer Waqar Ali Abbas --
file_var=input("Enter File Name With .txt Extension:  ")
with open(file_var,"r",encoding="UTF") as f:
    a=f.readlines()
with open("Formatting_Done.txt","a",encoding="UTF-8") as f:
    for i in a:
        if "profile.php?id" in i:
            b=i.split("=")
            user_Id=b[1].split("&")[0]
            f.write(f"{user_Id}\n")
        else:
            b=i.split("/")
            user_Id=b[3].split("?")[0]
            f.write(f"{user_Id}\n")