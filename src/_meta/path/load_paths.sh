# use
#   $ . <this-file-path>
THIS=$(cd $(dirname $0); pwd)
PARSER="${THIS}/load_ini.sh"
INI_FILES=`cd "${THIS}/ini/"; ls -1;`
INI_SECTION=Paths
for file in $INI_FILES; do
    INI_FILE="${THIS}/ini/${file}"
    . "${PARSER}" "${INI_FILE}" "${INI_SECTION}"
done
#echo $root_script
#echo $work_meta
