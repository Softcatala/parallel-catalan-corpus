#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Jordi Mas i Hernandez <jmas@softcatala.org>
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
from lxml import etree
import xml.etree.ElementTree as ET
import tracemalloc
import datetime


class ConvertTmx():

    def __init__(self, input_file, en_filename, ca_filename):
        self.input_file = input_file
        self.en_filename = en_filename
        self.ca_filename = ca_filename

    def convert(self, source_language, target_language):
        parser = etree.XMLParser(recover=True)
        tree = ET.parse(self.input_file, parser=parser)
        root = tree.getroot()
        entries = 0

        tf_en = open(self.en_filename, 'w')
        tf_ca = open(self.ca_filename, 'w')

        for tu_entry in root.iter('tu'):

            entry_id = None
            if 'tuid' in tu_entry.attrib:
                if len(tu_entry.attrib['tuid']):
                    entry_id = 'id: {0}'.format(tu_entry.attrib['tuid'])

            source = ''
            translation = ''
            for tuv_entry in tu_entry:
                if tuv_entry.tag != 'tuv':
                    continue

                if '{http://www.w3.org/XML/1998/namespace}lang' in tuv_entry.attrib:
                    llengua = tuv_entry.attrib['{http://www.w3.org/XML/1998/namespace}lang'].lower()
                else:
                    llengua = tuv_entry.attrib['lang'].lower()

                for seg_entry in tuv_entry.iter('seg'):
                    if llengua == source_language:
                        source = seg_entry.text
                    elif llengua == target_language:
                        translation = seg_entry.text

            if source is None or translation is None:
                continue

            source = source.rstrip().replace("\n", "")
            translation = translation.rstrip().replace("\n", "")

            if len(source) == 0 or len(translation) == 0:
                continue

            tf_en.write(source + "\n")
            tf_ca.write(translation + "\n")

            entries = entries + 1

        tf_en.close()
        tf_ca.close()
        print("Wrote {0} strings".format(entries))

def read_parameters():
    parser = OptionParser()

    parser.add_option(
        '-f',
        '--tmx-file',
        type='string',
        action='store',
        dest='tmx_file',
        help='tmx File to convert to Text'
    )

    parser.add_option(
        '-s',
        '--source_lang',
        type='string',
        action='store',
        default='en',
        dest='source_language',
        help='Source text file'
    )

    parser.add_option(
        '-t',
        '--target_lang',
        type='string',
        action='store',
        dest='target_language',
        help='Target text file'
    )

    parser.add_option(
        '-p',
        '--prefix',
        type='string',
        action='store',
        dest='prefix',
        default='',
        help='Filename prefix'
    )

    (options, args) = parser.parse_args()
    if options.tmx_file is None:
        parser.error('TMX file not given')

    if options.target_language is None:
        parser.error('target_language file not given')

    return options.tmx_file, options.source_language, options.target_language, options.prefix


def main():

    print("Converts TMX into two text files")

    tmx_file, source, target, prefix = read_parameters()

    if len(prefix) > 0:
        prefix = prefix + "."

    txt_en_file = f'{prefix}{source}-{target}.{source}'
    txt_ca_file = f'{prefix}{source}-{target}.{target}'

    tracemalloc.start()

    start_time = datetime.datetime.now()

    convert = ConvertTmx(tmx_file, txt_en_file, txt_ca_file)
    convert.convert(source, target)


    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()
    s = 'Execution time: {0}'.format(datetime.datetime.now() - start_time)
    print(s)

if __name__ == "__main__":
    main()
