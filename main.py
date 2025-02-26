from config import config
import csv
import pandas as pd
import ssl
import sys
from report_generators.snapshot import Snapshot
from report_generators.target_url_list import TargetUrlList
from report_generators.idea import Idea
from report_generators.standards import Standards
from report_generators.baseline import Baseline
from unique_website_list.unique_website_list import generate_unique_website_list


def save_to_csv(file, data):
    with open(file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['question', 'answer'])
        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'question': key, 'answer': value})

def generate_all_snapshot_report():
    df = pd.read_csv(config['all_snapshot_url'])
    snapshot_analyzer = Snapshot(df)
    analysis = snapshot_analyzer.generate_report()
    save_to_csv(config['all_snapshot_report_location'], analysis)

def generate_primary_snapshot_report():
    df = pd.read_csv(config['primary_snapshot_url'])
    snapshot_analyzer = Snapshot(df)
    analysis = snapshot_analyzer.generate_report()
    save_to_csv(config['primary_snapshot_report_location'], analysis)

def generate_unique_url_report():
    df = pd.read_csv(config['unique_final_urls_location'])
    snapshot_analyzer = Snapshot(df)
    analysis = snapshot_analyzer.generate_report()
    save_to_csv(config['unique_url_report_location'], analysis)

def generate_unique_websites_report():
    df = pd.read_csv(config['unique_final_websites_location'])
    snapshot_analyzer = Snapshot(df)
    analysis = snapshot_analyzer.generate_report()
    save_to_csv(config['unique_website_report_location'], analysis)

def generate_target_url_list_report():
    df = pd.read_csv(config['target_url_list_url'])
    target_url_list_analyzer = TargetUrlList(df)
    analysis = target_url_list_analyzer.generate_report()
    save_to_csv(config['target_url_list_report_location'], analysis)

def generate_idea_report():
    df = pd.read_csv(config['unique_final_websites_location'])
    idea_report_generator = Idea(df)
    report = idea_report_generator.generate_report()
    report.to_csv(config['idea_report_location'], index=False)

def generate_idea_bureau_report():
    df = pd.read_csv(config['unique_final_websites_location'])
    idea_report_generator = Idea(df)
    report = idea_report_generator.generate_bureaus_report()
    report.to_csv(config['idea_bureau_report_location'], index=False)

def generate_standards_report():
    df = pd.read_csv(config['unique_final_websites_location'])
    standards_report_generator = Standards(df)
    report = standards_report_generator.generate_report()
    report.to_csv(config['standards_report_location'], index=False)

def generate_standards_bureau_report():
    df = pd.read_csv(config['unique_final_websites_location'])
    standards_report_generator = Standards(df)
    report = standards_report_generator.generate_bureaus_report()
    report.to_csv(config['standards_bureau_report_location'], index=False)

def generate_baseline_report():
    df = pd.read_csv(config['unique_snapshot_url'])
    baseline_report_generator = Baseline(df)
    report = baseline_report_generator.generate_report()
    report.to_csv(config['baseline_report_location'], index=False)

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context

    command = sys.argv[1]

    if command == 'generate-all-snapshot-report':
        generate_all_snapshot_report()
    if command == 'generate-primary-snapshot-report':
        generate_primary_snapshot_report()
    if command == 'generate-unique-url-report':
        generate_unique_url_report()
    if command == 'generate-unique-websites-report':
        generate_unique_websites_report()
    if command == 'generate-target-url-report':
        generate_target_url_list_report()
    if command == 'generate-unique-website-list':
        generate_unique_website_list()
    if command == 'generate-idea-report':
        generate_idea_report()
    if command == 'generate-idea-bureau-report':
        generate_idea_bureau_report()
    if command == 'generate-standards-report':
        generate_standards_report()
    if command == 'generate-standards-bureau-report':
        generate_standards_bureau_report()
    if command == 'generate-baseline-report':
        generate_baseline_report()