## this must be implemented in OOP, I am thinking to create one class for student record and one class for hashtable


#Design a hash function HashId() which accepts the applicant’s name as a parameter and returns the hash value
def HashId(stname):
    #to mimic the functionality intitally planning to with 
    #python dictionaries slowly remove them later once the project is executing
    pass

#This function creates an empty hash table and points to null
def initializeHash(self):
    # I suppose the project must be planned in OOPS
    pass

#This function inserts the student’s name and corresponding details into the hash table
def insertAppDetails(ApplicationRecords, name, phone, country, program, status): 
    pass

#This function finds the applicant’s details based on the name and updates the corresponding details into the hash table.
def updateAppDetails(ApplicationRecords, name, phone, country, program, status):
    pass

#This function prints the list of all applicants who have applied to a particular program
def memRef(ApplicationRecords, Program):
    pass

#This function prints the list of number of applications in their current stage 
# - of the application process including Applied, Rejected and Approved
def appStatus(ApplicationRecords):
    pass

#This function destroys all the entries inside hash table. This is a clean-up code.
def destroyHash(ApplicationRecords):
    pass
 


#VIGNESH : 23-Dec-2020
#Pending: To Word document design PS8_<group id>.docx detailing the design and time complexity of the algorithm

try:
    #Creating a new Hash table
    class HashTable:
        
        #Hash table class accepts count as input parameter
        def __init__(self,count_values):
            self.count_values=count_values    
        
        #This function Initializes the Hash table
        def initializeHash(self):
            self.hash=[[] for i in range (self.count_values)]
        
        #This function creates an HashId for name
        def HashId(self, name):
            hash = 0
            for char in name:
                hash += ord(char)
            return hash % self.count_values
        
        #This function inserts application details into the Hashtable
        def insertAppDetails(self, name, phone,country, program, status):
            h = self.HashId(name)
            found = False
            count=0
            for idx, element in enumerate(self.hash[h]):
                if len(element)==2 and element[0] == name:
                    self.hash[h][idx] = [name,[phone,country, program, status]]
                    found = True
                    
            if not found:
                self.hash[h].append([name,[phone,country, program, status]])            
            for item in self.hash:
                for item1 in item:
                    if len(item1) !=0:                    
                        count=count+1
            return "Successfully inserted "+ str(count)+ " applications into the system."
    
        #This function updates the details of an applicant
        def updateAppDetails(self, name, phone,country, program, status):
            arr_index = self.HashId(name)
            a=[]
            for kv in self.hash[arr_index]:
                if kv[0] == name:                
                    phone1=kv[1][0]
                    country1=kv[1][1]
                    program1=kv[1][2]
                    status1=kv[1][3]
                    kv[1]=[phone,country, program, status]
            if phone!=phone1 and country!=country1 and program!=program1 and status!=status1:
                return "Updated details of " + name + ". Phone Number, Resident Country, Program Applied and Application status has been changed"
            if phone!=phone1 and country!=country1 and program!=program1:
                return "Updated details of " +  name +  ". Phone Number, Resident Country and Program Applied has been changed"
            if phone!=phone1 and country!=country1 and status!=status1:
                return "Updated details of "+ name+ ". Phone Number, Resident Country and Application status has been changed"
            if phone!=phone1 and program!=program1 and status!=status1:
                return "Updated details of "+ name+ ". Phone Number, Program Applied and Application status has been changed"
            if country!=country1 and program!=program1 and status!=status1:
                return "Updated details of "+ name+ ". Resident Country, Program Applied and Application status has been changed"
            if phone!=phone1 and country!=country1:
                return "Updated details of "+ name+ ". Phone Number and Resident Country has been changed"
            if phone!=phone1 and program!=program1:
                return "Updated details of "+ name + ". Phone Number and Program Applied has been changed"
            if phone!=phone1 and status!=status1:
                return "Updated details of "+ name+ ". Phone Number and Application status has been changed"
            if country!=country1 and program!=program1:
                return "Updated details of "+ name+ ". Resident Country and Program Applied has been changed"
            if country!=country1 and status!=status1:
                return "Updated details of "+ name+ ". Resident Country and Application status has been changed"
            if program!=program1 and status!=status1:
                return "Updated details of "+ name+ ". Program Applied and Application status has been changed"
            if phone!=phone1:
                return "Updated details of "+ name+ ". Phone Number has been changed"
            if country!=country1:
                return "Updated details of "+ name+ ". Resident Country has been changed"
            if program!=program1:
                return "Updated details of "+ name+ ". Program Applied has been changed"
            if status!=status1:
                return "Updated details of "+ name+ ". Application status has been changed"
            
            
        # This function returns the list of all applicantswho have applied to a particular program
        def memRef(self, Program):
            array1=[]  
            for i in self.hash:
                if len(i)>0:
                    for j in i:
                        if len(j)>0: 
                            if j[1][2]==Program:
                                array1.append(j)                       
            return array1                                
        
        #This function returns the list of number of applications in their current stage of the application process
        def appStatus(self):
            count_applied=0
            count_approved=0
            count_rejected=0
            for i in self.hash:
                if len(i)>0:
                    for j in i:
                        if len(j)>0:                         
                            if j[1][3] == 'Applied':
                                count_applied=count_applied+1
                            if j[1][3] == 'Approved':
                                count_approved=count_approved+1
                            if j[1][3] == 'Rejected':
                                count_rejected=count_rejected+1
                                
            return "Applied: "  + str(count_applied) + " Approved: " + str(count_approved) + " Rejected: " + str(count_rejected)
        
        #This function destroys all the entries inside hash table.
        def destroyHash(self):
            self.hash=[[]]
            
            
    #Reading the input and prompt files
    f = open(r"C:\Users\vigne\Desktop\vignesh\inputPS8.txt", "r")
    update_file = open(r"C:\Users\vigne\Desktop\vignesh\promptsPS8.txt", "r")
    
    #Fetching count of records from the input file
    zz=[]
    count_values=0
    for x in f:
        count_values=count_values+1
        zz.append(x.split('/'))
    count_values
    
    #Fetching details of records from the prompt file
    prompt=[]
    for x in update_file:
        prompt.append(x.split(':'))
    prompt
    
    #Splitting the prompt file based on conditions
    update=[]
    program=[]
    appstatus=[]
    for item in prompt:
        if len(item)>0:
            if item[0].upper().strip() == 'update'.upper():
                update.append(item[1])
            if item[0].upper().strip() == 'program'.upper():
                program.append(item[1])        
        elif item[0].upper().strip() == 'appstatus'.upper():
            appstatus.append(item[0])
            
    update_final=[]
    for item in update:
        update_final.append(item.split('/'))
    update_final
    
    #Creating an instance of the Hashtable class
    t=HashTable(count_values)
    
    #Creating and Hashtable
    t.initializeHash()
    output=[]
    
    #Inserting details of applicants into the hashtable
    for item in zz:
        a=t.insertAppDetails(item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip(),item[4].strip())
    output.append(a)
    
    
    #Updating details of applicants in the Hashtable
    for item in update_final:
        output.append(t.updateAppDetails(item[0].strip(),item[1].strip(),item[2].strip(),item[3].strip(),item[4].strip()))
    output
    
    #Listing of all applicantswho have applied to a particular program
    memref=[]
    memref1=[]
    for item in program:
        to_append = "---------- Applicants for " + item.strip() + " ----------"
        output.append(to_append)
        memref.append(t.memRef(Program=item.strip()))
        for item in memref:
            for item1 in item:
                string_concat=item1[0] + ' / ' + item1[1][0] + ' / ' + item1[1][1] + ' / ' + item1[1][2] + ' / ' + item1[1][3]         
                output.append(string_concat)
    output.append("-------------------------------------")
    output.append("---------- Application Status ----------")
    
    
    #Listing number of applications in the current stage of the application process
    output.append(t.appStatus())
    output.append("-------------------------------------")
    
    #Printing the output to an output file
    with open(r"C:\Users\vigne\Desktop\vignesh\outputPS8.txt", "w") as output1:
        for item in output:
            output1.write(str(item) + '\n')

except:
    with open(r"C:\Users\vigne\Desktop\vignesh\outputPS8.txt", "w") as output1:
        output1.write('Input file format error')
