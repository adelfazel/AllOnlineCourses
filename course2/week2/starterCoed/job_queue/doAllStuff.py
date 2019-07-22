import os
import subprocess
import time
import datetime


testName="testBase.txt"
naiveSolName="naiveSol.txt"
mySolName="mySol.txt"
tNaive=datetime.timedelta(0)
tMy=datetime.timedelta(0)
for _ in range(10):
    f=open(testName,'w')
    subprocess.call(['python3','createTest.py'],stdout=f)
    #print("testCreated")
    f.close()
    f=open(naiveSolName,'w')

    now1 = datetime.datetime.now()
    subprocess.call('cat %s | python3 naive.py'%(testName),stdout=f,shell=True)
    now2 = datetime.datetime.now()
    tNaive+=now2-now1
    f.close()
    #print("naive answer created")
    f=open(mySolName,'w')
    now1 = datetime.datetime.now()
    subprocess.call('cat %s | python3 job_queue.py'%(testName),stdout=f,shell=True)
    now2 = datetime.datetime.now()
    tMy+=now2-now1
    f.close()
    #print("my answer created")
    subprocess.call('python3 compare.py',shell=True)
print("mySol: %s:%s" %(str(tMy.seconds)  ,str(int(tMy.microseconds/1000) )))
print("Naive: %s:%s" %(str(tNaive.seconds),str(int(tNaive.microseconds/1000))))
