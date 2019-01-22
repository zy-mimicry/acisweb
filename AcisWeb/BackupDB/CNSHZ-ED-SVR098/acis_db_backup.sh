#! /bin/bash

DB_RSYNC_DIR=/ACIS_DB_BACKUP
DUMP_FILE=healthy.sql
Comp_DUMP_FILE=healty.sql.tgz
TIMESTAMP=`date +%Y-%m-%d:%H-%M-%S`

cd $DB_RSYNC_DIR;
mysqldump -u root -p 1234 --quick --all-databases --flush-logs --single-transaction > $DUMP_FILE
tar zcf $Comp_DUMP_FILE $DUMP_FILE

DONE=$?
echo $DONE

if [ ! -d "./.git" ]; then
  git init && git add ./ && git commit -m "DB backup Repo Init.[$TIMESTAMP]"
fi

git add ./ && git commit -m "DB backup. [$TIMESTAMP]"

cd -;
exit 0
