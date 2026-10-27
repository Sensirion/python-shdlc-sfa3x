# Python Driver for Sensirion SFA3x Formaldehyde Sensor Modules

This package contains the Python SHDLC driver for SFA3x sensor module.


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-shdlc-sfa3x) for an API description and a
[quickstart](https://sensirion.github.io/python-shdlc-sfa3x/execute-measurements.html) example.
https://sensirion.github.io/python-shdlc-sfa3x/.


## Contributing

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `main` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :-)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

## License

See [LICENSE](LICENSE).
