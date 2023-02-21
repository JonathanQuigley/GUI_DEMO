git init
git config user.email "j1quigley@student.bridgew.edu"
git config user.name "JonathanQuigley"
git add .
echo 'Enter a commit comment'
read commit_comment
git commit -m "$commit_comment"
echo 'Enter the remote origin URL'
read remote_URL
git remote add origin "$remote_URL"
git branch -M main
git push origin main