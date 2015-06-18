# better-javadoc
Currently I only tested it to javadocs generated with JDK 1.7.

## Demo
[http://epicdevs.github.io/better-javadoc-example/](http://epicdevs.github.io/better-javadoc-example/)

## HOW-TO

### 1. Copy files
- Copy `better-javadoc.js` and `better-javadoc.css` to the javadoc directory.

### 2. Configure better.py
- Modify `href` and `src` of variable `rep` to a proper path so that each html can access `better-javadoc.js` and `better-javadoc.css` when it is uploaded on the server.

### 3. Configure better-javadoc.js
- Change `disqus_shortname` to your own [disqus](http://disqus.com) site name.
- Modify the first function which appends DOM elements at the end of the document body.

### 4. Configure better-javadoc.css
- Modify styles to arrange the appended DOM elements.

### 5. Run better.py
    python better.py javadoc-directory
