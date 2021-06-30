#!/bin/bash

set -x

# Script to update the SHA version

# get name and version from dependabots last commit message
last_commit=$(git log --author=dependabot --pretty=oneline -1)

if [[ $last_commit =~ .*Bump.*from.*to.* ]]
then
    name=$(echo $last_commit | grep -o -P '(?<=Bump ).*(?= from)')
    new_version=$(echo $last_commit | grep -o -P '(?<=to ).*(?= in)')

    # find corresponding package file
    # CI executes at the root of the repository
    cd ./packages/
    directory=$(find . -maxdepth 1 -name '*'$name'*' -print)
    cd $directory

    # substitute new url of updated version
    old_url=$(cat ./package.py | grep 'url * = *"https' -m 1 | grep -oP '"\K[^"\047]+(?=["\047])')
    old_file=$(basename -- ${old_url})
    old_version=$(echo ${old_file} | sed -e "s/.bz2//;s/.dmg//;s/.tgz//;s/.gz//;s/.zip//;s/.xz//;s/.tar//;")
    old_url_line=$(cat package.py | grep "url.*=.*${old_version}.*")
    new_url_line=$(echo "${old_url_line/$old_version/$new_version}")
    sed -i "s#$old_url_line#$new_url_line#g" package.py

    # download new package
    new_url=$(echo $new_url_line | grep -o -P '(?<=").*(?=")')
    file_extension=$(echo $new_url | grep -o -P "(?<=${new_version}\.).*(?=)")
    package=$(echo $name'-'$new_version'.'$file_extension)
    wget -O $package $new_url

    # create sha256 sum, remove file again
    new_sha256=$(sha256sum $package | awk '{print $1}')
    rm $package

    # replace version and sha
    old_sha256_line=$(cat package.py | grep "version('$old_version'")
    old_sha256=$(echo $old_sha256_line | grep -o -P "(?<=sha256=').*(?='\))")
    new_sha_line=$(echo "${old_sha256_line/$old_version/$new_version}")
    new_sha_line=$(echo "${new_sha_line/$old_sha256/$new_sha256}")
    sed -i "/$old_sha256_line/i\\$new_sha_line" package.py
fi
