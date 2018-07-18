import quoteman as qm


target_url = "http://quotes.toscrape.com"
all_quotes = qm.list_all_quotes(target_url)
qm.write_quotes(all_quotes)
