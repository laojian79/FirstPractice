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

    #Scan bookmark, get how many BMs for each account
    with open('.\\svod\\bookmarkGt500.csv', 'w') as f:
        index = 10685
        while index <= 350000:
            account=('000000000'+str(index))[-9:]
            account = 'scale_tls_' + account
            #len(list(rows))
            rows = session.execute('SELECT count(*) FROM bookmarks WHERE userid=\'%s\' AND isadult=False AND querytype=0 AND queryvalue=\'\';'% account)
            for row in rows:
                if row is not None:
                    count = row.count
                    f.write(account + ',' + str(count) + '\n')
                    print('%s, %d' % (account,count))
                
            index+=1
    
    print('Write complete.')
except ConnectionFailure as e:
    print('Could not connect to Cassandra DB: %s' % e)

finally :
    if cluster is not None and not cluster.is_shutdown:
        cluster.shutdown()

