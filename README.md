### Personal Blog





### Publishing to master 

User the docker mage generated from the Dockerfile in this project 
```
docker build . -t blog-builder
```


Run the command in the image to compile and generate the static files for the blog
```
docker run -v ${PWD}:/app blog-builder jekyll build --verbose
```

The command will generate a `_site` folder that contains all static files for the blog,
access this file and 

```
git init
git remote add origin MY_REPOSITORY
git pull origin master

git add .
git commit -m "MY BLOG UPDATE" 
git push origin master 
```