#this is a list  use box brackets
myclassmate=["Erick","John","Sarah","Amy","Hansel","James", 50]
print(myclassmate[3],[4])
myclassmate[0]="Ann"
print(myclassmate)
mycars=["Toyota", "Tesla", "Mercedes", "Subaru", "Mitsubishi", "Nissan", "Ferrari"]
print(mycars)
mycars.append("Maybach") # append to add another item
mycars.insert(1, "Bugatti")
mycars
print(mycars)

#Tuple normal brackets
myfavfruits=("grapes", "tangerines", "mangoes", "pawpaw", "watermelon", "bananas")
myfavfruits[2]
print("my favourite fruit is "+ myfavfruits[2])
#setdatastructure

myfavballers={"messi", "mbappe", "neymar", "martinelli",}
myfavballers.add("saka")
print(myfavballers)

#dictionaries
magari={
    "Name":"Range" ,
    "Make":"Rangerover" ,
    "model":"SUV",
    "year" : "2020",

}
print(magari)
print(magari["Name"])
print(magari["Make"])