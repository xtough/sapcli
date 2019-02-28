# ABAP Unit

## Usage

Execute `sapcli` with the parameters `aunit run {package|class|program} $OBJECT_NAME`.

The exit code will be determined based on test results where exit code is the
number of failed and erroed tests.

## Output format

### Raw

Tests results are printed in the form as they were returned from ADT.

### Human

This format attempts to provide nice human readable form of the test results.

```
GLOBAL PUBLIC CLASS FOO
  LOCAL TEST CLASS A
    TEST METHOD1 [SUCCESS]
  LOCAL TEST CLASS B
    TEST METHOD1 [ERROR]
GLOBAL PUBLIC CLASS FOO
  LOCAL TEST CLASS A
    TEST METHOD1 [SKIPPED]
  LOCAL TEST CLASS B
    TEST METHOD1 [SUCCESS]

--------
GLOBAL PUBLIC CLASS FOO=>LOCAL TEST CLASS A=>TEST METHOD1
[critical] [failedAssertion] Assertion failed
--------

Succeeded: 2
Skipped:   1
Failed:    1
```

### JUnit

The JUnit format was assembed from:
- https://github.com/windyroad/JUnit-Schema/blob/master/JUnit.xsd
- https://github.com/junit-team/junit5/blob/master/platform-tests/src/test/resources/jenkins-junit.xsd
- http://svn.apache.org/repos/asf/ant/core/trunk/src/main/org/apache/tools/ant/taskdefs/optional/junit/

* testsuites
  - name :
  - tests :
  - failures :
  - disabled :
  - errors :
  - time :

* testsuite
  - name :
  - tests :
  - failures :
  - disabled :
  - errors :
  - time :
  - skipped :
  - hostname :
  - package :
  - id :

* properties
  - name:
  - value:

* testcase
  - error:
    - message:
    - type:
  - failure:
    - message:
    - type:
  - skipped:
  - system-err : stack
