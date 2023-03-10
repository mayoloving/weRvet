#!/bin/bash

t=$(git tag -l | sort -V | tail -1)
major=$(git tag -l | sort -V | tail -1 | cut -d"." -f"1")
minor=$(git tag -l | sort -V | tail -1 | cut -d"." -f"2")
line=$(git tag -l | sort -V | wc -l)
s=$major.$minor

if [ -z "$(git tag -l | sort -V)" ];
then
    echo "no tags were entered yet by coders"
elif [ "$line" == "1" ] && [ "$t" == "$s" ];
then
    major=$(git tag -l | sort -V | tail -1 | cut -d"." -f"1")
    minor=$(git tag -l | sort -V | tail -1 | cut -d"." -f"2")
    val=$major.$minor.1


    echo "1"
    git tag $val HEAD
    git push https://github.com/mayoloving/weRvet.git $val
else
    majorlast=$(git tag -l | sort -V | tail -1 | cut -d"." -f"1")
    minorlast=$(git tag -l | sort -V | tail -1 | cut -d"." -f"2")
    major=$(git tag -l | sort -V | tail -2 | head -1 | cut -d"." -f"1")
    minor=$(git tag -l | sort -V | tail -2 | head -1 | cut -d"." -f"2")

    if [ "$major" == "$majorlast" ] && [ "$minor" == "$minorlast" ];
    then
        num=$(git tag -l | sort -V | tail -1 | cut -d"." -f"3")
        num=$(($num+1))
        val=$major.$minor.$num
        echo "2"
        git tag $val HEAD
        git push https://github.com/mayoloving/weRvet.git $val
    else
        val=$majorlast.$minorlast.1


        echo "3"
        git tag $val HEAD
        git push https://github.com/mayoloving/weRvet.git $val
    fi
fi
