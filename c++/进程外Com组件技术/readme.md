## һ������һ��������com���
1. ��VS2010�����File->New->Project��ѡ��Atl->Atl Project�����빤����MyComTest��ȷ�Ϻ���Next��
 
2. ע��ѡ��ڶ���Executable(EXE)����ɡ�
    Dynamic Link Library(DLL) ��ʾ����һ�� DLL ��������򣨽������������
    Executable(EXE) ��ʾ����һ�� EXE ��������򣨽������������
Service(EXE) ��ʾ����һ���������ϵͳ������ͻ���ز�ִ�еĳ���
 
3. ע��ѡ��ڶ���Executable(EXE)����ɡ�
4. �������һ�Add->Class��������ѡ��Atl Simple Object�����Add��
 
5. ����������Short name�Լ�ProgID��������.��������Next��
 
6. ע�������Aggregationѡ��No����ɡ�
 
7. ������������һ���յĽӿڣ�������Ҫ��ӷ��������ϵ��á�������ͼ���ڸղŴ����Ķ���Ľӿ�ITest���һ�Add->Add Method��
 
8. ���һ��AddNum�ķ����������������������(in)��һ���������(retval)����ɺ󣬵��Next��Finish��
 
9. �����ڹ���������AddNum��������Щ�ļ������ı䣬�Ժ�Ҳ����ͨ���ֶ��ı���Щ�ļ�������ӷ�����
 
10. �ڷ�����������룬����ɹ���������AddNum�ֶΣ�ע�����ǰ��֤VS���Թ���Ա������еģ��������ɹ�������Զ�ע��ʧ�ܡ�
 
11. ����һ��Exe����MyClient����stdafx.h�������������ɵ�tlb�ļ���
 
12. ���ô������£�

> ���doc�ĵ�
 
13. �����������£�


> ���doc�ĵ�


 
14. ���Configuration Manager��

> ���doc�ĵ�
 
15. ����ͼ���New���½�һ���������á�

> ���doc�ĵ�
  
16. ����ͼ���New��

> ���doc�ĵ�
 
17. ���OK�����һ��64λ��������á�

> ���doc�ĵ�
 
18. ���µ����ñ��룬���У�������£�
 
> ���doc�ĵ�

## ���� �Զ���ṹ�����鴫�ݲ���

[http://blog.csdn.net/worldy/article/details/11850379](http://blog.csdn.net/worldy/article/details/11850379)

## ������sde����
1. ����Ⱦ��ȡ
  Com ���룺���Ӳ���
             ͼ����
       ���������
            ����
   1. ��BSTR���ݲ���      ReadLayer
   2. ��SAFEARRAY���ݲ���  ReadLayerOneStr
2. ����Ⱦ��ȡ
 Com ���룺���Ӳ���
            ͼ����
            ��Ⱦ���ò��� 
            ��������
       �����BOOL
    1. ��BSTR���ݲ���      GetLyC
    2. ��SAFEARRAY���ݲ���  GetLyB
3. ����ͨ���ȡ
   AE������ȡ��TestGetLy
  COM������ȡ��TestGetLyB

   

