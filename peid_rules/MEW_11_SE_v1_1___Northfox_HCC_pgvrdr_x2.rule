rule _MEW_11_SE_v1_1___Northfox_HCC_pgvrdr
{
	meta:
		description = "MEW 11 SE v1_1  __ Northfox _HCC"
	strings:
		$a = {E9??????FF0C}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
