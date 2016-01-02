.PHONY: all build-addon deploy-webtask clean

all: clean build-ami plan apply

build-addon:
	src = script.timewasted.src
	dest = script.timewasted

	rm -rf $(dest)
	rm $(dest)-0.1.zip

	mkdir -p $(dest)

	cp $(src)/addon.xml $(dest)/
	cp $(src)/*.txt $(dest)/
	cp $(src)/icon.png $(dest)/
	cp $(src)/*.py $(dest)/
	cp -r $(src)/resources $(dest)/

	zip -r $(dest)-0.1.zip $(dest)
	rm -rf $(dest)

deploy-webtask:
	http $(wt create webtask/dummy.js)
