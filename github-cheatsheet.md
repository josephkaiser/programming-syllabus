GitHub & Git CLI Cheat Sheet for Personal Projects

One-page reference guide for solo developers using GitHub and Git CLI
Includes deploy keys, commit workflow, and branching basics

---

## 1️⃣ Repository Setup

git init

git remote add origin [git@github.com](mailto:git@github.com):USERNAME/REPO_NAME.git

git remote -v

---

## 2️⃣ First Commit & Push

git add .
git commit -m "Initial commit"
git push -u origin main

---

## 3️⃣ Updating Your Local Repo

git fetch origin
git merge origin/main
git pull origin main

---

## 4️⃣ Branching Wokkflow

git checkout -b feature/awesome-feature
git add .
git commit -m "Add awesome feature"
git checkout main
git merge feature/awesome-feature
git push origin main

---

## 5️⃣ Tags & Milestones

git tag -a v1.0 -m "First functional version"
git push origin --tags

---

## 6️⃣ Deploy Key Setup (SSH)

ssh-keygen -t ed25519 -C "[deploy@myproject.com](mailto:deploy@myproject.com)" -f ~/.ssh/deploy_key

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/deploy_key
ssh -T [git@github.com](mailto:git@github.com)

---

## 7️⃣ Commit & Author Management

git config user.name "Your Name"
git config user.email "[you@newaccount.com](mailto:you@newaccount.com)"

# Or globally

git config --global user.name "Your Name"
git config --global user.email "[you@newaccount.com](mailto:you@newaccount.com)"

---

## 8️⃣ Useful Status & History Commands

git status
git log --oneline --graph --decorate --all
git diff --staged

---

## 9️⃣ Removing Sensitive Files

git rm --cached path/to/file
echo "path/to/file" >> .gitignore
git commit -m "Stop tracking sensitive file"
git push

---

Tips:

* Commit often with descriptive messages.
* Use feature branches even for solo projects.
* Keep .env and secrets out of your repo.
* Regularly push to GitHub to maintain backup.
* Use tags for milestones or releases.

