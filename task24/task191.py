print(len(list(filter(lambda el: len(el) >= 15 and 'B' not in el, open('24-191.txt').readline().split('A')[1:-1]))))