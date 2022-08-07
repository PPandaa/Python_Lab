if __name__ == '__main__':
    dic = {"affordable": 0, "expensive": 3, "cheap": 5, "very expensive": 0}
    print(max(dic, key=dic.get))