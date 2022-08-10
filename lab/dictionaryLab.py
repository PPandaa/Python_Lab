if __name__ == '__main__':
    dic = {"affordable": 0, "expensive": 3, "cheap": 5, "very expensive": 5}
    print(max(dic, key=dic.get))

    predictionKeys = []
    for key, value in dic.items():
        if value == dic.get(max(dic, key=dic.get)):
            predictionKeys.append(key)
    print(predictionKeys)