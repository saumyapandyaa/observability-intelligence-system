"""
Visualization module for log anomaly detection project.
Contains reusable plotting functions for EDA and results.
"""

import matplotlib.pyplot as plt

def plot_log_level_distribution(df):
    df['Level'].value_counts().plot(kind='bar')
    plt.title("Log Level Distribution")
    plt.xlabel("Level")
    plt.ylabel("Count")
    plt.show()


def plot_top_components(df):
    df['Component'].value_counts().head(10).plot(kind='bar')
    plt.title("Top Components")
    plt.show()


def plot_message_length(df):
    if 'msg_length' not in df.columns:
        df['msg_length'] = df['Content'].apply(len)

    df['msg_length'].hist(bins=30)
    plt.title("Message Length Distribution")
    plt.show()


def plot_logs_per_hour(df):
    if 'Hour' not in df.columns:
        df['Time'] = df['Time'].astype(str).str.zfill(6)
        df['Hour'] = df['Time'].str[:2].astype(int)

    df['Hour'].value_counts().sort_index().plot(kind='bar')
    plt.title("Logs per Hour")
    plt.show()


def plot_eventid_distribution(df):
    df['EventId'].value_counts().head(10).plot(kind='bar')
    plt.title("Top Event IDs")
    plt.show()


def plot_anomaly_groups(anomaly_df):
    anomaly_df['EventId'].value_counts().head(10).plot(kind='bar')
    plt.title("Top Anomaly Groups")
    plt.show()