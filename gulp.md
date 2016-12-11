# GULP
## what is gulp
[Gulp](http://gulpjs.com/) is a Javascript task runner that is:
* easy to use
* efficient
* high quality
* easy to learn

Gulp helps you automate your workflow, including but not limited to:
* script concatenation
* script minifaction
* Sass/less compilation
* automated testing
* JS/CSS linting
* image manipulation
* sprite generation
* many other

Gulp's advantages over task runners such as Grunt are:
* Very fast. This is due to the fact that it use node streams instead of writing intermediary files to disk
* Gulp plugins are designed to do one thing only, Grunt plugins often perform multiple tasks
* Gulp configuration file uses leaner javascript, which is easier to write and read than JSON configuration file.

## Installation
The installation steps are:
1. Install Gulp globally
2. Install Gulp in devDependencies
3. Create a gulpfile.js

First, install `gulp` globally so we can run `gulp` from the command line
```
    npm install -g gulp
```

Next, declare `gulp` in the development package list in `package.json`
```
  "devDependencies": {
    "gulp": "^3.9.0",
    ...
  }
```

You can also do this by running `npm` with `--save-dev` option
```
    npm install --save-dev gulp
```

Once you install `gulp`, you can now create a file named `gulpfile.js` in the project root directory. Then you can run `gulp` from the command line and it will execute the tasks defined in your `gulpfile.js`.

```
    # Run default task in your gulp file
    gulp
```

## Gulp file
A simplest `gulpfile.js` looks like this

```
var gulp = require('gulp')
gulp.task('default', function() {
});
```

It defines a task `default` that does nothing. More complicated `gulpfile.js` simply follows this linear structure: define a list of tasks in Javascript functions

```
gulp.task('taskA', function() {
    ... // do something for task A
});

gulp.task('taskB', function() {
    ... // do something for task A
});

...// tasks C, D, E and so on
```

Then we run the task like this
```
    # run single task
    gulp <taskA>

    # run several tasks at the same time
    gulp <taskA> <taskB> <taskC>

    # run `default` task
    gulp
```


## Core gulp functions
The gulp API contains only 4 functions
* gulp.task
* gulp.src
* gulp.dest
* gulp.watch

Apart from few built-in functions, gulp provides functionalities to users via a plugin system. Gulp plugins are simply npm packages whose names start with `gulp-` that you can install to the development packages of your project like this

```
    npm install --save-dev gulp-jshint
```

Let's create a task to use our `gulp-jshint` plugin

```
var gulp = require('gulp');
var jshint = require('gulp-jshint');

gulp.task('jshint', function() {
  gulp.src('./src/scripts/*.js')
    .pipe(jshint())
    .pipe(jshint.reporter('default'));
});
```

We run the `jshint` task like this
```
    gulp jshint
```

In this task we use 2 gulp functions
1. [gulp.src](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulpsrcglobs-options) takes a glob and return a stream of filenames matching the glob
2. [gulp.pipe](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulpsrcglobs-options) pipes the result of the last operation to the next, just like Linux pipe. In this case, the file names matching `*.js` in folder `src/scripts` are piped to `jshint`. Then the result is piped again to the jshint's reporter `default`.


Let's create another task `imagemin` to minify images

```
var imagemin = require('gulp-imagemin');

gulp.task('imagemin', function() {
  gulp.src('./src/images/**/*')
    .pipe(imagemin())
    .pipe(gulp.dest('./build/images'));
});
```

This task uses another gulp function called [gulp.dest](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulpdestpath-options). 
* `gulp.dest` pipes the output of the previous action to another directory.
* Write path is calculated by appending the file relative path to the given destination directory.
* Directories that don't exist will be created


Now we can define a `default` task that depends on the two tasks `imagemin` and `jshint` that we just created, and these tasks will run in sequence when we execute `gulp`

```
// default gulp task
gulp.task('default', ['jshint', 'imagemin'], function() {
});
```

The final step is to run appropriate task when there's change in the source folder

```
// default gulp task
gulp.task('default', ['jshint', 'imagemin'], function() {
    // watch for JS changes
    gulp.watch('./src/scripts/*.js', [jshint]);

    // watch for image changes
    gulp.watch('./src/images/**/*', [imagemin]);
});
```

Here [gulp.watch](https://github.com/gulpjs/gulp/blob/master/docs/API.md#gulpwatchglob--opts-tasks-or-gulpwatchglob--opts-cb) will watch files defined by the glob pattern and whenever there's any change it will rerun the corresponding tasks.


## Best Practices
### scaffolding gulp project
Even though setting up a new project and create gulp file from scratch is good for learning purpose, we often do the same thing again and again following some sort of best practices, that it's better to scaffold the project using best practice file from other developers and modify it later if necessary.

One of the most popular scaffolding tools is [Yeoman](http://yeoman.io/) and we will use it to scaffold our gulp project.

Steps:
1. Install `yo` and `bower` globally
2. Install `generator-gulp-webapp` globally
3. Generate gulp webapp project with yo


First install `yo` and `bower` globally like this

```
    npm install -g yo bower
```

Then we can install a generator for gulp webapp called `generator-gulp-webapp`
```
    npm install -g generator-gulp-webapp
```

Then run `yo`. We can go with all the default stuff and see how it goes. Remove the things you don't want.

### Watch files for change & live-reload
* Use `gulp-load-plugins`, `connect`, `connect-livereload`, `gulp-livereload`, `opn`

### Get the size of your project files
* Use `gulp-size`

### Remove extra css
* Use `uncss`

### Image resize
* Use `gulp-image-resize`

### Gzip scripts and styles
* Use `gulp-pako`


## Tips
* To list all available tasks use `gulp --tasks`
* Use `gulp-print` to print filenames to console so that you can see what's going through the pipe



# REFERENCES
* [Gulp introduction](http://tooling.github.io/book-of-modern-frontend-tooling/build-systems/gulp/introduction.html)
* [An Introduction to Gulp.js](http://www.sitepoint.com/introduction-gulp-js/)
* [Introduction to Gulp.js](https://medium.com/@lukyvj/an-introduction-to-gulp-js-295ee489e2c9#.1w8hl6xl1)
* [Introduction to Gulp.js](http://stefanimhoff.de/2014/gulp-tutorial-1-intro-setup/)
* [Gulp cheatsheet](https://github.com/osscafe/gulp-cheatsheet)
* [Awesome gulp](http://alferov.github.io/awesome-gulp/)

