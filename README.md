GAS_manual_webcrawler
=====================

Crawls GNU's website and downloads all the manual pages for the assembler.

Just run `python GAScrawler.py` and let the program handle the rest.
Feel free to play with the sleep values.

Index.txt is just the list of all the URLs

Creating your own index file:
    Take the source from https://sourceware.org/binutils/docs/as/index.html
    Take all strings that match this regex:  `<a.*?href.*?</a>`. This will take all the links.
    Remove all strings that match this regex:  `</?[b-z].*?>`. This will remove all non-links.
    Remove all strings that match: `</a>` and `<a.*?href.*?"`.
    Replace all strings `">` with newlines.
    Swap every other pair of lines. You may choose to insert whitespaces at this point.
    
One-liners:
Create Index file:
    `curl https://sourceware.org/binutils/docs/as/index.html | grep -o -P '<a.*?href.*?</a>' | perl -pe 's/<\/?[b-z].*?>//g' | perl -pe 's/<\/a>//' | perl -pe 's/<a.*?href.*?"//' | perl -pe 's/">/\n/' | awk '{getline x; print x "\n    " $0}' > Index.txt`
Check for updates (no output/return 0 = no updates):
    `diff <(curl https://sourceware.org/binutils/docs/as/index.html | grep -o -e 'version [0-9]\.[0-9][0-9]' | perl -pe 's/version //') <(grep -o -e 'version [0-9]\.[0-9][0-9]' ./index.html | perl -pe 's/version //')`
