rm all.list
cat *.list >> all.temp
mv all.temp all.list

aspell --lang=en create master ./cs.dict < all.list
