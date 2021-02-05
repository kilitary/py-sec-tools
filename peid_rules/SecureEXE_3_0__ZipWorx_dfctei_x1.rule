rule _SecureEXE_3_0__ZipWorx_dfctei
{
	meta:
		description = "SecureEXE 3_0 __ ZipWorx"
	strings:
		$a = {E9B8000000??????00??????00??????000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
