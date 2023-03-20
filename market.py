# market 이라는 list 변수 생성
market = []

while True:
	mode = int(input())
	
	# 상품 추가 모드 (상품명, 상품가격, 상품카테고리, 제조사를 입력받음) - 
	if mode == 1:
		flag = 0		# 추가하려는 상품은 이미 존재하지 않는다고 판단.
		item_name = input()
		item_price = int(input())
		item_category = input()
		item_corp = input()
		
		item = {
			"상품명": item_name,
			"상품 가격": item_price,
			"상품 카테고리": item_category,
			"제조사": item_corp
		}
		
		for i in market:
			if i['상품명'] == item['상품명']:
				print('상품 존재')
				flag = 1
				break
		if flag == 1:
			continue
		elif flag == 0:
			market.append(item)
			print('상품 등록')

	# 상품 삭제 모드 (상품명을 입력받아 삭제함) - OK
	if mode == 2:
		isDeleted = 0		# 삭제하려는 상품이 없다고 판단. 
		item_name = input()
		
		for item in market:
			if item['상품명'] == item_name:
				market.remove(item)
				isDeleted = 1
				print('상품 삭제')
				break
		if isDeleted == 1:
			continue
		elif isDeleted == 0:
			print('상품 없음')

	# 상품 제조사 검색 모드 (제조사를 입력받아 찾아줌.) - 문자열 오름차순을 기준으로 한다는 것에서 수정해봐야 할듯
	if mode == 3:
		item_corp = input()
		printList = []
		
		for item in market:
			if item['제조사'] == item_corp:
				printList.append(item['상품명'])
		
		if len(printList) > 0:
			printList.sort()
			
			for name in printList:
				print(name)
		else:
			print('제조사 없음')

	# 가격별 정렬 모드 (1: 오름차순, 2: 내림차순)	- OK
	if mode == 4:
		if len(market) < 1:
			continue
		user_input = int(input())
		printCount = 0
		if user_input == 1:
			market_copy = sorted(market, key=lambda market: market['상품 가격'])	# 특정 값을 기준으로 정렬
		if user_input == 2:
			market_copy = sorted(market, key=lambda market: market['상품 가격'], reverse=True)
	
		for item in market_copy:
			if (printCount > 3):
				break
			else:
				print('{} {} {} {}'.format(item['상품명'], item['상품 가격'], item['상품 카테고리'], item['제조사']))
			printCount += 1
		
	# 종료 모드 (종료하기 전에 현재 존재하는 상품의 개수를 출력 ex) 3 상품 존재) - OK
	if mode == 5:
		count = len(market)
		print('{} 상품 존재'.format(count))
		break
	