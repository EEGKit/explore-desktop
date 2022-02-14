@REM @echo off
@REM Check we are in master branch

git branch | find "* master" > NUL & IF ERRORLEVEL 1 (
    echo "Please checkout to master branch and try again!"
    exit
)


@REM # Conda virtual env
call conda config --append channels conda-forge
call conda create -n gui_installer python=3.8.10 -y
call conda activate gui_installer
call python -m pip install --upgrade pip

@REM Install qt and qt-ifw (TO BE USED IN FUTURE)
@REM mkdir temp || rm -rfv temp/*
@REM cd temp
@REM pip install aqtinstall
@REM aqt install-qt linux desktop 6.2.1
@REM aqt install-tool linux desktop tools_ifw
@REM aqt install-tool linux desktop tools_maintenance
@REM cd ..

@REM Install Pyinstaller
call pip install pyinstaller==4.7

@REM Install ExploreGUI
call pip install -e .

@REM  Clean required directories
call set exploregui_path="installer\ExploreGuiInstaller\ExploreGUI\packages\com.Mentalab.ExploreGUI\"
call rd /S /Q %exploregui_path%data
call md %exploregui_path%data
call rd /S /Q dist

@REM Create executable files
call pyinstaller --onedir --console ExploreGUI.spec

@REM Copy files to data dir
call xcopy /I /E /H /R /Q dist\ExploreGUI %exploregui_path%data\ExploreGUI
call xcopy %exploregui_path%extras\MentalabLogo.ico %exploregui_path%data


@REM Create installer file
call set config_path= "installer\ExploreGuiInstaller\ExploreGUI\config\config.xml"
call set package_path="installer\ExploreGuiInstaller\ExploreGUI\packages"
call C:\Qt\QtIFW-4.2.0\bin\binarycreator -c %config_path% -p %package_path% --verbose ExploreGUIInstaller.exe