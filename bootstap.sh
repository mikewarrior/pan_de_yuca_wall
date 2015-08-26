#!/bin/bash

if [ ! -d "tmp" ]; then
  mkdir tmp
fi
echo dev > tmp/YUCA_ENV
