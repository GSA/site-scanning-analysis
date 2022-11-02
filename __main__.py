from config import config
import csv
import pandas as pd
import ssl
import sys
from analyzer.snapshot_analyzer import SnapshotAnalyzer
from analyzer.target_url_list_analyzer import TargetUrlListAnalyzer


def save_to_csv(file, data):
    with open(file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['question', 'answer'])
        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'question': key, 'answer': value})

def generate_all_snapshot_analysis():
    df = pd.read_json(config['all_snapshot_url'])
    snapshot_analyzer = SnapshotAnalyzer(df)
    analysis = snapshot_analyzer.analyze()
    save_to_csv(config['all_snapshot_report_location'], analysis)

def generate_primary_snapshot_analysis():
    df = pd.read_json(config['primary_snapshot_url'])
    snapshot_analyzer = SnapshotAnalyzer(df)
    analysis = snapshot_analyzer.analyze()
    save_to_csv(config['primary_snapshot_report_location'], analysis)

def generate_target_url_list_analysis():
    df = pd.read_csv(config['target_url_list_url'])
    target_url_list_analyzer = TargetUrlListAnalyzer(df)
    analysis = target_url_list_analyzer.analyze()
    save_to_csv(config['target_url_list_report_location'], analysis)

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context

    command = sys.argv[1]

    if command == 'snapshot-all':
        generate_all_snapshot_analysis()
    if command == 'snapshot-primary':
        generate_primary_snapshot_analysis()
    if command == 'target-url-list':
        generate_target_url_list_analysis()
