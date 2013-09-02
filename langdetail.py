from getSource import *
from getPages import *

def visitSummaryPage(summaryPageList):
	summaryDetail = ['Article Count','New Articles per Day','Edits per Month']

	for x in  summaryPageList:
		data = get_source(x)
		data1 = extractSummaryData(data,summaryDetail)
		print x 
		print data1

def visitTablePage(tablePageList):
	tableDetail = []

	for x in tablePageList:
		data = get_source(x)
		data1 = extractTableData(data)
		print x
		print data1

def extractTableData(data):
	st = "<tr bgcolor='#ffdead'><td colspan=333 class=cb><img src='../black.gif' height='1' alt=''></td></tr><tr>"
	#print data.find(st)
	data1 = data[data.find(st) + len(st): data.find(st) + len(st)  + 200]
	#print data1

	li = []
	for x in range(5):
		td = '<td class=rb>'
		tdover = '</td>'
		start = data1.find(td)
		li_ind = data1[start + len(td):data1.find(tdover)]
		if li_ind.find('&nbsp;') != -1:
			li_ind = li_ind.replace('&nbsp;',' ')
		li.append(li_ind)
		data1 = data1[data1.find(tdover) + len(tdover):]
		#print data1

	return li


def extractSummaryData(data,summaryDetail):
	articleCount = data.find(summaryDetail[0])
	articleCountData = data[articleCount:]
	#print articleCountData
	articleCount = articleCountData.find('<td class=r>')
	#print articleCount
	articleCountData = articleCountData[articleCount + len('<td class=r>') : ]
	#print articleCountData
	articleCount1  = articleCountData[:articleCountData.find('</td>')]

	newArticle = data.find(summaryDetail[1])
	newArticleData = data[newArticle:]
	#print newArticleData
	newArticle = newArticleData.find('<td class=r>')
	#print newArticle
	newArticleData = newArticleData[newArticle + len('<td class=r>') : ]
	#print newArticleData
	newArticle1  = newArticleData[:newArticleData.find('</td>')]

	editMonth = data.find(summaryDetail[2])
	editMonthData = data[editMonth:]
	#print editMonthData
	editMonth = editMonthData.find('<td class=r>')
	#print editMonth
	editMonthData = editMonthData[editMonth + len('<td class=r>') : ]
	#print editMonthData
	editMonth1  = editMonthData[:editMonthData.find('</td>')]

	return [articleCount1,newArticle1,editMonth1]
#def summaryPage
#webpage = "http://stats.wikimedia.org/EN/Sitemap.htm"

langlist = ['BN','HI','OR','TE','AS','HI','GU','ML','MR','NE','PA','SA','TA']
summaryPageList = getSummaryPages(langlist)
tablePageList = getTablePages(langlist)

#print summaryPageList
visitSummaryPage(summaryPageList)
visitTablePage(tablePageList)


summaryDetail = ['Article Count','New Articles per Day','Edits per Month']