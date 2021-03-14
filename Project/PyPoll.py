# -*- coding: UTF-8 -*-


# Add our dependencies.
from datetime import date, time, datetime
import csv
import os

# Add a variable to load a file from a path
file_to_load = os.path.join("Project", "election_result.csv")

# Add a variable to save the file to a path.
file_to_save = os.path.join("Project", "election_analysis.txt")

# Intial total votes before opening the csv 

total_votes = 0

# Canditae options and candidate votes
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

#Track winning candidare, vote count and percentage
winning_candidate = ""
winning_votes = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_county_voter = 0

#Read the dictionary and convert it into a list of dictionaries
with open(file_to_load) as election_data:
   # print(election_data)
   
# Now we read and analyze our data

    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    #For eac row in the CSV File
    for row in file_reader:
        #Add to the total vote count
        total_votes +=1
        
        #Get the candiate name from each row
        candidate_names = row[2]
        
        # 3: Extract the county name from each row.
        county_name = row[1]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
    
        if candidate_names not in candidate_options:
        
            candidate_options.append(candidate_names)
            
            candidate_votes[candidate_names] = 0
    
        candidate_votes[candidate_names] += 1
        
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
            #county_list.append(county_name)


            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)


            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0


        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1
        
# Save the results to a text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-----------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-----------------------\n"
        f"\nCounty Votes:\n"
        
    )
    
    print(election_results, end="")
    
    txt_file.write(election_results)
    
    
    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        

        # 6b: Retrieve the county vote count.
        votes_count = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        county_percentage = float(votes_count)/float(total_votes)*100


         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county_name}: {county_percentage: .1f}% ({votes_count:,})\n"
         )
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if votes_count > largest_county_voter:
             
             largest_county_voter = votes_count
             largest_county = county_name


    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary =(
        
        f"----------------------------------------------\n"
        f"Largest county turnout: {largest_county}\n"
        f"----------------------------------------------\n"
    )
    
    print(winning_county_summary)


    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

        
    for candidate_names in candidate_votes:
        votes = candidate_votes[candidate_names]
    # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
       # print(f"{candidate_names}:{vote_percentage:.1f}% ({votes:,})\n")
        candidate_results =(f"{candidate_names}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results) 
        
        if(votes > winning_votes) and (vote_percentage > winning_percentage):
            winning_votes = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_names
        #print(f"{candidate_names}: {vote_percentage:.1f}% ({votes:,})\n")
     
    # Print the winning candiate to terminal
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_votes:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
     
    
        


