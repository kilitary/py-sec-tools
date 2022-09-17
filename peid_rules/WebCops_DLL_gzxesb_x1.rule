rule _WebCops_DLL_gzxesb
{
	meta:
		description = "WebCops _DLL"
	strings:
		$a = {A8BE58DCD6CCC4634A0FE002BBCEF35C5023FB62E73D2B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
