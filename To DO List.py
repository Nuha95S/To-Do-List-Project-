to_do_list = input("Enter your tasks for today sperated by comma:").split(", ")
done = []
ongoing =[]
for do in to_do_list:
   print(f"\n{do}\n")
   x=input(f"Did you finish {do} alredy?").lower()
   if x == "yes":
      print("Nice job")
      done.append(do)
   else:
      print("Try not to put it off")
      ongoing.append(do)
   print("--------")
done_task = input("Do you want to see your today's progress?(yes/no)").lower()
if done_task=="yes":
   print(f"""*******Done Tasks******\n{done}""")
   print(f"""\n*******Ongoing Tasks********\n{ongoing}""")
else:
   print("Please hit enter to exit")

