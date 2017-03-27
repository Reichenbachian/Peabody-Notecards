# util.sh
#
# Note: GhostScript must be installed to use this
#

if [ "$1" == "merge" ]
then
    pushd "$2"
    for f in *
    do
        echo "Moving files from $f"
        pushd "$f"
        cp * ../ -fpv
        popd
        
        echo "Removing $f"
        rm "$f" -fR
    done 
    popd

elif [ "$1" == "convert" ]
then

    ACCNO=$2
    CATNO=$3

    # This is the path to the peabody_files directory
    ROOT=$4

    # Path to the ghostscript executable
    GS=$5

    pushd "${ROOT}"

    "$GS" -dNOPAUSE -r300 -sDEVICE=tiffscaled24 -sCompression=lzw -dBATCH -sOutputFile=${ACCNO}_${CATNO}.tif ${ACCNO}_${CATNO}.pdf

    popd

fi 


