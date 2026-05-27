#!/bin/bash

# 📦 Archive Old Repositories Script
# ไฟล์นี้จะ archive repositories เก่าที่ไม่มีการเคลื่อนไหว
# ใช้: bash archive-old-repos.sh

set -e

echo "🚀 Starting Archive Process..."
echo "📋 This will archive old repositories (keep them read-only)"
echo ""

# ✅ ตรวจสอบ GitHub CLI
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI not installed!"
    echo "📥 Install: https://cli.github.com/"
    exit 1
fi

# ✅ ตรวจสอบ authentication
if ! gh auth status &> /dev/null; then
    echo "❌ Not authenticated with GitHub!"
    echo "🔐 Run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI ready"
echo ""

# 📋 List of OLD repositories to archive (2+ months old)
OLD_REPOS=(
    "ColorMyViews"
    "Aboutme2"
    "AndroidTrivia-Starter"
    "AndroidTrivia-Starter2"
    "3.3.AndroidTrivia-Starter-mastermmmstep4"
    "AndroidTrivia"
    "DessertClicker-Starter"
    "FirstApp"
    "GuessTheWord-Starter"
    "GuessTheWord-Starter.2"
    "GuessTheWord-Starter.3"
    "GuessTheWord-Starter.4"
    "TrackMySleepQuality-Starter"
    "Update2"
    "FirstUpdateee"
    "FirstApp_newTest"
    "MyApplication2"
    "NewFirst"
    "NewFirstttttttt"
    "NewFirstapp"
    "newFirstappp"
    "NewFirstAppHomeee"
    "RecyclerViewFundamentals-Starter"
    "MarsRealEstate-Starter"
    "Addgit-8"
    "8Apigit"
    "Project"
    "ProjectVideo"
    "ProjectVideoV2"
    "line-chatbot-one"
)

ARCHIVED_COUNT=0
FAILED_COUNT=0
SKIPPED_COUNT=0

echo "📦 REPOSITORIES TO ARCHIVE: ${#OLD_REPOS[@]}"
echo ""
echo "=================================="

# Process each repository
for repo in "${OLD_REPOS[@]}"; do
    repo_full="LifeStly/$repo"
    
    echo "⏳ Processing: $repo_full"
    
    # ✅ Check if repo exists
    if gh repo view "$repo_full" &> /dev/null; then
        # 📝 Get current status
        is_archived=$(gh repo view "$repo_full" --json isArchived -q '.isArchived')
        
        if [ "$is_archived" = "true" ]; then
            echo "  ✅ Already archived - SKIPPED"
            ((SKIPPED_COUNT++))
        else
            # 🔒 Archive the repository
            if gh repo archive "$repo_full" --confirm 2>/dev/null; then
                echo "  ✅ ARCHIVED successfully"
                ((ARCHIVED_COUNT++))
            else
                echo "  ❌ FAILED to archive"
                ((FAILED_COUNT++))
            fi
        fi
    else
        echo "  ⚠️  Repository not found - SKIPPED"
        ((SKIPPED_COUNT++))
    fi
    
    echo ""
done

echo "=================================="
echo ""
echo "📊 SUMMARY:"
echo "  ✅ Archived:  $ARCHIVED_COUNT"
echo "  ⚠️  Skipped:  $SKIPPED_COUNT"
echo "  ❌ Failed:   $FAILED_COUNT"
echo ""
echo "🎉 Process Complete!"
echo ""
echo "💡 NEXT STEPS:"
echo "  1. Check your GitHub profile - old repos should be hidden now"
echo "  2. They're still accessible if you know the link (read-only)"
echo "  3. To unarchive: gh repo unarchive LifeStly/RepoName --confirm"
echo ""
