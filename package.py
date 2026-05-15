#!/usr/bin/env python3
"""Package the skill into a .skill file for distribution."""
import sys
import os

# Workaround for Windows console encoding
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

# Import and run the packager
skill_creator_path = os.path.join(os.path.dirname(__file__), '..', 'skill-creator')
if not os.path.isdir(skill_creator_path):
    print("Error: skill-creator not found at", skill_creator_path)
    print("Clone it from github and place it as a sibling directory:")
    print("  git clone <skill-creator-repo> ../skill-creator")
    sys.exit(1)
sys.path.insert(0, skill_creator_path)
from scripts.package_skill import package_skill

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = script_dir
    dist_dir = os.path.join(script_dir, "dist")
    os.makedirs(dist_dir, exist_ok=True)
    result = package_skill(skill_dir, dist_dir)
    sys.exit(0 if result else 1)
