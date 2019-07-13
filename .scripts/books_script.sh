printer1=""

for folder in /home/prin/Dropbox/_books/*/
do
    folder=${folder:26:-1}
    printer1="$printer1
$folder"
done

printer1=${printer1:1}
category=$(echo "$printer1" | rofi -dmenu -p category)

if [$category = '']
then
    exit 0
fi

printer2=""

for file in /home/prin/Dropbox/_books/$category/*
do
    file=${file##*/}
    file=${file::-4}
    printer2="$printer2
$file"
done

printer2=${printer2:1}
book=$(echo "$printer2" | rofi -dmenu -p book)

if [$book = '']
then
    exit 0
fi

$(zathura "/home/prin/Dropbox/_books/$category/$book.pdf")
