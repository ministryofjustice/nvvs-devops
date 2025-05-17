import os
import requests
from datetime import datetime

# Get the GitHub token from the environment
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# Set headers for the requests
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}"
}

# List of repository URLs
repos = [
    "https://github.com/ministryofjustice/staff-device-dns-dhcp-infrastructure",
    "https://github.com/ministryofjustice/staff-device-dns-dhcp-admin",
    "https://github.com/ministryofjustice/staff-device-dhcp-server",
    "https://github.com/ministryofjustice/staff-device-dns-server",
    "https://github.com/ministryofjustice/deployment-tgw",
    "https://github.com/ministryofjustice/diso-devops-ami-builder",
    "https://github.com/ministryofjustice/diso-devops-module-ssm-bastion",
    "https://github.com/ministryofjustice/juniper-mist-integration",
    "https://github.com/ministryofjustice/linuxify",
    "https://github.com/ministryofjustice/mojo-aws-github-oidc-provider",
    "https://github.com/ministryofjustice/network-access-control-admin",
    "https://github.com/ministryofjustice/network-access-control-disaster-recovery",
    "https://github.com/ministryofjustice/network-access-control-infrastructure",
    "https://github.com/ministryofjustice/network-access-control-integration-tests",
    "https://github.com/ministryofjustice/network-access-control-server",
    "https://github.com/ministryofjustice/nvvs-containers",
    "https://github.com/ministryofjustice/nvvs-devops",
    "https://github.com/ministryofjustice/nvvs-devops-github-actions",
    "https://github.com/ministryofjustice/nvvs-devops-monitor",
    "https://github.com/ministryofjustice/staff-device-dns-dhcp-disaster-recovery",
    "https://github.com/ministryofjustice/staff-device-logging-dns-dhcp-integration-tests",
    "https://github.com/ministryofjustice/staff-device-logging-infrastructure",
    "https://github.com/ministryofjustice/staff-device-private-dns-zone",
    "https://github.com/ministryofjustice/staff-device-shared-services-infrastructure",
    "https://github.com/ministryofjustice/staff-infrastructure-certificate-services",
    "https://github.com/ministryofjustice/staff-infrastructure-monitoring-app-reachability",
    "https://github.com/ministryofjustice/staff-infrastructure-monitoring-blackbox-exporter",
    "https://github.com/ministryofjustice/staff-infrastructure-monitoring-snmpexporter",
    "https://github.com/ministryofjustice/staff-infrastructure-network-services",
    "https://github.com/ministryofjustice/staff-infrastructure-smtp-relay-server",
    "https://github.com/ministryofjustice/staff-technology-services-github-teams"
]

# Set your custom date range (ISO format: YYYY-MM-DD)
from_date = "2024-05-10"
to_date = "2024-05-17"

def get_default_branch(repo_url):
    owner_repo = repo_url.replace("https://github.com/", "")
    api_url = f"https://api.github.com/repos/{owner_repo}"
    response = requests.get(api_url, headers=HEADERS)

    # Debugging log to check what is returned
    if response.status_code == 200:
        repo_data = response.json()
        print(f"Repository data for {repo_url}: {repo_data}")  # Debugging line
        return repo_data.get("default_branch", "main")  # fallback to 'main'
    else:
        print(f"Failed to get repo data for {repo_url}: {response.status_code}, {response.text}")
        return None

def get_commit_count_in_date_range(repo_url, since, until):
    owner_repo = repo_url.replace("https://github.com/", "")
    default_branch = get_default_branch(repo_url)

    if not default_branch:
        return f"Error: Couldn't get default branch for {repo_url}"

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
            return f"Error: {response.status_code} for {repo_url}"

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
