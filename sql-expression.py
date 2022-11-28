from sqlalchemy import (
    cerate_engine, Table, Colum, Float, ForeignKey, Interger, String, MetaData
)

#executing the instruction from our localhost "chinook" db
db = create_engine("postgresql:///chinook") #the thee /// signify that our db is hosted locallywithin our workspace environment

meta = MetaData(db) #metaDAta is recursive data about data