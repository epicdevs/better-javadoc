# better-javadoc
**better-javadoc** makes javadocs as commentable documents. Each package and class has its own separate commenting thread so people can post questions and discussions directly on the related javadoc.

## JDK Support
Currently I only tested it to javadocs generated with JDK 1.7.

## Demo
[http://epicdevs.github.io/better-javadoc-example/](http://epicdevs.github.io/better-javadoc-example/)

## HOW-TO

### 1. Copy files
- Copy `better-javadoc.js` and `better-javadoc.css` to the javadoc directory.

### 2. Configure better.py
- Modify `href` and `src` of variable `rep` to a proper path so that each html can access `better-javadoc.js` and `better-javadoc.css` when uploaded on the server.

### 3. Configure better-javadoc.js
- Change `disqus_shortname` to your own [disqus](http://disqus.com) site name.

### 4. Run better.py
    python better.py javadoc-directory
