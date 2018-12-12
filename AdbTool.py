# -*- coding: cp936 -*-
import os,subprocess
import time

#���ڻ�ȡ�ֻ��Ƿ����ӵ���
def connectDevice():
    '''����豸�Ƿ����ӳɹ�������ɹ�����True�����򷵻�False'''
    try:
        '''��ȡ�豸�б���Ϣ'''
        deviceInfoTemp= subprocess.check_output('adb devices')
        deviceInfo = deviceInfoTemp.decode()
        
        '''��������豸�ɹ�����true�����򷵻�false'''
        if "	device" in deviceInfo:
            return True
        else:
            return False
    except Exception as err:
        print("Device Connect Fail:" + err)


#���ڽ�lua_log�ļ�����������
def copyLuaLogFile():
    date = input("������lua_log���ڣ����磺4��19�յ�log���� 0419����")
    
    path = "/sdcard/jjlog_lua_" + str(date) + ".log"
    pullsheel = "adb pull " + str(path) + " f:"

    print("���ڵ��������Ե�...")

    os.system(pullsheel)

    object_file = "f:\\jjlog_lua_" + str(date) + ".log" 
    if os.path.exists(object_file):
        print("�����ɹ���")
    else:
        print("����ʧ�ܣ�")


#���ڽ�android_log�ļ�����������
def copyAndroidLogFile():
    date = input("������android_log���ڣ����磺4��19�յ�log���� 0419����")
    
    path = "/sdcard/jjlog_android_" + str(date) + ".log"
    pullsheel = "adb pull " + str(path) + " f:\\"

    print("���ڵ��������Ե�...")

    os.system(pullsheel)

    object_file = "f:\\jjlog_android_" + str(date) + ".log" 
    if os.path.exists(object_file):
        print("�����ɹ���")
    else:
        print("����ʧ�ܣ�")
    
	
#�������
"""�ж��ֻ��Ƿ����ӳɹ����������ʧ�����û�ѡ���Ƿ����³�������"""
while not connectDevice():
    print("�����ֻ�ʧ�ܣ���ȷ���ֻ���USB���ԣ�")
    result = input("���� 1 ���³��ԣ����� 2 �˳�����")
    if result == 1:
        continue
    else:     
        break

        
if connectDevice():
    print("�ɹ������ֻ���")
    logType = input("�����뵼��log���ͣ����� lua_log ������ 1 ������ android_log ������ 2����")
    if logType == 1:
        copyLuaLogFile()
    else:
        copyAndroidLogFile()
    
    time.sleep(3)
else:
    print("�����˳�������...")
    
    time.sleep(3)



