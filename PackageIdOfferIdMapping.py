# Connect to Cassandra
print('Populating Category id and Package Id into SQL')
import sys, Common
from pymongo.errors import ConnectionFailure
import datetime

def main():
    """ Connect to MongoDB """
try:
    c = Common.GetMongoDBConnection()
    print("Connected to mongo successfully")

    # Get a Database handle to a database 
    dbh = c[Common.mongodbName]
    
    # Find categoryid for a particular packageId
    packageNamePrefix='scale_vodpackage_'
    packages  = dbh.packages.find({"Type":"TVOD","Name.Value":{"$regex":packageNamePrefix}})
    # categoryIdList  = dbh.categories.distinct("_id")        

    utcEndtime = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    with open('.\svod\PackageIdOfferId.txt', 'w') as f:
        for package in packages:
            f.write(package.get('_id') + '\n')
            offers = package.get("Offers")
            if offers:
                for offer in offers:
                    #if offer.get("EndUtc") > utcEndtime:
                    #f.write(package.get('_id') + ',')
                    #f.write(offer.get('_id') + '\n')
                    print(offer.get('_id'))

    print('Write complete.')
except ConnectionFailure as e:
    print('Could not connect to MongoDB: %s' % e)

finally :
    if c is not None: c.close()

