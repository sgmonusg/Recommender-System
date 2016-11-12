import MySQLdb
import sys
import os
import logging


class database:
    
    """
	This class defines the database that is used to create the bag-of-words representation

	"""
    
    def __init__(self,usID='sagar', pswd='toor@123', dbase='IR_assign', hst='localhost'):
        self.userID = usID
        self.password = pswd
        self.database = dbase
        self.host = hst
        self.N = 0
        try:
            self.db = MySQLdb.connect(self.host, self.userID, self.password, self.database)
            logging.info('Able to connect to database')
        except:
            logging.error('Error initialising database')

    def __del__(self):
        self.db.close()

    def create_Rating_table(self):    
        """This function creates the table Rating Table which stores all rating and userid """
		#prepare the cursor
        cursor=self.db.cursor()
        sql='''CREATE TABLE  RATING(
                USER_ID INT,
                MOVIE_ID INT,
                RATING VARCHAR(50),
                PRIMARY KEY(User_ID) 
                )'''
        try:
            cursor.execute(sql)
            logging.info("Created table DOC_FREQ")
        except:
            logging.warning("Could not create table DOC_FREQ. Table may already be existing")
        finally:
            cursor.close()


    def create_Movie_table(self):    
        """This function creates the table Movie Table which stores all movieid and year as well as name of the movie """
        #prepare the cursor
        cursor=self.db.cursor()
        sql='''CREATE TABLE  MOVIE(
                MOVIE_ID INT,
                Year INT,
                Name VARCHAR(50),
                PRIMARY KEY(Movie_ID) 
                )'''
        try:
            cursor.execute(sql)
            logging.info("Created table DOC_FREQ")
        except:
            logging.warning("Could not create table DOC_FREQ. Table may already be existing")
        finally:
            cursor.close()    

    def add_to_Rating_Table(self,User_ID,Movie_ID,Rating):
        """This function adds User_id , id of the movie they rated and the rating of the movie to the rating table """
        cursor=self.db.cursor();
        sql="INSERT into RATING values ('"+str(User_ID)+"','"+str(Movie_ID)+"','"+str(Rating)+"')"
        #print sql
        try:
            cursor.execute(sql)
            logging.info("Added User_ID: "+str(User_ID)+" Movie_ID: "+str(Movie_ID)+" Rating: "+str(Rating)+" into Rating_table")
            self.db.commit()
        except:
            logging.error("Error adding User_ID: "+str(User_ID)+" Movie_ID: "+str(Movie_ID)+" Rating: "+str(Rating)+" into Rating_table")
        finally:
            cursor.close()

    def add_to_Movie_Table(self,Movie_ID,Year,Name):
        """This function adds Movie_ID and Year of the movie and the name of it to the movie table"""
        cursor=self.db.cursor();
        sql="INSERT into MOVIE values ('"+str(Movie_ID)+"','"+str(Year)+"','"+Name+"')"
        #print sql
        try:
            cursor.execute(sql)
            logging.info("Added MovieId: "+str(Movie_ID)+" Year: "+str(Year)+" Name: "+Name+" into MOVIE")
            self.db.commit()
        except:
            logging.error("Error adding MovieId:"+str(Movie_ID)+" Year:"+str(year)+"  Name: "+Name+" into MOVIE")
        finally:
            cursor.close()

    def update_Rating_table(self, USER_ID , MOVIE_ID ,RATING):
        cursor=self.db.cursor();
        sql="UPDATE RATING SET RATING='"+str(RATING)+"' WHERE USER_ID"

   
    def set_no_of_doc(self,N):
    	"""
    	Sets the number of documents in database
    	"""
    	self.N=N
    
    def get_no_of_doc(self):
    	"""
    	Gets the number of documents in database
    	"""
    	return self.N 
    
    def set_total_words(self,N):
    	"""
    	Sets the total number of words in database
    	"""
    	self.total_words=N
    
    def get_total_words(self):
    	"""
    	Gets the total number of words in database
    	"""
    	return self.total_words  
