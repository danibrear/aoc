from watchgod import watch

executionCount = 1
for changes in watch('./'):
    try:
        file = list(changes)[0][1]
        if file.startswith('./day') and file.endswith('.py'):
            print('\n\n[{}]--------------------\nRunning'.format(executionCount), file)
            exec(open(file).read())
            executionCount += 1
        elif file.startswith('./day') and file.endswith('.txt'):
            pyfile = file.replace('.txt', '.py')
            print('\n\n[{}]--------------------\nRunning'.format(executionCount), pyfile)
            exec(open(pyfile).read())
            executionCount += 1
    except:
        continue