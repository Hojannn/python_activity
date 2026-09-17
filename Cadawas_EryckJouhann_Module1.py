#Pogi ako
con = True
while con == True:

    print("====SMART CAMPUS SYSTEM====")
    print("1. Attendance Counter")
    print("2. Secure Login")
    print("3. Grade Analyzer")
    print("4. Classroom Seat Map")
    print("5. Data Cleaning")
    print("6. Exit")
    
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    #Attendance Counter
    def AttCount():
        stat = True
        pres = 0
        abs = 0
        late = 0
        
        while stat ==  True:
           
            att = input("Enter attendance (PRESENT/ABSENT/LATE or DONE): ").lower()
            if att == "present":
                pres += 1
            elif att == "absent":
                abs += 1
            elif att == "late":
                late += 1
            elif att == "done":
                print("Attendance Summary: ")
                print(f"Present: {pres}")
                print(f"Absent: {abs}")
                print(f"Late: {late}")
                stat = False
            
    #Secure Login
    def SecureLog():
        attempts = 1
        password = "LSPU2026"
        while attempts <= 3:
            ent = input("Enter The Correct Password: ")
            attempts += 1
            if ent == password:
                print("Correct!")
                break
            elif attempts > 3:
                print("Maximum Attempts Reached, Noob.")
                break
            
    #Grade Analyzer/Skip
    def GradeAna():
        print("""
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⡇⠛⠛⠿⡿⡟⠻⣻⣿⠛⠛⠟⠛⠛⠛⠃⠙⠛⣛
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⣴⣶⣿⣿⣿⡏⠘⠟⠀⠀⠀⣼⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠘⢿⣿⣿⣿⡇⠠⡶⢠⠰⢸⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡙⣿⣿⢳⢰⡇⠀⠀⠈⠛⠛
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⠿⠃⠀⠀⠀⠀⠀⣀⣾⣿⣿⣿⣿⣧⣈⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠠⡱⢬⠉⠀⠈⣷⢔⠄⠀⢀⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⡘⠀⠀⠀⣠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠈⡈⢁⡰⠀⠸⠀⠀⠀⣤⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⣼⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠈⠐⠯⠁⠁⠀⡁⣷⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⣾⡏⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠄⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⠟⡛⠃⠀⠀⠀⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠈⠀⡀⠀⠀⠀⠀⡿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⡟⣴⠒⢠⣴⣿⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠂⠀⠀⡇⣿⣿
                ⢂⠀⠀⠀⠀⠀⠀⢀⡿⠀⢸⣿⣿⡇⣿⣿⣿⣯⡉⠻⠿⢿⣿⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢿⣿⣿⢟⠀⣤⣶⡆⠀⡄⠀⠀⠀⡇⣿⣿
                ⢸⣄⠀⠀⠀⠀⠀⠈⠃⠀⠘⠿⠿⠁⣿⣿⣿⣿⣷⣤⣄⣀⠀⠁⢸⣿⣿⠛⠋⠉⠉⢀⣀⣜⣶⣶⡧⠊⠀⢳⣿⡇⠘⣸⠀⡄⠀⠘⣿⣿
                ⢸⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣇⡈⠉⠉⠉⠁⠀⠠⣴⣾⣿⣿⣧⠀⠀⠈⠉⠉⠙⠛⠋⢁⡤⠀⠘⢿⠇⠀⠻⠀⡇⠀⠀⣿⣿
                ⣘⣿⣾⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⣿⣿⣶⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣷⠙⣦⣄⣀⣀⢀⢶⣾⣿⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⣻⡿
                ⠿⣿⣭⡙⢷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣧⣌⢿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠘⠐⣿⣗
                ⠀⠉⢻⣿⣦⣙⢿⣦⣀⡀⠀⠀⠀⠀⢠⣴⣝⠿⣟⣿⣿⣯⠙⠁⠈⠙⠛⠉⠁⠋⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣛
                ⡀⣀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⠶⠂⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣀⠀⠀⠀⢀⣿⣿⣿⣇⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢀⠀⢠⡄⣿
                ⣿⣷⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠈⣛⣿⣿⣿⡿⣿⣿⣿⢿⢻⣿⣻⣶⣿⣿⢿⣿⣿⡟⠀⠀⠀⠀⠤⠠⠀⠜⠀⠀⠀⠆⠤⠤⠟
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣁⣤⠀⠀⠀⠑⠙⢻⣿⣧⣀⣉⣈⡉⠳⠃⢀⣀⠈⠀⢺⠟⠁⠀⠀⠀⠀⠀⠐⢶⠀⣄⠀⠀⠀⢰⣶⣶⣶
                ⣿⣿⠿⠿⠟⠛⠛⠃⣀⣀⣾⣿⣿⣆⠀⠀⠀⠀⠀⡸⣿⠎⠫⠉⡛⢷⡶⢿⠟⠀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⢺⣿⣿⣿
                ⣭⣤⣶⣶⣶⣶⣖⣿⠻⣷⣝⠻⣿⣿⣷⣄⠀⠀⠀⠀⢻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠂⠻⢿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣬⢷⡌⠻⣦⠙⢿⣿⣿⣶⡀⠀⠀⠀⠘⢿⣷⣶⣶⠶⠶⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⠆⢀⣤⠉⣽⣾⢶⣄⠍⢻
                ⣿⣿⣿⣿⣿⣿⣿⣿⡞⢿⣄⠈⠳⣄⠙⣿⡿⣿⣶⣄⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣏⣿⠿⢃⣴⣿⣿⣗⢻⣿⣿⣟⡛⠀
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣷⣦⣄⠱⠶⣶⣤⣌⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⡿⠉⢠⣾⣿⣿⣿⢌⣇⢻⣿⣿⣿⣷
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡙⠻⠿⠶⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡏⠁⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
        """)

    #Classroom Seat Map
    def ClassSeatMap():
        seat = 1
        for x in range(5):
            for y in range(5):
                print(f"S{seat}" , end="\t")
                seat += 1
            print()

    #Data Cleaning
    def DataClean():
        scores = [95, -1, 88, 76, -1, 100, 67]
        val_scr = []
        for score in scores:
            if score < 0:
                continue
            val_scr.append(score)

        avg = sum(val_scr) / len(val_scr)
        print(f"Scores: {scores}")
        print(f"Valid Scores: {val_scr}")
        print(f"Average Score: {avg}")

    if choice == 6:
        print("Bye dude")
        con = False
    elif choice == 1:
        AttCount()
    elif choice == 2:
        SecureLog()
    elif choice == 3:
        GradeAna()
    elif choice == 4:
        ClassSeatMap()
    elif choice == 5:
        DataClean()
    else:
        print("Invalid choice. Please try again.")