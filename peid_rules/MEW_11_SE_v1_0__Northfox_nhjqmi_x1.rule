rule _MEW_11_SE_v1_0__Northfox_nhjqmi
{
	meta:
		description = "MEW 11 SE v1_0 __ Northfox"
	strings:
		$a = {E9????????000000020000000C?0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
