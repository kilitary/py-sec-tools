rule _LCC_Win32_v1_x_lveddl
{
	meta:
		description = "LCC Win32 v1_x"
	strings:
		$a = {64A1????????5589E56AFF68????????689A1040??50}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
