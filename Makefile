export PYTHONPATH := src:$(PYTHONPATH)

default: clean_derived collate wrangle

# by default, we don't attempt to fetch new data

fetch:
	./src/stash/fetch_zips.py

unpack:
	./src/stash/unzip_zips.py


stash: fetch unpack

collate:
	./src/collate/collate_nation.py
	./src/collate/collate_states.py
	./src/collate/collate_terr.py

wrangle:
	./src/wrangle_data.py




# publish:
# 	./src/publish_viz.py

# ### CLEANING/DELETION STUFF
# clean: clean_derived


clean_all: clean_stashed clean_derived

clean_derived:
	rm -rf data/collated data/wrangled

clean_stashed:
	rm -rf data/stashed
