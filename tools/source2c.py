#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025 L. E. Segovia <amy@centricular.com>
# SPDX-License-Identifier: BSD-3-Clause

from argparse import ArgumentParser
from pathlib import Path

if __name__ == "__main__":
    parser = ArgumentParser(
        'Convert a source file into a C source file containing the source code as a C string.')
    parser.add_argument('input', type=Path, help='Input source file')
    parser.add_argument('output', type=Path, help='Output C source file')

    args = parser.parse_args()

    input_path, output_path = args.input, args.output

    name = input_path.basename().replace('.', '_')

    with output_path.open('w', encoding='utf-8') as out:
        out.write(f'// Generated from {input_path}\n')
        out.write(f'const char *ff_source_{name} =\n')

        with input_path.open('r', encoding='utf-8') as src:
            for line in src.readlines():
                line = line.rstrip("\n")
                escaped = line.replace('\\', '\\\\').replace('"', '\\"')
                out.write(f'\"{escaped}\\n\"\n')

        out.write(';\n')
