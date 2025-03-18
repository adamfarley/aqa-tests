# Arctic Guide

Foreword: This is the public guide to running the Arctic project.
Please **do not** add any information specific to TCK testing.
TCK-specific Arctic information is documented [here](https://github.com/temurin-compliance/temurin-compliance/blob/arctic_docs/doc/ArcticTCKGotchas.md).

## Contents

- [1. QuickStart Guide](#Quickstart-Guide)
- [2. Tips](#Tips)
- [3. Gotchas](#Gotchas)

## QuickStart Guide
### Section Contents
- [Setup](#Setup)
- [To record](#To-Record)
- [To play](#To-Play)

### Setup:
1. Clone https://github.com/corretto/arctic

2. Download JDK17

3. Add JDK17's java bin directory to the start of your path.

4.
```
gradlew assemble
```

5.
```
java -jar /path_to_clone_dir/build/jars/Arctic.jar -r
```

6.
```
echo "# Defines where the test suite we record will be stored." >> ./recorder.properties
echo "arctic.common.testPath = /customise_this_to_point_to_working_directory/arctic_tests" >> ./recorder.properties
```

7.
```
java -jar /path_to_clone_dir/build/jars/Arctic.jar -p
```

8. Open player.properties and change "arctic.common.repository.json.path" value to:
/customise_this_to_point_to_working_directory/arctic_tests

<a name="torecord"></a>
**To Record (incomplete)**
```
java -jar /path_to_clone_dir/build/jars/Arctic.jar -r
test run
test group start testgroupnamegoeshere
test start testclassnamegoeshere testcasenamegoes here

```
Note test class and case names can be set to anything.

Now Cover the working area with the workbench and the excluded area with the 

<a name="toplay"></a>
**To Play (also incomplete)**
```
java -jar /path_to_clone_dir/build/jars/Arctic.jar -r
test run
test start testclassname testcasename
```

## Tips

### Section Contents
- [General Tips](#General-Tips)
- [Windows](#Windows-Tips)
- [Mac](#Mac-Tips)

### General Tips
- Use JDK17 to set up and run Arctic. JDK21 does not work.

### Windows


### Mac


## Public Gotchas

### Section Contents
- [General Gotchas](#Genberal-Gotchas)
- [Windows Gotchas](#Windows-Gotchas)
- [Mac Gotchas](#Mac-Gotchas)

### General Gotchas
- Use of JDK21 results in errors. Use JDK17 instead.

### Windows


### Mac

