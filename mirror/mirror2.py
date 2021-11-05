SIZE = 4
def bar():
    print("#" + (4 * SIZE)* "=" + "#")
def mirror():
    for line in list(range(1, SIZE + 1)) + list(range(SIZE, 0, -1)):
        print("|" + (-2 * line + 2 * SIZE) * " " +               "<>" + (4 * line - 4) * "." + "<>" +               (-2 * line + 2 * SIZE) * " " + "|")
        
# main
bar()
mirror()
bar()


# In[ ]:





# In[ ]:




