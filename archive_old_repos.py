#!/usr/bin/env python3

"""
🚀 Archive Old Repositories Script
ไฟล์นี้จะ archive repositories เก่าที่ไม่มีการเคลื่อนไหว (ตั้งแต่ 2 เดือนขึ้นไป)

ใช้งาน:
    python3 archive_old_repos.py
    
หรือ:
    chmod +x archive_old_repos.py
    ./archive_old_repos.py

ข้อมูลที่ต้องการ:
    - GitHub Token (Personal Access Token)
    - หรือ gh CLI authenticated
"""

import subprocess
import sys
from typing import List, Tuple

def check_gh_cli():
    """✅ ตรวจสอบ GitHub CLI"""
    try:
        subprocess.run(['gh', '--version'], capture_output=True, check=True)
        print("✅ GitHub CLI found")
        return True
    except FileNotFoundError:
        print("❌ GitHub CLI not installed!")
        print("📥 Install from: https://cli.github.com/")
        return False

def check_auth():
    """✅ ตรวจสอบการ authenticate"""
    try:
        subprocess.run(['gh', 'auth', 'status'], capture_output=True, check=True)
        print("✅ Authenticated with GitHub")
        return True
    except subprocess.CalledProcessError:
        print("❌ Not authenticated!")
        print("🔐 Run: gh auth login")
        return False

def archive_repo(username: str, repo_name: str) -> bool:
    """🔒 Archive a single repository"""
    full_repo = f"{username}/{repo_name}"
    try:
        # Check if already archived
        result = subprocess.run(
            ['gh', 'repo', 'view', full_repo, '--json', 'isArchived', '-q', '.isArchived'],
            capture_output=True,
            text=True,
            check=True
        )
        
        if result.stdout.strip() == "true":
            print(f"  ⏭️  Already archived - SKIPPED")
            return None
        
        # Archive the repo
        subprocess.run(
            ['gh', 'repo', 'archive', full_repo, '--confirm'],
            capture_output=True,
            check=True
        )
        print(f"  ✅ ARCHIVED")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"  ❌ FAILED: {e}")
        return False
    except Exception as e:
        print(f"  ⚠️  ERROR: {e}")
        return None

def main():
    print("=" * 50)
    print("📦 Archive Old Repositories Script")
    print("=" * 50)
    print()
    
    # Check requirements
    if not check_gh_cli():
        sys.exit(1)
    
    if not check_auth():
        sys.exit(1)
    
    print()
    
    username = "LifeStly"
    
    # 📋 List of old repositories (2+ months old)
    old_repos = [
        "ColorMyViews",
        "Aboutme2",
        "AndroidTrivia-Starter",
        "AndroidTrivia-Starter2",
        "3.3.AndroidTrivia-Starter-mastermmmstep4",
        "AndroidTrivia",
        "DessertClicker-Starter",
        "FirstApp",
        "GuessTheWord-Starter",
        "GuessTheWord-Starter.2",
        "GuessTheWord-Starter.3",
        "GuessTheWord-Starter.4",
        "TrackMySleepQuality-Starter",
        "Update2",
        "FirstUpdateee",
        "FirstApp_newTest",
        "MyApplication2",
        "NewFirst",
        "NewFirstttttttt",
        "NewFirstapp",
        "newFirstappp",
        "NewFirstAppHomeee",
        "RecyclerViewFundamentals-Starter",
        "MarsRealEstate-Starter",
        "Addgit-8",
        "8Apigit",
        "Project",
        "ProjectVideo",
        "ProjectVideoV2",
        "line-chatbot-one",
    ]
    
    print(f"📋 REPOSITORIES TO ARCHIVE: {len(old_repos)}")
    print()
    print("=" * 50)
    
    stats = {
        'archived': 0,
        'skipped': 0,
        'failed': 0
    }
    
    # Process each repository
    for repo in old_repos:
        print(f"⏳ {username}/{repo}")
        
        result = archive_repo(username, repo)
        
        if result is True:
            stats['archived'] += 1
        elif result is False:
            stats['failed'] += 1
        else:  # None (skipped)
            stats['skipped'] += 1
        
        print()
    
    # Summary
    print("=" * 50)
    print("📊 SUMMARY:")
    print(f"  ✅ Archived:  {stats['archived']}")
    print(f"  ⏭️  Skipped:  {stats['skipped']}")
    print(f"  ❌ Failed:   {stats['failed']}")
    print()
    
    print("🎉 Process Complete!")
    print()
    print("💡 NEXT STEPS:")
    print("  1. ✅ Check your GitHub profile - old repos are now hidden")
    print("  2. 📦 They're still accessible if you know the link (read-only)")
    print("  3. 🔓 To unarchive: gh repo unarchive LifeStly/RepoName --confirm")
    print()
    print("📌 NOTE:")
    print("  • Archived repos won't show in your profile")
    print("  • Code is still safe and accessible")
    print("  • Perfect for keeping old learning projects hidden!")
    print()

if __name__ == "__main__":
    main()
