class Querying:
    """
    This class defines the various methods required for querying using OKAPI BM-25 Algorothm
    """

    
    def __init__(self,N=0,query='',usID='sagar',pswd='toor@123',dbase='IR_assign',hst='localhost'):
        """
        Constructor for Querying object
        """
        self.userID=usID
        self.password=pswd
        self.database = dbase
        self.host = hst
        self.stemming='porter'
        self.n=N
        self.k1=1.5  
        self.b=0.75
        self.query=query
        try:
            self.db = MySQLdb.connect(self.host, self.userID, self.password, self.database)
        except:
            print 'Error initialising database'

    def __del__(self):
        self.db.close()
    
    