# BodyTrace API Example using Python and Requests

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

Then install requirements:

    pip install -r requirements.txt

And run:

    python bodytrace_python.py
