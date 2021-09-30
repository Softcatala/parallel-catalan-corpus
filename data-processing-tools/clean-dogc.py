#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Jordi Mas i Hernandez <jmas@softcatala.org>
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

def _clean(text):
    text = text.replace(" ,", ",")
    text = text.replace(" ;", ";")
    text = text.replace(" ' ", "'")
    text = text.replace(" · ", "·")
    text = text.replace(" .", ".")
    text = text.replace(" :", ":")
    text = text.replace(" )", ")")
    text = text.replace(" ’ ", "’")
    text = text.replace(" ’ ", "’")
    text = text.replace(" ?", "?")
    text = text.replace("¿ ", "¿")
    text = text.replace(" !", "!")
    text = text.replace("¡ ", "¡")


    return text
    
def main():

    print("Fixes spaces in DOGC corpus")

    with open("raw/dogc-es-ca.es", 'r') as tf_source, open("raw/dogc-es-ca.ca", 'r') as tf_target, \
         open("dogc-es-ca.es", 'w') as tf_clean_source, open("dogc-es-ca.ca", 'w') as tf_clean_target:

        strings = 0
        while True:
            src = tf_source.readline()
            trg = tf_target.readline()

            if not (src and trg):
                break

            src = _clean(src)
            trg = _clean(trg)

            tf_clean_source.write("{0}".format(src))
            tf_clean_target.write("{0}".format(trg))
            strings = strings + 1

        print(f"Pairs: {strings}")

if __name__ == "__main__":
    main()
