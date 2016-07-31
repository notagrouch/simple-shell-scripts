#!/usr/bin/env bash

echo "the URL is blank"
echo ""
echo "enter the URL"
read URL
echo ""
echo ""
	url={$URL}
echo ""
echo ""
echo "The URL set is:"
echo "$URL"
echo ""
echo ""
echo "opening $URL with Chrome incognito"
echo ""
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --new --args -incognito "$URL" &
echo ""
echo ""
echo "opening $URL with Firefox private"
echo ""
/Applications/Firefox.app/Contents/MacOS/firefox-bin -private-window "$URL" &
echo ""
echo ""
echo "opening $URL with Opera private"
echo ""
/Applications/Opera.app/Contents/MacOS/Opera -private "$URL" &
echo ""
echo ""
echo "opening $URL with Vivaldi private"
echo ""
/Applications/Vivaldi.app/Contents/MacOS/Vivaldi --incognito "$URL" &
