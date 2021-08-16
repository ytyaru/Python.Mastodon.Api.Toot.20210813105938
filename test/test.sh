#!/usr/bin/env bash
set -Ceu
#---------------------------------------------------------------------------
# a
# CreatedAt: 2021-08-16
#---------------------------------------------------------------------------
Run() {
	THIS="$(realpath "${BASH_SOURCE:-0}")"; HERE="$(dirname "$THIS")"; PARENT="$(dirname "$HERE")"; THIS_NAME="$(basename "$THIS")"; APP_ROOT="$PARENT";
	cd "$HERE"
	for file in `find . -name '*.py'`; do
		python3 "$file"
	done
}
Run "$@"
