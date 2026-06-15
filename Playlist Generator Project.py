import random
import csv


chosen_genres = []
chosen_moods = []
used_cases1 = []
used_cases2 = []
chosen_songs_genres = []
chosen_songs_moodes = []
filtered1 = []
filtered2 = [] # creates a list that i can filter my dictionary points through

generated_playlist = []

# store moods or genres in a list (up to 3)
def picked_genres():
    print("[1] Rap/Hip-Hop")
    print("[2] Pop")
    print("[3] Rock")
    print("[4] Country")
    print("[5] Jazz")
    print("[6] Generate Playlist")
    print("Choose up to 3 genres twinny")
    pick1 = int(input ("choose yo genre: "))
    count1 = 0
    
    while pick1 != 6 and count1 < 2:
        
        if pick1 in used_cases1:
            print("You can only do a genre one time gang") #add say which genres are already picked
        match pick1:

            case 1 if 1 not in used_cases1:
                chosen_genres.append("Rap/Hip-Hop")
                used_cases1.append(1)
                count1 = count1 +1
                
            case 2 if 2 not in used_cases1:
                chosen_genres.append("Pop")
                used_cases1.append(2)
                count1 = count1 +1
                
            case 3 if 3 not in used_cases1:
                chosen_genres.append("Rock")
                used_cases1.append(3)
                count1 = count1 +1
                
            case 4 if 4 not in used_cases1:
                chosen_genres.append("Country")
                used_cases1.append(4)
                count1 = count1 +1
                
            case 5 if 5 not in used_cases1:
                chosen_genres.append("Jazz")
                used_cases1.append(5)
                count1 = count1 +1
                
        pick1 = int(input ("choose yo genre twizzard: "))
        if count1 == 1:
            print("One genre remaining")
            
    else:
        print("Generating Playlist...")
        


def picked_moods():
    print("[1] Upbeat")
    print("[2] Mellow")
    print("[3] Depressing")
    print("[4] Yearning")
    print("[5] Hoodlum")
    print("[6] Generate Playlist")
    print("Choose up to 3 moods slimeski")
    pick2 = int(input("Choose yo mood slime: "))
    count2 = 0
    

    while pick2 != 6 and count2 < 2:
        match pick2:
            case 1 if 1 not in used_cases2: #if "case1" isnt in the list "used cases"
                chosen_moods.append("Upbeat")
                used_cases2.append(1)
                count2 = count2 +1
            case 2 if 2 not in used_cases2:
                chosen_moods.append("Mellow")
                used_cases2.append(2)
                count2 = count2 +1
            case 3 if 3 not in used_cases2:
                chosen_moods.append("Depressing")
                used_cases2.append(3)
                count2 = count2 +1
            case 4 if 4 not in used_cases2:
                chosen_moods.append("Yearning")
                used_cases2.append(4)
                count2 = count2 +1
            case 5 if 5 not in used_cases2:
                chosen_moods.append("Upbeat")
                used_cases2.append(5)
                count2 = count2 +1
        pick2 = int(input("Choose yo mood slime: "))
        if count2 == 1:
            print("One mood remaining")

        else:
            print("Generating Playlist...")

#csv reading stuff


def csv_handling_genres():
    with open(r"Playlist generator project\songs.csv", newline="") as songs1:
        song_puller1 = csv.DictReader(songs1)
        
        for row in song_puller1:
            if row['Genre'] in chosen_genres:
                filtered1.append({row['Artist'], row['Title']})
        
        generated_playlist.extend(random.sample(filtered1, song_number)) #adds a random 
        print(generated_playlist)

def csv_handling_moods():
    with open(r"Playlist generator project\songs.csv", newline="") as songs2:
        song_puller2 = csv.DictReader(songs2) #opens the csv using the dict reader function (reads csv file as dictionary so i dont have to do "header = next(row)")
     
        for row in song_puller2: #for loop that look through each row that contains a matching mood compared to chosen mood
            if row['Vibe'] in chosen_moods:
                filtered2.append({row['Artist'], row['Title']}) #brackets make t so it reads from the dict, row makes it only take from those 2 rows of the dict append writes it to that list
                
        generated_playlist.extend(random.sample(filtered2, song_number)) #choses n songs from filtered list and extends the playlist instead of appending it so there are no nested lists
        print(generated_playlist)
# start main loop
def clear_lists():
    chosen_genres.clear()
    chosen_moods.clear()
    count1 = 0
    count2 = 0
    used_cases1.clear()
    used_cases2.clear()
    generated_playlist.clear()
    filtered1.clear()
    filtered2.clear()
run = True

while run:
    #clear all lists
    clear_lists
    

    # welcome user 
    print("We making a playlist twin!")

    # ask for number of songs
    song_number = int(input("How many songs twin? "))
    if song_number < 1: 
        print("You gotta have some songs gang, one more time")
        
    elif song_number > 20:
        print("Only 20 songs twinski; one more time")
        
    else:
        # ask if genre or mood based
        genre_or_mood = int(input("We basing this on genre or mood twin? (1 is genre, 2 is mood):  "))
        if genre_or_mood != 1 and genre_or_mood != 2:
            print("That aint a valid option twin, try again")
        else:
            match genre_or_mood:
                case 1:
                    picked_genres()
                    # read csv file
                    csv_handling_genres()
                    regen1 = int(input("Generate again? "))
                    match regen1: 
                        case 1:
                            clear_lists()
                            run = True
                        
                        case 2:
                            print("Bye Bye Crosski")
                            run = False

                case 2:
                    picked_moods()
                    csv_handling_moods()
                    regen2 = int(input("Generate again twin?"))
                    match regen2: #match case for regen 2 int variable
                        case 1:
                            clear_lists()
                            run = True #playlist generator loop continues
                        case 2:
                            print("Bye Bye Croski")
                            run = False #game over twin
                    