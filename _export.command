#!/bin/bash
filepath=$(cd "$(dirname "$0")"; pwd)
cd "$filepath"

python3 export_balatro/exportSave.py