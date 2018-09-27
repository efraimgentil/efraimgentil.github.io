import os
from distutils import dir_util

my_git = "https://github.com/efraimgentil/efraimgentil.github.io.git"

current_path = os.getcwd()

print("# Building docker image for building process")
os.system("docker build . -t blog-builder")

print("## Running build process")
os.system("docker run -v " + current_path + ":/app blog-builder jekyll build")

print("### CREATING THE COMMIT DIR ###")
os.system("mkdir tocommit")
os.chdir("tocommit")
os.system( "git init")
os.system( "git remote add origin %s" % my_git )
os.system( "git pull origin master" )


dir_util.copy_tree("../_site", "../tocommit")

os.system( "git status")

os.system( "git add .")

os.system( "git commit -am 'Update blog'")

os.system( "git push origin master")

print("#### LIMPANDO PASTA TOCOMMIT ###")
os.chdir("..")
os.system("rm -rf tocommit")
