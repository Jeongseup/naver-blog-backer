g_c = 0
print ("Initial value of g_c: " + str(g_c))
print("Variable defined outside of method automatically global? "
      + str("g_c" in globals()))

class TestClass():
    def direct_print(self):
        print("Directly printing g_c without declaration or modification: "
              + str(g_c))
        #Without any local reference to the name
        #Python defaults to search for the variable in globals()
        #This of course happens for all the module names you import

    def mod_without_dec(self):
        g_c = 1
        #A local assignment without declaring reference to global variable
        #makes Python default to access local name
        print ("After mod_without_dec, local g_c=" + str(g_c))
        print ("After mod_without_dec, global g_c=" + str(globals()["g_c"]))


    def mod_with_late_dec(self):
        g_c = 2
        #Even with a late declaration, the global variable is accessed
        #However, a syntax warning will be issued
        global g_c
        print ("After mod_with_late_dec, local g_c=" + str(g_c))
        print ("After mod_with_late_dec, global g_c=" + str(globals()["g_c"]))

    def mod_without_dec_error(self):
        try:
            print("This is g_c" + str(g_c))
        except:
            print("Error occured while accessing g_c")
            #If you try to access g_c without declaring it global
            #but within the method you also alter it at some point
            #then Python will not search for the name in globals()
            #!!!!!Even if the assignment command occurs later!!!!!
        g_c = 3

    def sound_practice(self):
        global g_c
        #With correct declaration within the method
        #The local name g_c becomes an alias for globals()["g_c"]
        g_c = 4
        print("In sound_practice, the name g_c points to: " + str(g_c))


t = TestClass()
t.direct_print()
t.mod_without_dec()
t.mod_with_late_dec()
t.mod_without_dec_error()
t.sound_practice()