:: this bat file is used to set git repository
:: to run use .\set_git.bat
@echo off
:: add :: before the next row to initialize the repository
::exit /b

::git init
git remote remove origin
git remote add origin https://github.com/TameerAmer/Capstone-Project.git
git branch -M Python_Code_OptiVision
git push -u origin Python_Code_OptiVision
