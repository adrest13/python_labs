import argparse
from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import json_to_csv, csv_to_json


def main():
    """
    The function converts files between JSON, CSV and XLSX formats.

    json2csv:
        --in: path to the input JSON file
        --out: path to the output CSV file

    csv2json:
        --in: path to the input CSV file
        --out: path to the output JSON file

    csv2xlsx:
        --in: path to the input CSV file
        --out: path to the output XLSX file
    """
    parser = argparse.ArgumentParser(description="File format converters")
    commands = parser.add_subparsers(dest="command", required=True)

    json_parser = commands.add_parser("json2csv", help="Convert JSON to CSV")
    json_parser.add_argument("--in", dest="input", required=True, help="Input JSON file")
    json_parser.add_argument("--out", dest="output", required=True, help="Output CSV file")

    csv_parser = commands.add_parser("csv2json", help="Convert CSV to JSON")
    csv_parser.add_argument("--in", dest="input", required=True, help="Input CSV file")
    csv_parser.add_argument("--out", dest="output", required=True, help="Output JSON file")

    excel_parser = commands.add_parser("csv2xlsx", help="Convert CSV to XLSX")
    excel_parser.add_argument("--in", dest="input", required=True, help="Input CSV file")
    excel_parser.add_argument("--out", dest="output", required=True, help="Output XLSX file")

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)


if __name__ == "__main__":
    main()
