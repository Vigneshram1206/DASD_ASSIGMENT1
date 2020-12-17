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
 


#VIGNESH : 18-Dec-2020
#Created a class Hashtable with the functions without LinkedList concept. Needs to be updated with LinkedList and futher fine tunings

class HashTable:
    
    def __init__(self):
        self.Max=10    
    
    def initializeHash(self):
        self.hash=[None for i in range (self.Max)]
    
    def get_hash(self, name):
        hash = 0
        for char in name:
            hash += ord(char)
        return hash % self.Max
    
    def insertAppDetails(self,name, phone, country, program, status):
        h=self.get_hash(name)
        count=0
        self.hash[h]=[phone, country, program, status]
        for i in self.hash:
            if i != None:
                count=count+1
        return (print("Successfully inserted", count, "applications into the system."))
    
    def updateAppDetails(self,name, phone, country, program, status):
        h=self.get_hash(name)
        count=0
        if self.hash[h][0] != None: 
            if self.hash[h][0]!=phone:
                self.hash[h][0]=phone
                count=1
        if count==1:
            return (print("Updated details of ", name, ". Phone has been changed"))
        
    def memRef(self, Program):
        array1=[]
        for i in self.hash:
            if i!=None:
                if i[2]==Program:                
                    array1.append(i) 
        return array1                                
    
    def appStatus(self):
        count_applied=0
        count_approved=0
        count_rejected=0
        for i in self.hash:
            if i != None:
                if i[3] == 'Applied':
                    count_applied=count_applied+1
                if i[3] == 'Approved':
                    count_approved=count_approved+1
                if i[3] == 'Rejected':
                    count_rejected=count_rejected+1
        return (print('Applied' , count_applied, 'Approved' ,count_approved, 'Rejected',count_rejected))
    
    def destroyHash(self):
        self.hash=[]
        
