from datamanager import DataMenager

host='192.168.1.10'
user='root'
password='123456'
db='mercado'
port=3307
url =""

data = DataMenager(host=host,user=user,password=password,db=db,port=port)

def main():
    getData(data,url)

if __name__ == "__main__":
    main()