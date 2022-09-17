rule _VMProtect_0_x__PolyTech_tltygo
{
	meta:
		description = "VMProtect 0_x __ PolyTech"
	strings:
		$a = {5B20564D50726F7465637420}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
