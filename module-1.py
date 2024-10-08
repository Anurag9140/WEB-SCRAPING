import pandas as pd
# with open("file.txt","w") as file:
#     file.write("Hello,I am learning web scraping")



states=["UP","BIHAR","RAJSTHAN","ODISA","JHARKHAND"]
population=[223021,203521,214589,181234,143742]
dict_states={"States":states,"Population":population}
df_states=pd.DataFrame.from_dict(dict_states)
print(df_states)

df_states.to_csv("States.csv",index=False)


list=[2,6,8,"anurag"]
for element in list:
    try:
        print(element/2)
    
    except:
        print("The element is not a number")
        
