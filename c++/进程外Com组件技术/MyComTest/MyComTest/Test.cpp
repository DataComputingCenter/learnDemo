// Test.cpp : Implementation of CTest

#include "stdafx.h"
#include "Test.h"


// CTest



STDMETHODIMP CTest::AddNum(LONG num1, LONG num2, LONG* numRst)
{
	// TODO: Add your implementation code here
	*numRst=num1+num2;
	return S_OK;
}
