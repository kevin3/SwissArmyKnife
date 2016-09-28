#!/usr/bin/python3
import pandas as pd
import argparse


def main():
    parser = argparse.ArgumentParser(description='convert xlsx to csv')
    parser.add_argument('-f', action='store', dest='XLS', help="input", required=True)
    parser.add_argument('-o', action='store', dest="CSV", help="output", required=True)

    args = parser.parse_args()
    all_data=pd.DataFrame()
    xl=pd.ExcelFile(args.XLS)
    df=xl.parse('Sheet1') ##single sheet
    print sheet,df.describe()
    all_data=all_data.append(df)
    all_data.to_csv(args.CSV, index=False)

if __name__ == "__main__":
    main()
