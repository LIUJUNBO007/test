import cx_Oracle
import paramiko
class MyOracle():
    def __init__(self,userName,userPasswd,TNS):
        if userName != 'sys':
            self.conn = cx_Oracle.connect(userName+ '/' + userPasswd + '@' + TNS)
        else:
            self.conn = cx_Oracle.connect(userName + '/' + userPasswd + '@' + TNS,mode=cx_Oracle.SYSDBA)
        self.cursor = self.conn.cursor()

    #查询函数
    def selectDatas(self,selectSql):
        self.cursor.execute(selectSql)
        rows = self.cursor.fetchall()
        for row in rows:
            print("%d %s" % row)

    #批量插入函数
    def batchInsertDatas(self,batchInsertSql,batchInsertDatas):
        self.cursor.executemany(batchInsertSql,batchInsertDatas)
        self.conn.commit()

    #删除函数
    def deleteDatas(self,deleteSql):
        print("Begin deleting...")
        self.cursor.execute(deleteSql)
        print(str(self.cursor.rowcount) + " has be deleted.")
        self.conn.commit()
        print("End deleting...")

    #关闭连接函数
    def closeConn(self):
        self.cursor.close()
        self.conn.close()

#     my_oracle = MyOracle('scott','scott','TNS_PDB01')
#     myBatchInsertSql = "insert into scott.t1 values(:1,:2)"
#     myBatchInsertDatas = [
#         (1,'a'),
#         (2,'b'),
#         (3,'c'),
#         (4,'d'),
#         (5,'e'),
#         (6,'f'),
#         (7,'g'),
#         (8,'h')
# ]
#
#     mySelectSql = "select * from scott.t1 order by 1"
#
#     my_oracle.selectDatas(mySelectSql)
#     my_oracle.batchInsertDatas(myBatchInsertSql,myBatchInsertDatas)
#
#     myDeleteSql = "delete from scott.t1 where id in (1,2,3)"
#     my_oracle.deleteDatas(myDeleteSql)
#
#     my_oracle.selectDatas(mySelectSql)
#
#     my_oracle.closeConn()

if __name__ == '__main__':

    with paramiko.Transport(('192.168.20.150', 22)) as trans:
        trans.connect(username='root', password='root123')
        ssh = paramiko.SSHClient()
        ssh._transport = trans
        stdin, stdout, stderr = ssh.exec_command('cat /etc/my.cnf')
        my_cnf = stdout.read().decode()
        # print(type(my_cnf),my_cnf)
        print(my_cnf)