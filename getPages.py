def getSummaryPages(langdata):
	getSummaryPageslist = []
	for x in langdata:
		getSummaryPageslist.append('http://stats.wikimedia.org/EN/Summary' + x + '.htm')
	return getSummaryPageslist


def getTablePages(langdata):
	getTablesPageslist = []
	for x in langdata:
		getTablesPageslist.append('http://stats.wikimedia.org/EN/TablesWikipedia' + x + '.htm')
	return getTablesPageslist 