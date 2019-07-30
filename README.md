# ceda-unittest-prometheus-wrapper
Convenience utility for creating a Prometheus target wrapper for 
`unittest.TestCase` tests.  It runs a web service which invokes a given unit 
test case and returns an UP/DOWN status in Prometheus compatible output based
on the aggregate success / failure of the unit tests in the test case.  It
can also be configured to run individual unit tests rather than all the tests
in the case.

## Command line
Get UP/DOWN status based on aggregate result of running all tests in 
`MyTestCase` class
```bash
$ prometheus_unittest_wrapper -c my_unittest_package.my_module.MyTestCase
```

To get output,
```bash
curl http://localhost:5000/metrics/MyTestCase
```

Run two specific tests from a given test case and serve up Prometheus output
on separate endpoints for each:

```bash
$ prometheus_unittest_wrapper -c my_unittest_package.my_module.MyTestCase -n test_1 test_5
```

To get output:

```bash
curl http://localhost:5000/metrics/MyTestCase/test_1
```

```bash
curl http://localhost:5000/metrics/MyTestCase/test_5
```

Run with `-h` for a complete list of command line options.

## API
Create a Flask app for exposing metrics based on output from `MyTestCase`
```python
>>> from ceda.unittest_prometheus_wrapper.flask_app import flask_app_factory
>>> from my_unittest_package.my_module import MyTestCase
>>> app = flask_app_factory(MyTestCase, test_names=['test_1', 'test_5'], service_name='my_test_case')
>>> app.run()
```