#!/usr/bin/env python3

from __future__ import print_function

import argparse

import pandas as pd
# from pd import DataFrame
# from pd import read_excel


def get_args():
    parser = argparse.ArgumentParser(
        description='Get order totals for each track')
    parser.add_argument('spreadsheet_filename',
                        type=str,
                        action='store',
                        help='The xlsx workbook to parse orders from',
                        default=None)

    return parser.parse_args()


def main():
    args = get_args()

    spreadsheet_filename = args.spreadsheet_filename

    # Load the spreadsheet directly into pandas
    fr = pd.read_excel(io=spreadsheet_filename, sheet_name="Items")

    # Print the income by ticket type, and total tickets purchased of each type
    tickets = fr.groupby(["Ticket Type"])["Total"].agg(['sum', 'count'])
    print(tickets)


if __name__ == "__main__":
    main()