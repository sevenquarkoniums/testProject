# some useful functions.
import pytz,datetime
import pandas as pd
from subprocess import call

def unix2string(unixTime, timezone='US/Pacific'):
    '''
    Convert unix time into time string at a certain timezone.
    '''
    pacific = pytz.timezone(timezone)
    thisTime = datetime.datetime.utcfromtimestamp(unixTime).replace(tzinfo=datetime.timezone.utc).astimezone(tz=pacific)
    timestr = thisTime.strftime('%Y-%m-%d %H:%M:%S')
    return timestr

def unix2pdTime(unixTime, timezone='US/Pacific'):
    '''
    Convert unix time into pandas time.
    '''
    return pd.Timestamp(unixTime, unit='s', tz=timezone)

def string2unix(timeString):
    '''
    Convert time string into unix time.
    '''
    return datetime.datetime.strptime(timeString, '%m/%d/%Y, %H:%M:%S%z').timestamp()

def getfiles(folder):
    # get all the files in a certain folder with full path.
    fileList = []
    for root, directories, files in os.walk(folder):
        for filename in files:
            filepath = os.path.join(root, filename)
            fileList.append(filepath)
    return fileList

def submit(script='name.py', shfile='run.sh', outfile='output.out', system='cori'):
    '''
    submit a batch job.
    '''
    fsh = open(shfile, 'w')
    line = '#!/bin/bash -l\n'
    if system == 'cori':
        line += 'module load python/3.6-anaconda-5.2\n'
        line += 'export HDF5_USE_FILE_LOCKING=FALSE\n'
    line += '%s\n' % script
    fsh.write(line)
    fsh.close()

    command = 'chmod +x \'%s\'\n' % shfile
    call(command, shell=True)

    if system == 'cori':
        command = 'sbatch -N 1 -C haswell --qos=premium -t 9:00:00 -o %s %s' % (outfile, shfile)
    call(command, shell=True)
