import requests
from datetime import datetime

# GitHub personal access token (set this to avoid rate limiting)
GITHUB_TOKEN = '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'

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# List of repository URLs
repos = [
    "https://github.com/ministryofjustice/staff-device-dns-dhcp-infrastructure",
    "https://github.com/ministryofjustice/staff-device-dns-dhcp-admin",
    "https://github.com/ministryofjustice/staff-device-dhcp-server",
    "https://github.com/ministryofjustice/staff-device-dns-server",
    "https://github.com/ministryofjustice/staff-device-private-dns-zone",
    "https://github.com/ministryofjustice/staff-device-dns-dhcp-disaster-recovery",
    "https://github.com/ministryofjustice/staff-device-logging-dns-dhcp-integration-tests",
    "https://github.com/ministryofjustice/network-access-control-admin",
    "https://github.com/ministryofjustice/network-access-control-disaster-recovery",
    "https://github.com/ministryofjustice/network-access-control-infrastructure",
    "https://github.com/ministryofjustice/network-access-control-integration-tests",
    "https://github.com/ministryofjustice/network-access-control-server",
    "https://github.com/ministryofjustice/staff-infrastructure-monitoring-app-reachability",
    "https://github.com/ministryofjustice/staff-infrastructure-monitoring-blackbox-exporter",
    "https://github.com/ministryofjustice/staff-infrastructure-monitoring-snmpexporter",
    "https://github.com/ministryofjustice/staff-infrastructure-certificate-services",
    "https://github.com/ministryofjustice/staff-infrastructure-network-services",
    "https://github.com/ministryofjustice/staff-infrastructure-smtp-relay-server"
]

# Set your custom date range (ISO format: YYYY-MM-DD)
from_date = "2024-05-01"
to_date = "2024-05-08"

def get_default_branch(repo_url):
    owner_repo = repo_url.replace("https://github.com/", "")
    api_url = f"https://api.github.com/repos/{owner_repo}"
    response = requests.get(api_url, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("default_branch", "main")  # fallback to 'main'
    else:
        return None

def get_commit_count_in_date_range(repo_url, since, until):
    owner_repo = repo_url.replace("https://github.com/", "")
    default_branch = get_default_branch(repo_url)

    if not default_branch:
        return "Error: Couldn't get default branch"

    api_url = f"https://api.github.com/repos/{owner_repo}/commits"
    params = {
        "sha": default_branch,
        "since": since,
        "until": until,
        "per_page": 100
    }

    count = 0
    page = 1
    while True:
        params['page'] = page
        response = requests.get(api_url, headers=HEADERS, params=params)

        if response.status_code != 200:
            return f"Error: {response.status_code}"

        commits = response.json()
        count += len(commits)

        if len(commits) < 100:
            break
        page += 1

    return count

if __name__ == "__main__":
    print(f"📅 Counting commits from {from_date} to {to_date}...\n")
    for repo in repos:
        count = get_commit_count_in_date_range(repo, from_date + "T00:00:00Z", to_date + "T23:59:59Z")
        print(f"{repo} → {count} commits")
