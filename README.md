GAS_manual_webcrawler
=====================

Crawls GNU's website and downloads all the manual pages for the assembler.

Just run `python GAScrawler.py` and let the program handle the rest. Feel free to play with the sleep values.

If you want to update, you may want to run `rm *.html` prior to running the crawler.

Index.txt is just the list of all the URLs (2.24).
Index.2.25.txt is the list for version 2.25.

One-liners:
- Create Index file:
    `curl https://sourceware.org/binutils/docs/as/index.html | grep -o -P '<a.*?href.*?</a>' | perl -pe 's/<\/?[b-z].*?>//g' | perl -pe 's/<\/a>//' | perl -pe 's/<a.*?href.*?"//' | perl -pe 's/">/\n/' | awk '{getline x; print x "\n    " $0}' > Index.txt`
- Check for updates (no output/return 0 = no updates):
    `diff <(curl https://sourceware.org/binutils/docs/as/index.html | grep -o -e 'version [0-9]\.[0-9][0-9]' | perl -pe 's/version //') <(grep -o -e 'version [0-9]\.[0-9][0-9]' ./index.html | perl -pe 's/version //')`
