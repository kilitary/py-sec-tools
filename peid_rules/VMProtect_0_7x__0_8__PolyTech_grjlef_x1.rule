rule _VMProtect_0_7x__0_8__PolyTech_grjlef
{
	meta:
		description = "VMProtect 0_7x _ 0_8 __ PolyTech"
	strings:
		$a = {5B20564D50726F74656374207620302E382028432920506F6C7954656368205D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
