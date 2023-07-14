from config import config
import csv
import pandas as pd
import ssl
import sys
from analyzer.snapshot_analyzer import SnapshotAnalyzer
from analyzer.target_url_list_analyzer import TargetUrlListAnalyzer
from unique_website_list.unique_website_list import generate_unique_website_list
from idea.idea_report_generator import IdeaReportGenerator

def save_to_csv(file, data):
    with open(file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['question', 'answer'])
        writer.writeheader()
        for key, value in data.items():
            writer.writerow({'question': key, 'answer': value})

def analyze_all_snapshot():
    df = pd.read_csv(config['all_snapshot_url'])
    snapshot_analyzer = SnapshotAnalyzer(df)
    analysis = snapshot_analyzer.analyze()
    save_to_csv(config['all_snapshot_report_location'], analysis)

def analyze_primary_snapshot():
    df = pd.read_csv(config['primary_snapshot_url'])
    snapshot_analyzer = SnapshotAnalyzer(df)
    analysis = snapshot_analyzer.analyze()
    save_to_csv(config['primary_snapshot_report_location'], analysis)

def analyze_unique_url():
    df = pd.read_csv(config['unique_final_urls_location'])
    snapshot_analyzer = SnapshotAnalyzer(df)
    analysis = snapshot_analyzer.analyze()
    save_to_csv(config['unique_url_report_location'], analysis)

def analyze_unique_website():
    df = pd.read_csv(config['unique_final_websites_location'])
    snapshot_analyzer = SnapshotAnalyzer(df)
    analysis = snapshot_analyzer.analyze()
    save_to_csv(config['unique_website_report_location'], analysis)

def generate_target_url_list_analysis():
    df = pd.read_csv(config['target_url_list_url'])
    target_url_list_analyzer = TargetUrlListAnalyzer(df)
    analysis = target_url_list_analyzer.analyze()
    save_to_csv(config['target_url_list_report_location'], analysis)

def generate_idea_report():
    df = pd.read_csv(config['unique_final_websites_location'])
    idea_report_generator = IdeaReportGenerator(df)
    report = idea_report_generator.report()
    report.to_csv(config['idea_report_location'], index=False)

def generate_idea_bureau_report():
    df = pd.read_csv(config['unique_final_websites_location'])
    idea_report_generator = IdeaReportGenerator(df)
    report = idea_report_generator.report_bureaus()
    report.to_csv(config['idea_bureau_report_location'], index=False)

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context

    command = sys.argv[1]

    if command == 'analyze-snapshot-all':
        analyze_all_snapshot()
    if command == 'analyze-snapshot-primary':
        analyze_primary_snapshot()
    if command == 'analyze-unique-urls':
        analyze_unique_url()
    if command == 'analyze-unique-websites':
        analyze_unique_website()
    if command == 'analyze-target-url-list':
        generate_target_url_list_analysis()
    if command == 'generate-unique-website-list':
        generate_unique_website_list()
    if command == 'generate-idea-report':
        generate_idea_report()
    if command == 'generate-idea-bureau-report':
        generate_idea_bureau_report()