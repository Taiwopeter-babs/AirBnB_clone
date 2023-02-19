#!/usr/bin/env bash
# Automates basic git actions

# Second argument on command line
arg1="$1"
# Third argument on command line
arg2="$2"

git add "$arg1"

git commit -m "$arg2"


git push
