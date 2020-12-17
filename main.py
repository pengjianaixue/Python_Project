import argparse
import os
import xlrd
import xlrd.sheet as sheet
import xlrd.book as book


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    # parser.add_argument("-x", "--verbosity", type=int, choices=[0, 1, 2],
    #                     help="increase output verbosity")
    parser.add_argument("-l", "--lmc_locate", type=str, help="the lmc file (.xlf or .sxlf) path")
    args = parser.parse_args()
    if args.verbose:
        print("verbosity turned on")
    if args.lmc_locate:
        print(args.lmc_locate)
        print(os.system("dir"))
    # book = xlrd.open_workbook("myfile.xls")