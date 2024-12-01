#!/bin/bash
autopep8 --in-place --aggressive -r .
buildifier -r .