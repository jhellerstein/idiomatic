import argparse
from os import system
from os import close
from sys import stdout
from bloom_core import fullparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser("Generate Fluent C++ code from Bloom DSL spec.")
  parser.add_argument('spec',
                    help='path to the Bloom DSL spec file')
  parser.add_argument('-o', '--out',
                    help='output C++ file')


  args = parser.parse_args()

  if (args.out == None):
    codeFd = stdout
  else:
    codeFd = open(args.out, "w")

  result = fullparse(args.spec)
  codeFd.write(result)
  codeFd.close()