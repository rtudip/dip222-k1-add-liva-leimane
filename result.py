# name=[]
# with open("data.txt","r") as f:
#     for row in f:
#         row=row.rstrip().split(",")
#         name.append(row[6])
#     print(min(name))

name=[]
kkas=[]
with open("data.txt","r") as f:
    for row in f:
        row=row.rstrip().split(",")
        name.append((row[4]))
        if name=='Latvia':
            kkas.append((name))
    print(sum((kkas)))

# name=[]
# kkas=[]
# with open("data.txt","r") as f:
#     for row in f:
#         row=row.rstrip().split(",")
#         name.append(row[4])
#         if name=='Latvia':
#             kkas.append(int(name))
#     print(sum(kkas))

# name=[]
# kkas=[]
# with open("data.txt","r") as f:
#     for row in f:
#         row=row.rstrip().split(",")
#         name.append(row[4])
#         if name=='Latvia':
#             name.append(kkas)
#             if kkas=='Telecommunications':
#                 kkas.append(name)
#     print(sum(kkas))
