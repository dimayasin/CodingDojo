def Reading_dict(dict1):
    New_Tuples=()
    i=0;


    for key,val in dict1.items():
            New_Tuples += (key,)
            New_Tuples += (val,)

    return New_Tuples

        #  New_Tuples[i] = key
        #     New_Tuples[i+1]= val
        #     i +=2

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

print Reading_dict(my_dict)

