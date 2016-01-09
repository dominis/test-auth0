SRC = script.timewasted.src
DEST = script.timewasted
VERSION = 0.$(shell date +%s)

dist-addon: clean pack-addon

pack-addon:
	mkdir -p $(DEST)

	cp $(SRC)/addon.xml $(DEST)/
	sed -i s/##VERSION##/$(VERSION)/g $(DEST)/addon.xml
	cp $(SRC)/icon.png $(DEST)/
	cp $(SRC)/*.py $(DEST)/

	zip -r $(DEST)-$(VERSION).zip $(DEST)
	rm -rf $(DEST)

deploy-webtask:
	wt create webtask/dummy.js --secret REDIS_PASS=${REDIS_PASS}

clean:
	rm -rf $(DEST)
	rm -rf $(DEST)*.zip
