#!/usr/bin/sh

green=#55aa55


if pgrep -x "picom" > /dev/null
then
  echo %{u"$green"}{F"$green"} 
else
  echo 
fi
