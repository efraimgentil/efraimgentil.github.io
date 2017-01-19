import os
from distutils import dir_util


my_git = "git@github.com:efraimgentil/efraimgentil.github.io.git";

os.system( "jekyll build")

print("### CREATING THE COMMIT DIR ###")
os.system("mkdir tocommit")
os.chdir("tocommit")
os.system( "git init")
os.system( "git remote add origin %s" % my_git )
os.system( "git pull origin master" )


dir_util.copy_tree("../_site", "../tocommit")

os.system( "git status")

print("### LIMPANDO PASTA TOCOMMIT ###")
os.chdir("..")
os.system("rm -rf tocommit")
