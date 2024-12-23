#!/bin/bash
filepath=$(cd "$(dirname "$0")"; pwd)
cd "$filepath"

python3 import_balatro/importSave.py