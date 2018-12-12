# -*- coding: cp936 -*-
import os,subprocess
import time

#��ȡ�ֻ��Ƿ����ӵ���
def connectDevice():
    '''����豸�Ƿ����ӳɹ�������ɹ�����True�����򷵻�False'''
    try:
        '''��ȡ�豸�б���Ϣ'''
        deviceInfoTemp = subprocess.check_output('adb devices')
        deviceInfo = deviceInfoTemp.decode()
        
        '''��������豸�ɹ�����true�����򷵻�false'''
        if "	device" in deviceInfo:
            return True
        else:
            return False
    except Exception as err:
        print("Device Connect Fail:" + err)


#��ȡ�ֻ��� abilist
def getAbilist():
    
    try:
        '''��ȡ�豸 CPU ��Ϣ'''
        CPUInfoTemp = subprocess.check_output('adb shell getprop ro.product.cpu.abilist')
        CPUInfo = CPUInfoTemp.decode()   
        print("���豸֧�� ABI ����Ϊ��" + str(CPUInfo)+"------------------------------------------------------------")

        if "arm64-v8a" in CPUInfo:
            print("֧�� 64 λ�� 32 λ��")
        elif "armeabi-v7a" or "armeabi"in CPUInfo:
            print("��֧�� 64 λ��֧�� 32 λ��")
        else:
    	    print("�Ȳ�֧�� 64 λ��Ҳ��֧�� 32 λ��")
		
    except Exception as err:
        print("��ȡ CPU ��Ϣʧ�ܣ�:" + err)

	
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
    print("------------------------------------------------------------")
    getAbilist();
    time.sleep(10)
else:
    print("�����˳�������...")    
    time.sleep(10)



