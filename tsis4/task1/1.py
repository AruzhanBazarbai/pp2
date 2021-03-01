import re

with open('raw.txt','r',encoding='utf-8 ') as f:

    all_lines=' '.join(f.readlines())#соединяет массивы

company_name=re.search(r'ДУБЛИКАТ\n(.+)\n',all_lines).group(1) #вытащит первую группу

bin_number=re.search(r'БИН (\d+)',all_lines).group(1) #берет первую группу только, так как слово БИН не нужно

items_titles=re.findall(r'\d\.\n(.+)\n',all_lines)

items_couts=re.findall(r'[0-9][,][0-9]{3}',all_lines) 

items_unit_prices=re.findall(r'x\s(.+,\d+)',all_lines)#если задать в паттерне группу, то файндалл выведет только группу

items_total_prices=re.findall(r'Стоимость\n(.+)\n',all_lines)

date=re.search(r'Время:\s(.+)\n',all_lines).group(1)

address=re.search(r'(г\.\s.+\n)',all_lines).group(1)

#выведем все

print("1.Name of the company:",company_name,end='\n\n')

print("2.BIN number:",bin_number,end='\n\n')

print("3.For each item:",end='\n\n')

for i in range(len(items_titles)):

    print("     1.Title----",items_titles[i])

    print("     2.Cout----",items_couts[i])

    print("     3.Unit price----",items_unit_prices[i])

    print("     4.Total price----",items_total_prices[i],end='\n\n')

print("4.Date----",date,end='\n\n')

print("5.Address----",address)


