cd build/
#rm -r build/
rm -r dist/
#
#source ~/.virtualenvs/bumbum/bin/activate
#export QT5DIR=/usr/local/Cellar/qt/5.8.0_2/
#
#pyinstaller ../bumbum/bumbum.py --add-data '../bumbum/gui:gui' -w -y

pyinstaller bumbum.spec -y


# remove unnecessary files
echo
echo Remove unnecessary files
echo

cd dist/bumbum/

rm Qt3D*
rm QtXmlPatterns
rm QtGamepad
rm QtSvg
rm QtSql
rm QtQuickTemplates2
rm QtQuickParticles


cd ../../
cd dist/bumbum.app/Contents/MacOS/
rm Qt3D*
rm QtXmlPatterns
rm QtGamepad
rm QtSvg
rm QtSql
rm QtQuickTemplates2
rm QtQuickParticles

echo Done
