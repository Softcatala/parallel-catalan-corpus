#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018-2020 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

from optparse import OptionParser

def _is_invalid(src, trg):
    if len(src) < 2 or len(trg) < 2:
        return True

    return False

def load_data_set(f_src, f_trg):
    strings = {}

    with open(f_src, "r") as source, open(f_trg, "r") as target:
        while True:
            src = source.readline()
            trg = target.readline()

            if not (src and trg):
                break

            if _is_invalid(src, trg):
                continue

            strings[src] = trg

    print(f"Loaded {len(strings)} from {f_src} and {f_trg}")
    return strings

def split_in_two_files(file_one, file_two, file_third, file_fourth):

    pairs = 0
    cnt = 0

    #source 1: eng-deu
    #source 2: eng-cat
    source_one = load_data_set(file_one, file_two)
    source_two = load_data_set(file_third, file_fourth)

    with open("src.txt", "w") as source,\
        open("tgt.txt", "w") as target:

        for src_one in source_one.keys():

            if src_one not in source_two.keys():
                continue

            tgt = source_two[src_one]
            src = source_one[src_one]
            pairs = pairs + 1

            source.write(src)
            target.write(tgt)
            cnt = cnt + 1

    print("Pairs: " + str(pairs))

def read_parameters():
    parser = OptionParser()

    parser.add_option(
        '-1',
        '--fileset-one-source',
        type='string',
        action='store',
        dest='fileset_one_source',
        help=''
    )

    parser.add_option(
        '-2',
        '--fileset-one-target',
        type='string',
        action='store',
        dest='fileset_one_target',
        help=''
    )
    parser.add_option(
        '-3',
        '--fileset-two-source',
        type='string',
        action='store',
        dest='fileset_two_source',
        help=''
    )

    parser.add_option(
        '-4',
        '--fileset-two-target',
        type='string',
        action='store',
        dest='fileset_two_target',
        help=''
    )

    (options, args) = parser.parse_args()
    return options.fileset_one_source, options.fileset_one_target, options.fileset_two_source, options.fileset_two_target


def main():

    print("Takes to pair of datasets (e.g. en-ca and en-es), pivots over en, and produces es-ca with")
    print("the matching strings")

    fileset_one_source, fileset_one_target, fileset_two_source, fileset_two_target = read_parameters()
    split_in_two_files(fileset_one_source, fileset_one_target, fileset_two_source, fileset_two_target)


if __name__ == "__main__":
    main()
