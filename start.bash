pyexec="python"

if type python3 >/dev/null 2>&1
then 
    pyexec="python3"
fi

if type py >/dev/null 2>&1
then 
    pyexec="py"
fi

if [ -z $DEVBOTTOKEN ]
then
    echo "Please set the bots token as envoirement variable 'CCBOTTOKEN'!"
    exit -1
fi

$pyexec src/main.py