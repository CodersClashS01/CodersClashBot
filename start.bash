pyexec="python"

if type python3 >/dev/null 2>&1
then 
    pyexec="python3"
fi

if type py >/dev/null 2>&1
then 
    pyexec="py"
fi

if [ -z $1 ]
then
    echo "Please set the bots token as first arguemtn of this script!"
    exit -1
fi

$pyexec src/main.py $1