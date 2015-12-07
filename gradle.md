# GRADLE
Gradle is an open source build automation system that builds upon the concepts of Apache Ant and Apache Maven and introduces a Groovy-based domain-specific language (DSL) instead of the XML form used by Apache Maven of declaring the project configuration. Gradle uses a directed acyclic graph ("DAG") to determine the order in which tasks can be run.

## Install
* Download one of the Gradle distributions from the [Gradle web site](http://www.gradle.org/downloads)
* On MacOS, use `brew`
```
    brew install gradle
```

## Create project
* Run `gradle init` to initialize a project of a particular type
```
    gradle init --type <project-type>
    > Available values for project-type are:
    >     basic
    >     groovy-library
    >     java-library
    >     pom
    >     scala-library
```

* Next you should create a task called `wrapper` and choose your the gradle version.
```
    task wrapper(type: Wrapper) {
        gradleVersion = '2.3'
    }
```

* Then you can run gradle wrapper to setup approriate gradle binary
```
    gradle wrapper
    ./gradlew build
```

* Note that you can also run gradle wrapper without creating `wrapper` tasks in the `build.gradle` file
```
    gradle wrapper --gradle-version 2.4
```

* After that you should use `./gradlew` instead of the system gradle
```
    ./gradlew run
```

## Run tasks
* To see which tasks are available for a project
```
    gradle tasks
    > Build Setup tasks
    > -----------------
    > init - Initializes a new Gradle build. [incubating]
    > wrapper - Generates Gradle wrapper files. [incubating]

    > Help tasks
    > ----------
    > components - Displays the components produced by root project 'gradle-test'. [incubating]
    > dependencies - Displays all dependencies declared in root project 'gradle-test'.
    > dependencyInsight - Displays the insight into a specific dependency in root project 'gradle-test'.
    > help - Displays a help message.
    > model - Displays the configuration model of root project 'gradle-test'. [incubating]
    > projects - Displays the sub-projects of root project 'gradle-test'.
    > properties - Displays the properties of root project 'gradle-test'.
    > tasks - Displays the tasks runnable from root project 'gradle-test'.

    > Other tasks
    > -----------
    > ... other project specific tasks
```

* Run a task
```
    # -q for running it quietly
    gradle -q <task>
```




# REFERENCES
* [Gradle User Guide](https://docs.gradle.org/current/userguide/userguide.html)
* [Build your project with Gradle Wrapper](https://spring.io/guides/gs/gradle/#_build_your_project_with_gradle_wrapper)
* [Gradle in Action](https://www.manning.com/books/gradle-in-action)
