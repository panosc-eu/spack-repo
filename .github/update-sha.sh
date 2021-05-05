#!/bin/bash

# Script to update the SHA version

# get name and version from dependabots last commit message
last_commit=$(git log --author=dependabot --pretty=oneline -1)
name=$(echo $last_commit | grep -o -P '(?<=Bump ).*(?= from)')
old_version=$(echo $last_commit | grep -o -P '(?<=from ).*(?= to)')
new_version=$(echo $last_commit | grep -o -P '(?<=to ).*(?= in)')

# find corresponding package file
cd ../packages/
directory=$(find . -maxdepth 1 -name '*'$name'*' -print)
cd $directory

# substitute new url of updated version
old_url_line=$(cat package.py | grep "url.*=.*${old_version}.*")
new_url_line=$(echo "${old_url_line/$old_version/$new_version}")
sed -i "s#$old_url_line#$new_url_line#g" package.py

# download new package
new_url=$(echo $new_url_line | grep -o -P '(?<=").*(?=")')
file_extension=$(echo $new_url | grep -o -P "(?<=${new_version}\.).*(?=)")
package=$(echo $name'-'$new_version'.'$file_extension)
wget -O $package $new_url

# create sha256 sum, remove file again
sha256_new=$(sha256sum $package | awk '{print $1}')
rm $package

# replace version and sha
sha256_old_line=$(cat package.py | grep "version('$old_version'")
sha256_old=$(echo $sha256_old_line | grep -o -P "(?<=sha256=').*(?='\))")
new_sha_line=$(echo "${sha256_old_line/$old_version/$new_version}")
new_sha_line=$(echo "${new_sha_line/$sha256_old/$sha256_new}")
sed -i "/$sha256_old_line/i\\$new_sha_line" package.py

# commit and push to PR branch
git commit package.py -m "Update SHA256 in $name from $old_version to $new_version"
PR_branch="dependabot/pip/dot-github/dependabot/$name-$new_version"
git push origin PR_branch
