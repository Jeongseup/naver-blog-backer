from naverblogbacker.utils import isEmptyDirectory

def main():
    myPath = 'C:\Jeongseup\python_test'

    # 빈 폴더 경로가 아니면 종료한다.
    if not isEmptyDirectory(dirPath=myPath):
        exit(-1)

if __name__ == '__main__':
    main()
