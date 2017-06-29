// MyComTest.cpp : Implementation of WinMain


#include "stdafx.h"
#include "resource.h"
#include "MyComTest_i.h"



class CMyComTestModule : public ATL::CAtlExeModuleT< CMyComTestModule >
	{
public :
	DECLARE_LIBID(LIBID_MyComTestLib)
	DECLARE_REGISTRY_APPID_RESOURCEID(IDR_MYCOMTEST, "{A4035479-1302-4EFA-9231-4AB101BCF561}")
	};

CMyComTestModule _AtlModule;



//
extern "C" int WINAPI _tWinMain(HINSTANCE /*hInstance*/, HINSTANCE /*hPrevInstance*/, 
								LPTSTR /*lpCmdLine*/, int nShowCmd)
{
	return _AtlModule.WinMain(nShowCmd);
}

