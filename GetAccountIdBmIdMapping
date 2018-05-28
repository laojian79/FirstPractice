# Access Cassandra DB to get something
print('Populating user id and video Id into file')
import sys, Common
from pymongo.errors import ConnectionFailure
import datetime

def main():
    """ Connect to Cassandra DB """
try:
    cluster = Common.GetCassandraDBCluster()
    session = cluster.connect(Common.subscriberdbName)
    print("Connect to cassandradb(subscriber) Successfully.")

    rows = session.execute('SELECT * FROM bookmarks WHERE userid=\'scale_000010684\' AND isadult=False AND querytype=0 AND queryvalue=\'\';')
    with open('.\\svod\\accountBookmarkId_0010684.csv', 'w') as f:
        for row in rows:
            f.write(row.userid + ',' + row.videoid + '\n')
            print(row.userid + row.videoid)
    
    print('Write complete.')
except ConnectionFailure as e:
    print('Could not connect to Cassandra DB: %s' % e)

finally :
    if cluster is not None and not cluster.is_shutdown:
        cluster.shutdown()

