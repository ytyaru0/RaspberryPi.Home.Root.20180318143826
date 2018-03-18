dir=/tmp/work/
if [ ! -d $dir ]; then
    #now=`date "+%Y%m%d%H%M%S"`
    #mkdir /tmp/work.${now}/
    mkdir "$dir"
fi
#uploader=GitHub.Uploader.Pi3.Https.201802210700
#source=/home/pi/root/script/py/${uploader}
#if [ ! -d $dir$uploader ]; then
#    cp -r "$source" "$dir$uploader"
#fi
cd "$dir"
unset dir
#unset uploader
#unset source
