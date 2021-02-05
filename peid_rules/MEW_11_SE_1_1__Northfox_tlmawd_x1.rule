rule _MEW_11_SE_1_1__Northfox_tlmawd
{
	meta:
		description = "MEW 11 SE 1_1 __ Northfox"
	strings:
		$a = {E9????????000000020000000C00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
