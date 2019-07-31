#!/bin/bash

version=2.0.0

rm -r rhoplusGUI-$version/opt
rm -r rhoplusGUI-$version/bin

mkdir rhoplusGUI-$version/opt
mkdir rhoplusGUI-$version/opt/rhoplusGUI
mkdir rhoplusGUI-$version/bin

cd rhoplusGUI-$version/opt/rhoplusGUI

cp -r ../../../../* .

rm -r PACKAGE
rm rhoplusGUI

cd ../../bin
cp ../../../rhoplusGUI .

cd ../../
dpkg -b rhoplusGUI-$version
