import cgi, os, sys
import sqlite3 as db
import pymysql as mysql
import datetime

for i in range(364):
    count = 0
    t_str = '2015-01-02'
    d = datetime.datetime.strptime(t_str, '%Y-%m-%d')
    d = (d + datetime.timedelta(days=i)).strftime("%Y%m%d")

    conn = db.connect("E:\\badou\\airdata\\"+str(d)+'.db')
    cursor = conn.cursor()
    conn.row_factory = db.Row
    cursor.execute("select station, time, OBSSTATIONTYPE, lowestch,VISIBLITY,CAMOUNT,WD,WS,AT,TD,RH,"
                   "STATIONP,SEAP,CODEP,CODEH,CHANGEP3_IDX,CHANGEP3,PRECIPITATION,RAINTIMECODE,WW,"
                   "PASTWW1,PASTWW2,LOWCAMOUNT,LOWCTYPE,MIDCTYPE,HIGHCTYPE,OBSTIME2,CHANGEP24,"
                   "CHANGET24,HIGHT24,LOWT24,LOWSURT,SNOWSURFTYPE,SNOWHIGHT,PRECI24,LAYERCLOUDAMOUT,LAYERCLOUDTYPE,LAYERCLOUDHIGHT,SP"
                   " from ZR_SURF01_ELE")
    result = cursor.fetchall()

    conn2 = mysql.connect(
            host='localhost',
            port = 3306,
            user='root',
            passwd='123456',
            db ='airdata',
            charset='utf8'
            )
    cur = conn2.cursor()

    sql = "insert into weather (station, time, OBSSTATIONTYPE, lowestch,VISIBLITY,CAMOUNT,WD,WS,AT,TD,RH," \
          "STATIONP,SEAP,CODEP,CODEH,CHANGEP3_IDX,CHANGEP3,PRECIPITATION,RAINTIMECODE,WW," \
          "PASTWW1,PASTWW2,LOWCAMOUNT,LOWCTYPE,MIDCTYPE,HIGHCTYPE,OBSTIME2,CHANGEP24," \
          "CHANGET24,HIGHT24,LOWT24,LOWSURT,SNOWSURFTYPE,SNOWHIGHT,PRECI24,LAYERCLOUDAMOUT,LAYERCLOUDTYPE,LAYERCLOUDHIGHT,SP) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s, " \
          "%s, %s, %s, %s, %s, %s, %s,%s,%s, " \
          "%s, %s, %s, %s, %s, %s,%s,%s, " \
          "%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    for line in result:
        count = count+1
        cur.execute(sql, line)

        if(count % 50000 == 0):
            conn2.commit()

    conn2.commit()

cur.close()
conn2.close()

