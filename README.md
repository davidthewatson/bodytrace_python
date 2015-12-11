This example shows how to retrieve weight, battery, and signal strength from the BodyTrace Scale API.

http://www.bodytrace.com/medical/

Setup the input files as follows:

auth.txt should contain two lines:

    username@example.com
    password

imei_list.txt should contain one or more lines where each line is an IMEI ID from the back of a scale:

    1234567890

uri.txt should contain a single line with the URL of the bodytrace API:

    https://us.data.bodytrace.com/1/device/{}/datavalues?names=batteryVoltage,signalStrength,values/weight,values/unit

Create a virtualenv and activate it:

    mkvirtualenv -p `which python` bodytrace_python

Note: I use the -p flag here for a reason. The version of python 2.7 that ships with Mac OS X has a defective openSSL lib. Therefore, I run a brewed python from /usr/local/bin/python. The flag containing *which python* makes sure that we use the brewed python with a working openSSL, which is a requirement for the python requests module used in this code.

Then install requirements:

    pip install -r requirements.txt

And run:

    python bodytrace_python.py
